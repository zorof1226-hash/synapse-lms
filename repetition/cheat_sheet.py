import json
from pathlib import Path
from typing import Optional, Dict, Any
from config import EXPORTS_DIR
from db.database import Database

class CheatSheetGenerator:
    """Generates a high-density, one-page formula and definition cheat-sheet
    per course, auto-updated from all ingested lectures.
    """

    def __init__(self, export_dir: Path = EXPORTS_DIR, db: Database = None):
        self.export_dir = export_dir
        self.db = db or Database()

    def generate_sheet(self, course_id: str) -> Dict[str, Any]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            # Fetch all materials for this course
            cursor.execute("SELECT lecture_title, key_terms, short_answers FROM materials WHERE course_id = ?", (course_id,))
            rows = cursor.fetchall()

        all_terms = {}
        formulas_or_rules = []

        for row in rows:
            if row["key_terms"]:
                terms = json.loads(row["key_terms"])
                for t in terms:
                    all_terms[t.get("term")] = t.get("definition")

            if row["short_answers"]:
                sqs = json.loads(row["short_answers"])
                for s in sqs:
                    q = s.get("q", "")
                    ans = s.get("model_answer", "")
                    if any(k in q.lower() for k in ["rule", "formula", "complexity", "principle", "algorithm", "property"]):
                        formulas_or_rules.append({"q": q, "ans": ans})

        # Generate markdown format
        out_file = self.export_dir / f"cheatsheet_{course_id}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"# 📌 {course_id} Executive Formula & Concept Cheat-Sheet\n\n")
            f.write(f"*Auto-generated high-yield review matrix for quick exam cramming.*\n\n")
            f.write("## 🔑 Essential Definitions & Vocabulary\n\n")
            f.write("| Term | Core Definition |\n")
            f.write("| :--- | :--- |\n")
            for term, defn in sorted(all_terms.items())[:35]:
                clean_defn = defn.replace("|", "/").replace("\n", " ")
                f.write(f"| **{term}** | {clean_defn} |\n")

            if formulas_or_rules:
                f.write("\n## ⚡ Core Rules, Theorems & Key Mechanics\n\n")
                for item in formulas_or_rules[:15]:
                    f.write(f"- **{item['q']}**\n  > {item['ans']}\n\n")

        return {
            "course_id": course_id,
            "file_path": str(out_file),
            "term_count": len(all_terms),
            "rule_count": len(formulas_or_rules)
        }
