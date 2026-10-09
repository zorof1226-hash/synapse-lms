import os
import json
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import WEB_HOST, WEB_PORT, LMS_DOWNLOADS_DIR, EXPORTS_DIR, AUDIO_DIR
from db.database import Database
from pipeline import StudyPipeline
from repetition.weak_tracker import WeakTopicTracker
from repetition.cheat_sheet import CheatSheetGenerator
from exam.exam_engine import ExamEngine
from generation.llm_generator import LLMGenerator

app = FastAPI(title="Automated Study System API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()
pipeline = StudyPipeline(db=db)
weak_tracker = WeakTopicTracker(db=db)
cheat_gen = CheatSheetGenerator(db=db)
exam_engine = ExamEngine(db=db)
llm_gen = LLMGenerator()

STATIC_DIR = Path(__file__).resolve().parent / "static"

# ==================== API ENDPOINTS ====================

@app.get("/api/overview")
def get_overview():
    stats = db.get_stats_overview()
    exams = exam_engine.get_upcoming_exams()
    deadlines = exam_engine.check_deadlines_due_soon()
    courses = db.get_all_courses()
    return {
        "stats": stats,
        "upcoming_exams": exams,
        "deadlines": deadlines,
        "courses": courses
    }

@app.get("/api/courses")
def get_courses():
    return {"courses": db.get_all_courses()}

@app.post("/api/reset_previous_courses")
def reset_previous_courses():
    """Purges previous dummy courses and resets the system."""
    import shutil
    db.clear_all_previous_data()
    # Clean dummy folders
    for d in [LMS_DOWNLOADS_DIR, EXPORTS_DIR, AUDIO_DIR]:
        for item in d.glob("*"):
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            elif item.is_file() and item.name != "study_system.db":
                try:
                    item.unlink()
                except Exception:
                    pass
    return {"status": "success", "message": "All previous courses and files cleared."}

@app.post("/api/regenerate_mcqs")
def regenerate_mcqs():
    """Deletes all existing MCQs/flashcards and regenerates them using Gemini AI.
    Keeps courses, files, exams, and deadlines intact.
    """
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM files")
        total_files = cur.fetchone()[0]
        # Clear only generated content
        cur.execute("DELETE FROM quiz_attempts")
        cur.execute("DELETE FROM flashcards")
        cur.execute("DELETE FROM mcqs")
        cur.execute("DELETE FROM materials")
        # Reset all files back to pending so they get reprocessed
        cur.execute("UPDATE files SET status = 'pending', processed_at = NULL")
        conn.commit()

    # Re-run the generation pipeline
    processed = pipeline.process_pending_files()

    # Count new totals
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM mcqs")
        new_mcqs = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM flashcards")
        new_cards = cur.fetchone()[0]

    return {
        "status": "success",
        "files_reprocessed": len(processed),
        "total_files": total_files,
        "new_mcqs": new_mcqs,
        "new_flashcards": new_cards,
        "details": processed
    }

@app.post("/api/moodle/login")
def moodle_login(username: str = Form(...), password: str = Form(...), service: str = Form("moodle_mobile_app")):
    res = pipeline.moodle.login_with_credentials(username, password, service)
    if not res.get("success"):
        raise HTTPException(status_code=400, detail=res.get("error", "Login failed"))

    # Purge dummy demo courses
    reset_previous_courses()

    # Discover and register enrolled courses from NUST LMS
    courses = pipeline.moodle.get_enrolled_courses()
    synced_items = []
    course_names = []

    for c in courses:
        cid = c.get("id")
        code = c.get("fullname") or c.get("shortname") or f"Moodle_{cid}"
        course_names.append(code)
        print(f"[NUST Sync] Downloading materials for: {code} (ID: {cid})...")
        synced_items.extend(pipeline.moodle.sync_course_materials(cid, code))

    # Process all newly downloaded lecture slide decks
    processed = pipeline.process_pending_files()

    return {
        "status": "success",
        "token_acquired": True,
        "enrolled_courses": course_names,
        "synced_files": len(synced_items),
        "processed_materials": len(processed)
    }

@app.get("/api/mcqs")
def get_mcqs(course_id: Optional[str] = None, limit: int = 15, mode: Optional[str] = None):
    with db.get_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM mcqs"
        conditions = []
        params = []
        if course_id and course_id != "all":
            conditions.append("course_id = ?")
            params.append(course_id)
        # In 'revision' mode, show all MCQs; otherwise only AI-generated
        if mode != "revision":
            conditions.append("(generated_by = 'ai' OR generated_by IS NULL)")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY RANDOM() LIMIT ?"
        params.append(limit)
        cursor.execute(query, params)
        rows = cursor.fetchall()

    items = []
    for r in rows:
        item = dict(r)
        if isinstance(item.get("options"), str):
            item["options"] = json.loads(item["options"])
        items.append(item)
    return {"questions": items}

@app.get("/api/mcqs/all")
def get_all_mcqs(course_id: Optional[str] = None, limit: int = 50, mode: Optional[str] = None):
    """Returns all MCQs for revision (or only AI-generated ones in default mode)."""
    with db.get_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM mcqs"
        conditions = []
        params = []
        if course_id and course_id != "all":
            conditions.append("course_id = ?")
            params.append(course_id)
        if mode != "revision":
            conditions.append("(generated_by = 'ai' OR generated_by IS NULL)")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY RANDOM() LIMIT ?"
        params.append(limit)
        cursor.execute(query, params)
        rows = cursor.fetchall()

    items = []
    for r in rows:
        item = dict(r)
        if isinstance(item.get("options"), str):
            item["options"] = json.loads(item["options"])
        items.append(item)
    return {"questions": items}

@app.post("/api/mcqs/generate")
def generate_custom_mcqs(course_id: Optional[str] = Form("all"), count: int = Form(10), topic: Optional[str] = Form(None)):
    """Generates a specified number of high-quality AI MCQs on demand from course materials."""
    mcqs = pipeline.generate_mcqs_for_course(course_id=course_id, count=count, topic=topic)
    return {
        "status": "success",
        "generated_count": len(mcqs),
        "course_id": course_id,
        "questions": mcqs
    }

@app.delete("/api/mcqs/heuristic")
def delete_heuristic_mcqs(course_id: Optional[str] = None):
    """Purges all low-quality template/heuristic-generated MCQs and flashcards."""
    course_filter = None if (not course_id or course_id == "all") else course_id
    deleted_mcqs = db.delete_heuristic_mcqs(course_id=course_filter)
    deleted_fc = db.delete_heuristic_flashcards(course_id=course_filter)
    return {
        "status": "success",
        "deleted_mcqs": deleted_mcqs,
        "deleted_flashcards": deleted_fc,
        "message": f"Removed {deleted_mcqs} low-quality MCQs and {deleted_fc} heuristic flashcards."
    }

@app.post("/api/mcq/attempt")
def attempt_mcq(mcq_id: int = Form(...), user_answer: int = Form(...)):
    res = db.log_quiz_attempt(mcq_id, user_answer)
    return res

@app.post("/api/explain_stuck")
def explain_stuck(question: str = Form(...), correct_option: str = Form(...),
                  user_option: str = Form(...), explanation: str = Form(...)):
    res = llm_gen.explain_stuck(question, correct_option, user_option, explanation)
    return res

@app.get("/api/flashcards")
def get_flashcards(course_id: Optional[str] = None, mode: Optional[str] = None):
    course_filter = None if (course_id == "all" or not course_id) else course_id
    if mode == "all":
        cards = db.get_all_flashcards(course_id=course_filter, limit=200)
    else:
        cards = db.get_due_flashcards(course_id=course_filter, limit=30)
    return {"flashcards": cards}

@app.post("/api/flashcard/review")
def review_flashcard(card_id: int = Form(...), quality: int = Form(...)):
    db.update_flashcard_sm2(card_id, quality)
    return {"status": "success", "card_id": card_id}

@app.get("/api/weak_topics")
def get_weak_topics(course_id: Optional[str] = None):
    course_filter = None if (course_id == "all" or not course_id) else course_id
    return {"weak_topics": weak_tracker.get_topic_analytics(course_id=course_filter)}

@app.get("/api/weekend_quiz")
def get_weekend_quiz(course_id: Optional[str] = None):
    course_filter = None if (course_id == "all" or not course_id) else course_id
    questions = weak_tracker.generate_weekend_quiz(course_id=course_filter, total_questions=15)
    return {"questions": questions}

@app.get("/api/exams")
def get_exams():
    return {"exams": exam_engine.get_upcoming_exams()}

@app.post("/api/exams/add")
def add_exam(course_id: str = Form(...), exam_title: str = Form(...),
             exam_date: str = Form(...), target_score: int = Form(85), notes: str = Form("")):
    exam_id = exam_engine.add_exam(course_id, exam_title, exam_date, target_score, notes)
    return {"status": "success", "exam_id": exam_id}

@app.get("/api/mock_exam")
def get_mock_exam(course_id: str, question_count: int = 15, time_limit_minutes: int = 25):
    return exam_engine.generate_mock_exam(course_id, question_count, time_limit_minutes)

@app.get("/api/cheatsheet")
def get_cheatsheet(course_id: str):
    res = cheat_gen.generate_sheet(course_id)
    # Read generated markdown
    md_content = ""
    if Path(res["file_path"]).exists():
        with open(res["file_path"], "r", encoding="utf-8") as f:
            md_content = f.read()
    res["content"] = md_content
    return res

@app.post("/api/sync")
def trigger_sync(lms_type: str = Form("folder")):
    synced = pipeline.run_sync(lms_type)
    processed = pipeline.process_pending_files()
    return {
        "status": "success",
        "synced_count": len(synced),
        "processed_count": len(processed),
        "processed": processed
    }

@app.post("/api/upload_lecture")
async def upload_lecture(course_id: str = Form(...), week_num: int = Form(1), file: UploadFile = File(...)):
    target_dir = LMS_DOWNLOADS_DIR / course_id / f"Week_{week_num:02d}"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / file.filename

    content = await file.read()
    with open(target_file, "wb") as f:
        f.write(content)

    rec = db.record_file(course_id, target_file, week_num=week_num, lecture_title=file.filename)
    # Process pipeline immediately for uploaded lecture
    processed = pipeline.process_pending_files()

    return {
        "status": "success",
        "file_name": file.filename,
        "change": rec["change"],
        "processed": processed
    }

@app.get("/api/audio_digests")
def get_audio_digests():
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audio_digests ORDER BY created_at DESC LIMIT 10")
        rows = cursor.fetchall()
    return {"digests": [dict(r) for r in rows]}

@app.get("/api/audio/play/{filename}")
def play_audio(filename: str):
    file_path = AUDIO_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Audio file not found")
    return FileResponse(file_path, media_type="audio/wav")

@app.get("/api/export/{kind}")
def export_file(kind: str, course_id: Optional[str] = None):
    from repetition.anki_exporter import AnkiAndMarkdownExporter
    exp = AnkiAndMarkdownExporter(db=db)
    if kind == "anki":
        p = exp.export_anki_tsv(course_id)
        return FileResponse(p, filename=p.name, media_type="text/plain")
    elif kind == "markdown":
        p = exp.export_markdown_notes(course_id)
        return FileResponse(p, filename=p.name, media_type="text/markdown")
    raise HTTPException(status_code=400, detail="Invalid export kind")

# Serve frontend static assets
if STATIC_DIR.exists():
    app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")

def run():
    uvicorn.run("web.server:app", host=WEB_HOST, port=WEB_PORT, reload=False)

if __name__ == "__main__":
    run()
