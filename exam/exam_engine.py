import json
import random
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Optional
from db.database import Database

class ExamEngine:
    """Manages exam countdowns, adjusts study intensity, and runs timed mock exams."""

    def __init__(self, db: Database = None):
        self.db = db or Database()

    def add_exam(self, course_id: str, exam_title: str, exam_date_str: str, target_score: int = 85, notes: str = "") -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO exams (course_id, exam_title, exam_date, target_score, notes)
                VALUES (?, ?, ?, ?, ?)
            """, (course_id, exam_title, exam_date_str, target_score, notes))
            conn.commit()
            return cursor.lastrowid

    def get_upcoming_exams(self) -> List[Dict[str, Any]]:
        today_str = date.today().isoformat()
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM exams WHERE exam_date >= ? ORDER BY exam_date ASC", (today_str,))
            rows = cursor.fetchall()

        results = []
        for r in rows:
            exam_dt = datetime.strptime(r["exam_date"], "%Y-%m-%d").date()
            days_left = (exam_dt - date.today()).days

            # Study phase determination
            if days_left <= 3:
                phase = "EMERGENCY_REVISION"
                ratio_desc = "100% Mock exams & weak-spot drills"
            elif days_left <= 7:
                phase = "HIGH_YIELD_CRAM"
                ratio_desc = "75% High-yield revision, 25% new material"
            elif days_left <= 14:
                phase = "CONSOLIDATION"
                ratio_desc = "50% Revision, 50% regular lectures"
            else:
                phase = "NORMAL_INGESTION"
                ratio_desc = "Normal paced daily ingestion"

            results.append({
                "id": r["id"],
                "course_id": r["course_id"],
                "exam_title": r["exam_title"],
                "exam_date": r["exam_date"],
                "days_left": days_left,
                "target_score": r["target_score"],
                "phase": phase,
                "strategy": ratio_desc
            })
        return results

    def generate_mock_exam(self, course_id: str, question_count: int = 20, time_limit_minutes: int = 30) -> Dict[str, Any]:
        """Generates a timed mock exam from existing MCQs and high-yield questions."""
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM mcqs WHERE course_id = ? ORDER BY RANDOM() LIMIT ?
            """, (course_id, question_count))
            rows = cursor.fetchall()

        questions = []
        for r in rows:
            q = dict(r)
            if isinstance(q.get("options"), str):
                q["options"] = json.loads(q["options"])
            questions.append(q)

        return {
            "course_id": course_id,
            "title": f"Timed Mock Exam: {course_id}",
            "question_count": len(questions),
            "time_limit_minutes": time_limit_minutes,
            "questions": questions
        }

    def check_deadlines_due_soon(self) -> List[Dict[str, Any]]:
        """Identifies deadlines due in 3 days or 1 day."""
        today = datetime.now()
        in_3_days = today + timedelta(days=3)

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM deadlines ORDER BY due_date ASC")
            rows = cursor.fetchall()

        alerts = []
        for r in rows:
            try:
                # Accept various ISO formats
                due_dt = datetime.fromisoformat(r["due_date"].replace("Z", "+00:00"))
                # strip tz for simple comparison
                due_dt = due_dt.replace(tzinfo=None)
                diff = due_dt - today

                if timedelta(days=0) <= diff <= timedelta(days=3):
                    hours_left = int(diff.total_seconds() // 3600)
                    urgency = "CRITICAL (<= 24h)" if hours_left <= 24 else "WARNING (<= 72h)"
                    alerts.append({
                        "id": r["id"],
                        "course_id": r["course_id"],
                        "title": r["title"],
                        "due_date": r["due_date"],
                        "hours_left": hours_left,
                        "urgency": urgency
                    })
            except Exception:
                continue

        return alerts
