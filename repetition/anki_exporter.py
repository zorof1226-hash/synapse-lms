import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import EXPORTS_DIR
from db.database import Database

class AnkiAndMarkdownExporter:
    """Exports flashcards and study notes to Anki-compatible TSV, AnkiConnect,
    and formatted Markdown for Obsidian / Notion.
    """

    def __init__(self, export_dir: Path = EXPORTS_DIR, db: Database = None):
        self.export_dir = export_dir
        self.db = db or Database()

    def export_anki_tsv(self, course_id: Optional[str] = None) -> Path:
        """Generates tab-separated text file importable directly into Anki.
        Columns: Front \t Back \t Topic/Tag
        """
        out_file = self.export_dir / f"anki_{course_id or 'all_courses'}.txt"
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT front, back, topic, course_id FROM flashcards"
            params = []
            if course_id:
                query += " WHERE course_id = ?"
                params.append(course_id)
            cursor.execute(query, params)
            cards = cursor.fetchall()

        with open(out_file, "w", encoding="utf-8") as f:
            for card in cards:
                front = card["front"].replace("\t", " ").replace("\n", "<br>")
                back = card["back"].replace("\t", " ").replace("\n", "<br>")
                tag = f"{card['course_id']}::{card['topic'].replace(' ', '_')}"
                f.write(f"{front}\t{back}\t{tag}\n")

        return out_file

    def export_markdown_notes(self, course_id: Optional[str] = None) -> Path:
        """Exports clean Obsidian/Notion markdown files with summaries, key terms, and questions."""
        out_file = self.export_dir / f"study_notes_{course_id or 'all_courses'}.md"
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM materials"
            params = []
            if course_id:
                query += " WHERE course_id = ?"
                params.append(course_id)
            cursor.execute(query, params)
            materials = cursor.fetchall()

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"# 📚 Study Knowledge Base: {course_id or 'All Courses'}\n\n")
            f.write(f"*Auto-generated from LMS lecture notes. Compatible with Obsidian & Notion.*\n\n---\n\n")

            for mat in materials:
                f.write(f"## {mat['course_id']} - {mat['lecture_title']}\n\n")
                f.write(f"### 📝 Executive Summary\n{mat['summary']}\n\n")

                # Key terms
                if mat['key_terms']:
                    f.write("### 🔑 Key Definitions\n")
                    terms = json.loads(mat['key_terms'])
                    for t in terms:
                        f.write(f"- **{t.get('term')}**: {t.get('definition')}\n")
                    f.write("\n")

                # Short answers
                if mat['short_answers']:
                    f.write("### 💡 Core Conceptual Questions\n")
                    sqs = json.loads(mat['short_answers'])
                    for sq in sqs:
                        f.write(f"> **Q: {sq.get('q')}**\n>\n> *A:* {sq.get('model_answer')}\n\n")

                f.write("---\n\n")

        return out_file
