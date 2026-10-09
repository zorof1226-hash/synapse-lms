import os
import re
from pathlib import Path
from typing import List, Dict, Any
from config import LMS_DOWNLOADS_DIR
from db.database import Database

class FolderWatcher:
    """Scans and monitors local course folder tree.
    Expected structure:
      data/lms_downloads/
        ├── CS101/
        │   ├── Week_01/
        │   │   └── Lec1_Introduction.pdf
        │   └── Week_02/
        │       └── Lec2_DataStructures.pptx
        └── MATH201/
            └── Week_01/
                └── Calculus_Limits.pdf
    """

    def __init__(self, watch_dir: Path = LMS_DOWNLOADS_DIR, db: Database = None):
        self.watch_dir = watch_dir
        self.db = db or Database()

    def parse_path_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract course_id, week_num, lecture_title from folder structure and filename."""
        rel_parts = file_path.relative_to(self.watch_dir).parts
        course_id = "General"
        week_num = 1
        lecture_title = file_path.stem

        if len(rel_parts) >= 2:
            course_id = rel_parts[0]
        
        # Check for week pattern in path parts
        for part in rel_parts:
            match = re.search(r"week[_\-\s]*(\d+)", part, re.IGNORECASE)
            if match:
                week_num = int(match.group(1))

        # Check for lecture number in filename
        clean_title = re.sub(r"^[0-9]+[_\-\s]*", "", file_path.stem).replace("_", " ")
        if clean_title:
            lecture_title = clean_title

        return {
            "course_id": course_id,
            "week_num": week_num,
            "lecture_title": lecture_title
        }

    def scan_for_new_files(self) -> List[Dict[str, Any]]:
        """Scans folder tree and records new/modified files in SQLite."""
        supported_extensions = {".pdf", ".pptx", ".ppt", ".txt", ".md"}
        results = []

        if not self.watch_dir.exists():
            self.watch_dir.mkdir(parents=True, exist_ok=True)

        for root, _, files in os.walk(self.watch_dir):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in supported_extensions:
                    meta = self.parse_path_metadata(file_path)
                    res = self.db.record_file(
                        course_id=meta["course_id"],
                        file_path=file_path,
                        week_num=meta["week_num"],
                        lecture_title=meta["lecture_title"]
                    )
                    results.append({
                        "file_path": str(file_path),
                        "file_name": file_path.name,
                        "course_id": meta["course_id"],
                        "change": res["change"],
                        "file_id": res["id"]
                    })
        return results
