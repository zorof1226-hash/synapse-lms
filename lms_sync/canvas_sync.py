import os
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import CANVAS_URL, CANVAS_TOKEN, LMS_DOWNLOADS_DIR
from db.database import Database

class CanvasSync:
    """Canvas LMS REST API Client.
    Uses /api/v1/courses, /modules, /files, and /assignments.
    """

    def __init__(self, base_url: str = CANVAS_URL, token: str = CANVAS_TOKEN,
                 download_dir: Path = LMS_DOWNLOADS_DIR, db: Database = None):
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.token = token
        self.download_dir = download_dir
        self.db = db or Database()

    def is_configured(self) -> bool:
        return bool(self.base_url and self.token)

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

    def get_courses(self) -> List[Dict[str, Any]]:
        if not self.is_configured():
            return []
        try:
            url = f"{self.base_url}/api/v1/courses?enrollment_state=active"
            res = requests.get(url, headers=self._headers(), timeout=30)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"[CanvasSync] Error getting courses: {e}")
            return []

    def sync_course_files(self, course_id: int, course_code: str) -> List[Dict[str, Any]]:
        """Download slide files and store in local course directory."""
        downloaded = []
        try:
            url = f"{self.base_url}/api/v1/courses/{course_id}/files"
            res = requests.get(url, headers=self._headers(), timeout=30)
            res.raise_for_status()
            files = res.json()

            for item in files:
                display_name = item.get("display_name", "")
                download_url = item.get("url")
                ext = Path(display_name).suffix.lower()

                if ext in (".pdf", ".pptx", ".ppt", ".txt") and download_url:
                    target_dir = self.download_dir / course_code / "Modules"
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target_file = target_dir / display_name

                    r = requests.get(download_url, headers=self._headers(), stream=True, timeout=60)
                    if r.status_code == 200:
                        with open(target_file, "wb") as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                f.write(chunk)

                        change_info = self.db.record_file(
                            course_id=course_code,
                            file_path=target_file,
                            week_num=1,
                            lecture_title=display_name
                        )
                        downloaded.append({
                            "course_id": course_code,
                            "file_name": display_name,
                            "change": change_info["change"]
                        })
        except Exception as e:
            print(f"[CanvasSync] Error syncing course files: {e}")

        return downloaded

    def sync_assignments(self, course_id: int, course_code: str) -> List[Dict[str, Any]]:
        """Fetch assignment due dates to populate the deadline watcher."""
        deadlines = []
        try:
            url = f"{self.base_url}/api/v1/courses/{course_id}/assignments"
            res = requests.get(url, headers=self._headers(), timeout=30)
            res.raise_for_status()
            assignments = res.json()

            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                for assign in assignments:
                    due_at = assign.get("due_at")
                    name = assign.get("name")
                    if due_at and name:
                        cursor.execute("""
                            INSERT INTO deadlines (course_id, title, due_date, source)
                            VALUES (?, ?, ?, 'Canvas')
                        """, (course_code, name, due_at))
                        deadlines.append({"course_id": course_code, "title": name, "due_date": due_at})
                conn.commit()
        except Exception as e:
            print(f"[CanvasSync] Error syncing assignments: {e}")

        return deadlines
