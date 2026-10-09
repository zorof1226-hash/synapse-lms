"""Quick test: Generate MCQs for ONE lecture file using Gemini 2.5 Flash"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from db.database import Database
from generation.llm_generator import LLMGenerator
from extraction.extractor import DocumentExtractor

db = Database()
gen = LLMGenerator()
ext = DocumentExtractor()

# Get one pending file
pending = db.get_pending_files()
if not pending:
    # Reset one file to pending
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, file_path, course_id, lecture_title FROM files LIMIT 1")
        row = dict(cur.fetchone())
        cur.execute("UPDATE files SET status='pending' WHERE id=?", (row["id"],))
        conn.commit()
    pending = [row]

f = pending[0]
print(f"Testing with: {f['course_id']} | {f['lecture_title']}")
fp = Path(f["file_path"])
if not fp.exists():
    print(f"File not found: {fp}")
    sys.exit(1)

chunks = ext.extract_file(fp, course_id=f["course_id"], lecture_title=f["lecture_title"])
print(f"Extracted {len(chunks)} chunks")

print("Calling Gemini 2.5 Flash...")
result = gen._call_gemini(
    "\n\n".join([f"--- [{c.source_tag}] {c.heading} ---\n{c.text}" for c in chunks]),
    f["lecture_title"]
)
print(f"SUCCESS! Got {len(result.get('mcqs', []))} MCQs, {len(result.get('flashcards', []))} flashcards")
print("\nSample MCQ:")
if result.get("mcqs"):
    q = result["mcqs"][0]
    print(f"  Q: {q['q']}")
    for i, opt in enumerate(q['options']):
        mark = " [CORRECT]" if i == q['answer'] else ""
        print(f"  {chr(65+i)}. {opt}{mark}")
    print(f"  Explanation: {q['explanation'][:150]}")
