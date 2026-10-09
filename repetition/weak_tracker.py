import random
import json
from typing import List, Dict, Any, Optional
from db.database import Database

class WeakTopicTracker:
    """Tracks error rates per topic and builds targeted diagnostic quizzes."""

    def __init__(self, db: Database = None):
        self.db = db or Database()

    def get_topic_analytics(self, course_id: Optional[str] = None) -> List[Dict[str, Any]]:
        return self.db.get_weak_topics(course_id=course_id, limit=20)

    def generate_weekend_quiz(self, course_id: Optional[str] = None, total_questions: int = 15) -> List[Dict[str, Any]]:
        """Builds a weekend quiz mixed from recent lectures, weighted toward weak topics."""
        with self.db.get_connection() as conn:
            cursor = conn.cursor()

            # 1. Identify weak topics (accuracy < 70%)
            weak_topics_data = self.db.get_weak_topics(course_id=course_id, limit=10)
            weak_topic_names = [item["topic"] for item in weak_topics_data if item["accuracy"] < 70.0]

            # 2. Fetch questions for weak topics
            weak_pool = []
            if weak_topic_names:
                placeholders = ",".join(["?"] * len(weak_topic_names))
                query = f"SELECT * FROM mcqs WHERE topic IN ({placeholders})"
                params = list(weak_topic_names)
                if course_id:
                    query += " AND course_id = ?"
                    params.append(course_id)
                cursor.execute(query, params)
                weak_pool = [dict(r) for r in cursor.fetchall()]

            # 3. Fetch general question pool
            gen_query = "SELECT * FROM mcqs"
            gen_params = []
            if course_id:
                gen_query += " WHERE course_id = ?"
                gen_params.append(course_id)
            gen_query += " ORDER BY RANDOM() LIMIT 50"
            cursor.execute(gen_query, gen_params)
            general_pool = [dict(r) for r in cursor.fetchall()]

            # 4. Mix pools: 60% weak topics, 40% general review
            num_weak = min(len(weak_pool), int(total_questions * 0.6))
            num_gen = total_questions - num_weak

            selected = []
            if weak_pool:
                selected.extend(random.sample(weak_pool, num_weak))

            # Remove already chosen from general pool
            chosen_ids = {q["id"] for q in selected}
            available_gen = [q for q in general_pool if q["id"] not in chosen_ids]

            if available_gen:
                selected.extend(random.sample(available_gen, min(num_gen, len(available_gen))))

            # If still short, backfill
            if len(selected) < total_questions:
                all_ids = {q["id"] for q in selected}
                cursor.execute("SELECT * FROM mcqs ORDER BY RANDOM() LIMIT ?", (total_questions,))
                for r in cursor.fetchall():
                    if r["id"] not in all_ids:
                        selected.append(dict(r))
                        if len(selected) >= total_questions:
                            break

            random.shuffle(selected)
            for item in selected:
                if isinstance(item.get("options"), str):
                    item["options"] = json.loads(item["options"])

            return selected
