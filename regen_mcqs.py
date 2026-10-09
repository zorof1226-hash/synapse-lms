"""
Regenerate all MCQs and flashcards using Gemini AI.
This script:
1. Deletes ALL existing MCQs, flashcards, and materials from the database
2. Resets all processed files back to 'pending' status
3. Re-runs the full AI generation pipeline for every lecture file
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from db.database import Database
from pipeline import StudyPipeline

def nuke_and_regenerate():
    db = Database()
    pipeline = StudyPipeline(db=db)

    # Step 1: Count what we have
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM mcqs")
        old_mcqs = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM flashcards")
        old_cards = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM files")
        total_files = cur.fetchone()[0]
        print(f"[Regen] Current DB: {old_mcqs} MCQs, {old_cards} flashcards, {total_files} files")

    # Step 2: Delete bad MCQs, flashcards, materials (keep files + courses + exams + deadlines)
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM quiz_attempts")
        cur.execute("DELETE FROM flashcards")
        cur.execute("DELETE FROM mcqs")
        cur.execute("DELETE FROM materials")
        # Reset all files back to pending
        cur.execute("UPDATE files SET status = 'pending', processed_at = NULL")
        conn.commit()
        print(f"[Regen] Cleared all MCQs, flashcards, materials. Reset {total_files} files to pending.")

    # Step 3: Verify pending count
    pending = db.get_pending_files()
    print(f"[Regen] {len(pending)} lecture files queued for AI generation...")

    if not pending:
        print("[Regen] No pending files found. Nothing to process.")
        return

    # Step 4: Run pipeline (this calls Gemini for each file)
    print("[Regen] Starting AI generation pipeline. This may take a few minutes...\n")
    processed = pipeline.process_pending_files()

    # Step 5: Report results
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM mcqs")
        new_mcqs = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM flashcards")
        new_cards = cur.fetchone()[0]

    print(f"\n{'='*60}")
    print(f"[Regen] DONE! Processed {len(processed)} lecture files.")
    print(f"[Regen] Generated {new_mcqs} AI-powered MCQs")
    print(f"[Regen] Generated {new_cards} AI-powered Flashcards")
    print(f"{'='*60}")

    for p in processed:
        status = "✓" if p['mcq_count'] > 0 else "⚠"
        print(f"  {status} {p['course_id']} | {p['lecture_title'][:50]} → {p['mcq_count']} MCQs, {p['flashcard_count']} cards")

if __name__ == "__main__":
    nuke_and_regenerate()
