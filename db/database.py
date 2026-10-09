import sqlite3
import json
import hashlib
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import DB_PATH

class Database:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self._init_tables()

    def get_connection(self):
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executescript("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT NOT NULL,
                file_path TEXT UNIQUE NOT NULL,
                file_name TEXT NOT NULL,
                file_hash TEXT NOT NULL,
                file_size INTEGER DEFAULT 0,
                week_num INTEGER DEFAULT 1,
                lecture_title TEXT,
                last_modified TIMESTAMP,
                status TEXT DEFAULT 'pending',
                processed_at TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER,
                course_id TEXT NOT NULL,
                lecture_title TEXT NOT NULL,
                summary TEXT NOT NULL,
                key_terms TEXT, -- JSON array
                short_answers TEXT, -- JSON array
                raw_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (file_id) REFERENCES files(id)
            );

            CREATE TABLE IF NOT EXISTS mcqs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                material_id INTEGER,
                course_id TEXT NOT NULL,
                topic TEXT NOT NULL,
                question TEXT NOT NULL,
                options TEXT NOT NULL, -- JSON array of strings
                answer_idx INTEGER NOT NULL,
                explanation TEXT NOT NULL,
                source TEXT NOT NULL,
                generated_by TEXT DEFAULT 'ai', -- 'ai' or 'heuristic'
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (material_id) REFERENCES materials(id)
            );

            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                material_id INTEGER,
                course_id TEXT NOT NULL,
                topic TEXT NOT NULL,
                front TEXT NOT NULL,
                back TEXT NOT NULL,
                repetition_count INTEGER DEFAULT 0,
                interval_days INTEGER DEFAULT 1,
                ease_factor REAL DEFAULT 2.5,
                next_review_date TEXT, -- YYYY-MM-DD
                generated_by TEXT DEFAULT 'ai', -- 'ai' or 'heuristic'
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (material_id) REFERENCES materials(id)
            );

            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mcq_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                topic TEXT NOT NULL,
                user_answer INTEGER NOT NULL,
                is_correct INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (mcq_id) REFERENCES mcqs(id)
            );

            CREATE TABLE IF NOT EXISTS exams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT NOT NULL,
                exam_title TEXT NOT NULL,
                exam_date TEXT NOT NULL, -- YYYY-MM-DD
                target_score INTEGER DEFAULT 85,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS deadlines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT NOT NULL,
                title TEXT NOT NULL,
                due_date TEXT NOT NULL, -- YYYY-MM-DD HH:MM
                source TEXT DEFAULT 'LMS',
                notified INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS audio_digests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT NOT NULL,
                title TEXT NOT NULL,
                audio_path TEXT,
                script_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT UNIQUE NOT NULL,
                course_name TEXT NOT NULL,
                moodle_id INTEGER,
                enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            conn.commit()

        # Migrate existing databases: add generated_by column if missing
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for table in ("mcqs", "flashcards"):
                try:
                    cursor.execute(f"ALTER TABLE {table} ADD COLUMN generated_by TEXT DEFAULT 'ai'")
                    conn.commit()
                except Exception:
                    pass  # Column already exists

    @staticmethod
    def compute_sha256(filepath: Path) -> str:
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for block in iter(lambda: f.read(65536), b""):
                sha256.update(block)
        return sha256.hexdigest()

    def record_file(self, course_id: str, file_path: Path, week_num: int = 1, lecture_title: str = "") -> Dict[str, Any]:
        """Record or update a file. Returns dict with 'status': 'new' | 'modified' | 'unmodified'"""
        file_hash = self.compute_sha256(file_path)
        stat = file_path.stat()
        file_size = stat.st_size
        mtime = datetime.fromtimestamp(stat.st_mtime).isoformat()
        file_name = file_path.name
        abs_path = str(file_path.resolve())

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, file_hash, status FROM files WHERE file_path = ?", (abs_path,))
            row = cursor.fetchone()

            if row is None:
                cursor.execute("""
                    INSERT INTO files (course_id, file_path, file_name, file_hash, file_size, week_num, lecture_title, last_modified, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending')
                """, (course_id, abs_path, file_name, file_hash, file_size, week_num, lecture_title or file_name, mtime))
                conn.commit()
                return {"id": cursor.lastrowid, "change": "new", "hash": file_hash}
            else:
                if row["file_hash"] != file_hash:
                    cursor.execute("""
                        UPDATE files SET file_hash = ?, file_size = ?, last_modified = ?, status = 'pending'
                        WHERE id = ?
                    """, (file_hash, file_size, mtime, row["id"]))
                    conn.commit()
                    return {"id": row["id"], "change": "modified", "hash": file_hash}
                else:
                    return {"id": row["id"], "change": "unmodified", "status": row["status"]}

    def get_pending_files(self) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM files WHERE status = 'pending' ORDER BY id ASC")
            return [dict(r) for r in cursor.fetchall()]

    def mark_file_processed(self, file_id: int):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE files SET status = 'processed', processed_at = ? WHERE id = ?", 
                           (datetime.now().isoformat(), file_id))
            conn.commit()

    def save_material(self, file_id: int, course_id: str, lecture_title: str,
                      summary: str, key_terms: List[Dict], mcqs: List[Dict],
                      flashcards: List[Dict], short_answers: List[Dict], raw_json: str) -> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO materials (file_id, course_id, lecture_title, summary, key_terms, short_answers, raw_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (file_id, course_id, lecture_title, summary, json.dumps(key_terms), json.dumps(short_answers), raw_json))
            material_id = cursor.lastrowid

            for q in mcqs:
                cursor.execute("""
                    INSERT INTO mcqs (material_id, course_id, topic, question, options, answer_idx, explanation, source, generated_by)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (material_id, course_id, q.get("topic", "General"), q.get("q", ""),
                      json.dumps(q.get("options", [])), q.get("answer", 0),
                      q.get("explanation", ""), q.get("source", "Lecture Notes"),
                      q.get("generated_by", "ai")))

            today_str = date.today().isoformat()
            for fc in flashcards:
                cursor.execute("""
                    INSERT INTO flashcards (material_id, course_id, topic, front, back, next_review_date, generated_by)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (material_id, course_id, fc.get("topic", "General"), fc.get("front", ""), fc.get("back", ""), today_str,
                      fc.get("generated_by", "ai")))

            conn.commit()
            return material_id

    def save_mcqs(self, mcqs: List[Dict], course_id: str, material_id: Optional[int] = None) -> List[int]:
        """Saves a batch of generated MCQs and returns their inserted IDs."""
        inserted_ids = []
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for q in mcqs:
                cursor.execute("""
                    INSERT INTO mcqs (material_id, course_id, topic, question, options, answer_idx, explanation, source, generated_by)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (material_id, course_id, q.get("topic", "General"), q.get("q", ""),
                      json.dumps(q.get("options", [])), q.get("answer", 0),
                      q.get("explanation", ""), q.get("source", "Course Slides"),
                      q.get("generated_by", "ai")))
                inserted_ids.append(cursor.lastrowid)
            conn.commit()
        return inserted_ids

    def log_quiz_attempt(self, mcq_id: int, user_answer: int) -> Dict[str, Any]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT course_id, topic, answer_idx, explanation, source FROM mcqs WHERE id = ?", (mcq_id,))
            mcq = cursor.fetchone()
            if not mcq:
                return {"error": "Question not found"}

            is_correct = 1 if user_answer == mcq["answer_idx"] else 0
            cursor.execute("""
                INSERT INTO quiz_attempts (mcq_id, course_id, topic, user_answer, is_correct)
                VALUES (?, ?, ?, ?, ?)
            """, (mcq_id, mcq["course_id"], mcq["topic"], user_answer, is_correct))
            conn.commit()

            return {
                "is_correct": bool(is_correct),
                "correct_answer": mcq["answer_idx"],
                "explanation": mcq["explanation"],
                "source": mcq["source"],
                "topic": mcq["topic"]
            }

    def get_weak_topics(self, course_id: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = """
                SELECT topic, course_id,
                       COUNT(*) as total_attempts,
                       SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as correct_count,
                       ROUND(100.0 * SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) / COUNT(*), 1) as accuracy
                FROM quiz_attempts
            """
            params = []
            if course_id:
                query += " WHERE course_id = ? "
                params.append(course_id)
            query += " GROUP BY topic, course_id HAVING total_attempts >= 1 ORDER BY accuracy ASC, total_attempts DESC LIMIT ?"
            params.append(limit)
            cursor.execute(query, params)
            return [dict(r) for r in cursor.fetchall()]

    def get_due_flashcards(self, course_id: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
        today_str = date.today().isoformat()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM flashcards WHERE (next_review_date <= ? OR next_review_date IS NULL)"
            params = [today_str]
            if course_id:
                query += " AND course_id = ?"
                params.append(course_id)
            query += " ORDER BY interval_days ASC LIMIT ?"
            params.append(limit)
            cursor.execute(query, params)
            return [dict(r) for r in cursor.fetchall()]

    def get_all_flashcards(self, course_id: Optional[str] = None, limit: int = 200) -> List[Dict[str, Any]]:
        """Returns ALL flashcards (not just due ones) for revision sessions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM flashcards"
            params = []
            if course_id:
                query += " WHERE course_id = ?"
                params.append(course_id)
            query += " ORDER BY RANDOM() LIMIT ?"
            params.append(limit)
            cursor.execute(query, params)
            return [dict(r) for r in cursor.fetchall()]

    def delete_heuristic_mcqs(self, course_id: Optional[str] = None) -> int:
        """Deletes all template/heuristic-generated MCQs (low quality). Returns count deleted."""
        pattern_condition = (
            "(generated_by = 'heuristic' OR "
            "options LIKE '%deprecated secondary mechanism%' OR "
            "question LIKE '%what is the primary role or definition associated with%' OR "
            "options LIKE '%computational overhead%' OR "
            "options LIKE '%unconstrained, static environments%')"
        )
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if course_id:
                cursor.execute(f"DELETE FROM quiz_attempts WHERE mcq_id IN (SELECT id FROM mcqs WHERE {pattern_condition} AND course_id = ?)", (course_id,))
                cursor.execute(f"DELETE FROM mcqs WHERE {pattern_condition} AND course_id = ?", (course_id,))
            else:
                cursor.execute(f"DELETE FROM quiz_attempts WHERE mcq_id IN (SELECT id FROM mcqs WHERE {pattern_condition})")
                cursor.execute(f"DELETE FROM mcqs WHERE {pattern_condition}")
            deleted = cursor.rowcount
            conn.commit()
            return deleted

    def delete_heuristic_flashcards(self, course_id: Optional[str] = None) -> int:
        """Deletes all template/heuristic-generated flashcards (low quality). Returns count deleted."""
        pattern_condition = (
            "(generated_by = 'heuristic' OR "
            "front LIKE 'Explain the principle of %')"
        )
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if course_id:
                cursor.execute(f"DELETE FROM flashcards WHERE {pattern_condition} AND course_id = ?", (course_id,))
            else:
                cursor.execute(f"DELETE FROM flashcards WHERE {pattern_condition}")
            deleted = cursor.rowcount
            conn.commit()
            return deleted

    def update_flashcard_sm2(self, card_id: int, quality: int):
        """Quality 0-5 according to SuperMemo SM-2 algorithm"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT repetition_count, interval_days, ease_factor FROM flashcards WHERE id = ?", (card_id,))
            card = cursor.fetchone()
            if not card:
                return

            rep = card["repetition_count"]
            interval = card["interval_days"]
            ef = card["ease_factor"]

            # SM-2 calculation
            if quality >= 3:
                if rep == 0:
                    interval = 1
                elif rep == 1:
                    interval = 6
                else:
                    interval = int(round(interval * ef))
                rep += 1
            else:
                rep = 0
                interval = 1

            # New Ease Factor formula
            ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
            if ef < 1.3:
                ef = 1.3

            next_date = (date.today() + timedelta(days=interval)).isoformat()
            cursor.execute("""
                UPDATE flashcards SET repetition_count = ?, interval_days = ?, ease_factor = ?, next_review_date = ?
                WHERE id = ?
            """, (rep, interval, ef, next_date, card_id))
            conn.commit()

    def clear_all_previous_data(self):
        """Purges all dummy/previous courses, files, and study materials."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quiz_attempts")
            cursor.execute("DELETE FROM flashcards")
            cursor.execute("DELETE FROM mcqs")
            cursor.execute("DELETE FROM materials")
            cursor.execute("DELETE FROM files")
            cursor.execute("DELETE FROM exams")
            cursor.execute("DELETE FROM deadlines")
            cursor.execute("DELETE FROM audio_digests")
            cursor.execute("DELETE FROM courses")
            conn.commit()

    def register_course(self, course_id: str, course_name: str, moodle_id: Optional[int] = None):
        """Registers an enrolled course."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO courses (course_id, course_name, moodle_id)
                VALUES (?, ?, ?)
                ON CONFLICT(course_id) DO UPDATE SET course_name=excluded.course_name, moodle_id=excluded.moodle_id
            """, (course_id, course_name, moodle_id))
            conn.commit()

    def get_all_courses(self) -> List[str]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT course_id FROM courses UNION SELECT DISTINCT course_id FROM files WHERE course_id IS NOT NULL AND course_id != '' ORDER BY 1 ASC")
            return [r[0] for r in cursor.fetchall()]

    def get_stats_overview(self) -> Dict[str, Any]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM files")
            total_files = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM mcqs")
            total_mcqs = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM flashcards")
            total_flashcards = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*), SUM(is_correct) FROM quiz_attempts")
            attempts_row = cursor.fetchone()
            total_attempts = attempts_row[0] or 0
            correct_attempts = attempts_row[1] or 0
            accuracy = round((correct_attempts / total_attempts * 100), 1) if total_attempts > 0 else 0.0

            cursor.execute("SELECT COUNT(*) FROM exams WHERE exam_date >= ?", (date.today().isoformat(),))
            upcoming_exams = cursor.fetchone()[0]

            return {
                "total_files": total_files,
                "total_mcqs": total_mcqs,
                "total_flashcards": total_flashcards,
                "total_attempts": total_attempts,
                "accuracy": accuracy,
                "upcoming_exams": upcoming_exams
            }
