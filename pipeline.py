import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import LMS_DOWNLOADS_DIR, TEXTBOOKS_DIR, DAILY_MCQ_COUNT, DAILY_FLASHCARD_COUNT
from db.database import Database
from lms_sync.folder_watcher import FolderWatcher
from lms_sync.moodle_sync import MoodleSync
from lms_sync.canvas_sync import CanvasSync
from extraction.extractor import DocumentExtractor
from extraction.textbook_matcher import TextbookMatcher
from notebooklm.notebooklm_client import NotebookLMClient
from generation.llm_generator import LLMGenerator
from generation.quality_filter import QualityFilter
from repetition.anki_exporter import AnkiAndMarkdownExporter

ADMIN_FILE_PATTERNS = [
    r"course\s*outline",
    r"syllabus",
    r"policy",
    r"guideline",
    r"cover\s*page",
    r"lecture\s*links",
    r"lecture\s*0\b",
    r"course\s*intro",
    r"rubric",
]

def is_administrative_file(filename: str) -> bool:
    name_lower = filename.lower()
    return any(re.search(pat, name_lower) for pat in ADMIN_FILE_PATTERNS)

class StudyPipeline:
    """The central orchestrator connecting LMS ingestion, slide extraction,
    LLM study package generation, spaced repetition, and exports.
    """

    def __init__(self, db: Optional[Database] = None):
        self.db = db or Database()
        self.watcher = FolderWatcher(db=self.db)
        self.moodle = MoodleSync(db=self.db)
        self.canvas = CanvasSync(db=self.db)
        self.extractor = DocumentExtractor()
        self.textbook_matcher = TextbookMatcher()
        self.notebooklm = NotebookLMClient()
        self.generator = LLMGenerator()
        self.filter = QualityFilter()
        self.exporter = AnkiAndMarkdownExporter(db=self.db)

    def run_sync(self, lms_type: str = "folder") -> List[Dict[str, Any]]:
        """Syncs files from selected LMS source into local storage and registers in SQLite."""
        print(f"[Pipeline] Starting file sync via mode: {lms_type}...")
        results = []

        if lms_type == "moodle" and self.moodle.is_configured():
            courses = self.moodle.get_enrolled_courses()
            for c in courses:
                cid = c.get("id")
                code = c.get("fullname") or c.get("shortname") or f"Moodle_{cid}"
                results.extend(self.moodle.sync_course_materials(cid, code))
        elif lms_type == "canvas" and self.canvas.is_configured():
            courses = self.canvas.get_courses()
            for c in courses:
                cid = c.get("id")
                code = c.get("course_code") or f"Canvas_{cid}"
                results.extend(self.canvas.sync_course_files(cid, code))
                self.canvas.sync_assignments(cid, code)
        else:
            # Default folder watcher
            results = self.watcher.scan_for_new_files()

        print(f"[Pipeline] Sync finished. {len(results)} files scanned/updated.")
        return results

    def process_pending_files(self) -> List[Dict[str, Any]]:
        """Processes any files marked as 'pending' in SQLite."""
        pending = self.db.get_pending_files()
        if not pending:
            print("[Pipeline] No pending files to process.")
            return []

        processed_summary = []
        # Pre-load any textbooks in TEXTBOOKS_DIR
        textbook_chapters = []
        for tb_file in TEXTBOOKS_DIR.glob("*.pdf"):
            textbook_chapters.extend(self.textbook_matcher.extract_chapters_from_pdf(tb_file))

        for file_row in pending:
            file_id = file_row["id"]
            file_path = Path(file_row["file_path"])
            course_id = file_row["course_id"]
            lecture_title = file_row["lecture_title"] or file_path.stem

            print(f"\n[Pipeline] ---> Processing: {course_id} | {lecture_title} ({file_path.name})")

            # Check if file is administrative (syllabus, course outline, policy, cover page)
            if is_administrative_file(file_path.name) or is_administrative_file(lecture_title):
                print(f"  [!] Skipping administrative document from MCQ generation: {file_path.name}")
                self.db.mark_file_processed(file_id)
                continue

            # 1. Extraction & Slide Chunking
            chunks = self.extractor.extract_file(file_path, course_id=course_id, lecture_title=lecture_title)
            print(f"  - Extracted {len(chunks)} slide/section chunks.")

            # 2. NotebookLM layer (optional wrapper)
            nb_res = self.notebooklm.sync_lecture_to_notebook(course_id, file_path)
            print(f"  - NotebookLM sync status: {nb_res.get('status')}")

            # 3. LLM Study Package Generation (Strict JSON)
            raw_pkg = self.generator.generate_study_package(chunks, course_id, lecture_title)

            # 4. Quality Filter (Ambiguity, single answer, citations)
            valid_mcqs = self.filter.filter_mcqs(raw_pkg.get("mcqs", []))[:DAILY_MCQ_COUNT]
            valid_flashcards = self.filter.filter_flashcards(raw_pkg.get("flashcards", []))[:DAILY_FLASHCARD_COUNT]
            summary = raw_pkg.get("summary", "")
            key_terms = raw_pkg.get("key_terms", [])
            short_answers = raw_pkg.get("short_answer", [])

            # 5. Textbook Matching (Chapter reading recommendation)
            if textbook_chapters:
                matched_tb = self.textbook_matcher.find_relevant_chapters(" ".join([c.text for c in chunks]), textbook_chapters)
                if matched_tb:
                    rec = matched_tb[0]["reading_recommendation"]
                    summary += f"\n\n📖 **Recommended Textbook Reading**: {rec}"

            # 6. Audio Digest Generation (pyttsx3 / NotebookLM audio overview)
            audio_info = self.notebooklm.generate_audio_digest(course_id, lecture_title, summary, key_terms)
            print(f"  - Audio Digest synthesized: {bool(audio_info.get('audio_path'))}")

            # 7. Store in SQLite
            material_id = self.db.save_material(
                file_id=file_id,
                course_id=course_id,
                lecture_title=lecture_title,
                summary=summary,
                key_terms=key_terms,
                mcqs=valid_mcqs,
                flashcards=valid_flashcards,
                short_answers=short_answers,
                raw_json=str(raw_pkg)
            )

            # 8. Mark file as processed
            self.db.mark_file_processed(file_id)

            # 9. Export latest Anki TSV and Markdown backups
            self.exporter.export_anki_tsv(course_id)
            self.exporter.export_markdown_notes(course_id)

            processed_summary.append({
                "file_id": file_id,
                "course_id": course_id,
                "lecture_title": lecture_title,
                "material_id": material_id,
                "mcq_count": len(valid_mcqs),
                "flashcard_count": len(valid_flashcards),
                "audio_path": audio_info.get("audio_path")
            })

            print(f"  [+] Finished! Generated {len(valid_mcqs)} MCQs, {len(valid_flashcards)} Flashcards.")

        return processed_summary

    def generate_mcqs_for_course(self, course_id: str = "all", count: int = 10, topic: Optional[str] = None) -> List[Dict[str, Any]]:
        """Extracts text from course lectures/slides and uses AI to generate `count` MCQs."""
        chunks = []
        target_course = course_id if (course_id and course_id != "all") else "General"

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            if course_id and course_id != "all":
                cursor.execute("SELECT id, course_id, file_path, lecture_title FROM files WHERE course_id = ? ORDER BY RANDOM() LIMIT 6", (course_id,))
            else:
                cursor.execute("SELECT id, course_id, file_path, lecture_title FROM files ORDER BY RANDOM() LIMIT 6")
            files = cursor.fetchall()

        for f in files:
            lt = f["lecture_title"] or ""
            fp_name = Path(f["file_path"]).name
            if is_administrative_file(lt) or is_administrative_file(fp_name):
                continue
            fpath = Path(f["file_path"])
            if fpath.exists():
                file_chunks = self.extractor.extract_file(fpath, course_id=f["course_id"], lecture_title=f["lecture_title"])
                chunks.extend(file_chunks)
                if target_course == "General":
                    target_course = f["course_id"]

        if not chunks:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                if course_id and course_id != "all":
                    cursor.execute("SELECT summary, key_terms FROM materials WHERE course_id = ? LIMIT 5", (course_id,))
                else:
                    cursor.execute("SELECT summary, key_terms FROM materials LIMIT 5")
                mats = cursor.fetchall()
                text_parts = [m["summary"] for m in mats if m["summary"]]
                chunks_text = "\n\n".join(text_parts)
        else:
            chunks_text = "\n\n".join([f"--- [{c.source_tag}] {c.heading} ---\n{c.text}" for c in chunks[:15]])

        if not chunks_text:
            return []

        # Generate via LLM, with a local heuristic fallback if Gemini/OpenAI fail.
        raw_mcqs = self.generator.generate_focused_mcqs(chunks_text, course_id=target_course, count=count)
        if raw_mcqs:
            valid_mcqs = self.filter.filter_mcqs(raw_mcqs)[:count]
        else:
            heuristic_pkg = self.generator._generate_heuristic(
                chunks[:12] if chunks else [],
                target_course,
                target_course if target_course and target_course != "General" else "Lecture Notes",
            )
            valid_mcqs = self.filter.filter_mcqs(heuristic_pkg.get("mcqs", []))[:count]

        # Save to DB
        if valid_mcqs:
            self.db.save_mcqs(valid_mcqs, course_id=target_course)

        return valid_mcqs
