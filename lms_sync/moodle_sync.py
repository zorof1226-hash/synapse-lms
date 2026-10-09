import os
import re
import json
import requests
import urllib3
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import MOODLE_URL, MOODLE_TOKEN, MOODLE_SESSION_COOKIE, MOODLE_VERIFY_SSL, LMS_DOWNLOADS_DIR
from db.database import Database

if not MOODLE_VERIFY_SSL:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class MoodleSync:
    """Moodle Client tailored for university portals like NUST (lms.nust.edu.pk).
    Uses both Moodle Web Services API and authenticated Session Scraping to ensure 100%
    of lecture slides and course documents are discovered and downloaded.
    """

    def __init__(self, base_url: str = MOODLE_URL, token: str = MOODLE_TOKEN,
                 session_cookie: str = MOODLE_SESSION_COOKIE,
                 verify_ssl: bool = MOODLE_VERIFY_SSL,
                 download_dir: Path = LMS_DOWNLOADS_DIR, db: Database = None):
        self.base_url = base_url.rstrip("/") if base_url else "https://lms.nust.edu.pk"
        self.token = token
        self.session_cookie = session_cookie
        self.verify_ssl = verify_ssl
        self.download_dir = download_dir
        self.db = db or Database()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

        if self.session_cookie:
            self.session.cookies.set("MoodleSession", self.session_cookie, domain="lms.nust.edu.pk")

    def is_configured(self) -> bool:
        return bool(self.base_url and (self.token or self.session_cookie))

    def login_with_credentials(self, username: str, password: str, service: str = "moodle_mobile_app") -> Dict[str, Any]:
        """Dual-authentication:
        1. Obtains Web Services token via /login/token.php
        2. Establishes browser session via /login/index.php
        """
        token_endpoint = f"{self.base_url}/login/token.php"
        params = {
            "username": username,
            "password": password,
            "service": service
        }

        # 1. Web Service Token
        token_success = False
        try:
            resp = requests.post(token_endpoint, data=params, verify=self.verify_ssl, timeout=20)
            data = self._clean_json(resp.text)
            if "token" in data:
                self.token = data["token"]
                token_success = True
                self._save_token_to_env(self.token)
        except Exception as e:
            print(f"[MoodleSync] Token endpoint exception: {e}")

        # 2. Web Session Login
        session_success = False
        try:
            login_page = self.session.get(f"{self.base_url}/login/index.php", verify=self.verify_ssl, timeout=15)
            match = re.search(r'name=["\']logintoken["\'] value=["\']([^"\']+)["\']', login_page.text)
            logintoken = match.group(1) if match else ""

            login_payload = {
                "username": username,
                "password": password,
                "logintoken": logintoken
            }
            post_login = self.session.post(f"{self.base_url}/login/index.php", data=login_payload, verify=self.verify_ssl, timeout=20)
            if "login/index.php" not in post_login.url or "my/" in post_login.url:
                session_success = True
                moodle_cookie = self.session.cookies.get("MoodleSession")
                if moodle_cookie:
                    self.session_cookie = moodle_cookie
                    self._save_session_to_env(moodle_cookie)
        except Exception as e:
            print(f"[MoodleSync] Web session login exception: {e}")

        if token_success or session_success:
            return {"success": True, "token": self.token, "session_active": session_success}
        else:
            return {"success": False, "error": "Invalid LMS credentials or connection failed."}

    def _save_token_to_env(self, token: str):
        env_file = Path(__file__).resolve().parent.parent / ".env"
        if env_file.exists():
            content = env_file.read_text(encoding="utf-8")
            if "MOODLE_TOKEN=" in content:
                content = re.sub(r"MOODLE_TOKEN=.*", f"MOODLE_TOKEN={token}", content)
            else:
                content += f"\nMOODLE_TOKEN={token}\n"
            env_file.write_text(content, encoding="utf-8")

    def _save_session_to_env(self, session_cookie: str):
        env_file = Path(__file__).resolve().parent.parent / ".env"
        if env_file.exists():
            content = env_file.read_text(encoding="utf-8")
            if "MOODLE_SESSION_COOKIE=" in content:
                content = re.sub(r"MOODLE_SESSION_COOKIE=.*", f"MOODLE_SESSION_COOKIE={session_cookie}", content)
            else:
                content += f"\nMOODLE_SESSION_COOKIE={session_cookie}\n"
            env_file.write_text(content, encoding="utf-8")

    @staticmethod
    def _clean_json(text: str) -> Any:
        clean = text.strip()
        try:
            return json.loads(clean)
        except Exception:
            # Extract JSON array or object substring (bypasses PHP notices like <br /><b>Deprecated</b>)
            match = re.search(r"(\[.*\]|\{.*\})", clean, re.DOTALL)
            if match:
                return json.loads(match.group(1))
            raise ValueError(f"Could not parse JSON from response: {clean[:200]}")

    def _call_ws(self, wsfunction: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if not self.token:
            raise ValueError("Moodle Web Services Token required.")

        endpoint = f"{self.base_url}/webservice/rest/server.php?moodlewsrestformat=json"
        data = {
            "wstoken": self.token,
            "wsfunction": wsfunction,
            "moodlewsrestformat": "json"
        }
        if params:
            data.update(params)

        resp = requests.post(endpoint, data=data, verify=self.verify_ssl, timeout=30)
        resp.raise_for_status()
        return self._clean_json(resp.text)

    def get_enrolled_courses(self) -> List[Dict[str, Any]]:
        """Fetch courses user is enrolled in."""
        courses = []
        # 1. Try Web Service API
        if self.token:
            try:
                user_info = self._call_ws("core_webservice_get_site_info")
                user_id = user_info.get("userid")
                if user_id:
                    res = self._call_ws("core_enrol_get_users_courses", {"userid": user_id})
                    if isinstance(res, list):
                        courses = res
            except Exception as e:
                print(f"[MoodleSync] get_enrolled_courses WS failed: {e}")

        # 2. Fallback: Parse courses from web session /my/
        if not courses and self.session_cookie:
            try:
                my_page = self.session.get(f"{self.base_url}/my/", verify=self.verify_ssl, timeout=20)
                # Matches /course/view.php?id=(\d+)
                found = re.findall(r'/course/view\.php\?id=(\d+)["\'][^>]*>(.*?)</a>', my_page.text, re.DOTALL)
                seen_ids = set()
                for cid_str, raw_title in found:
                    cid = int(cid_str)
                    clean_title = re.sub(r'<[^>]+>', '', raw_title).strip()
                    if cid not in seen_ids and clean_title and len(clean_title) > 3:
                        seen_ids.add(cid)
                        courses.append({
                            "id": cid,
                            "fullname": clean_title,
                            "shortname": clean_title.split()[0]
                        })
            except Exception as e:
                print(f"[MoodleSync] Scraper get_enrolled_courses error: {e}")

        return courses

    def sync_course_materials(self, course_id: int, course_code: str) -> List[Dict[str, Any]]:
        """Downloads lecture slides and notes using Web Services + Session Scraper."""
        downloaded = []
        clean_code = re.sub(r'[^a-zA-Z0-9_\-]', '_', course_code).strip('_')

        # Register course in SQLite database
        self.db.register_course(course_id=clean_code, course_name=course_code, moodle_id=course_id)

        # Method 1: Web Service API
        if self.token:
            try:
                contents = self._call_ws("core_course_get_contents", {"courseid": course_id})
                if isinstance(contents, list):
                    for section in contents:
                        sec_name = section.get("name", "General").replace("/", "_").strip()
                        modules = section.get("modules", [])

                        for mod in modules:
                            mod_name = mod.get("name", "Lecture Notes")
                            contents_list = mod.get("contents", [])

                            for file_info in contents_list:
                                file_url = file_info.get("fileurl")
                                file_name = file_info.get("filename", "")
                                ext = Path(file_name).suffix.lower()

                                if ext in (".pdf", ".pptx", ".ppt", ".txt", ".docx") and file_url:
                                    target_dir = self.download_dir / clean_code / sec_name
                                    target_dir.mkdir(parents=True, exist_ok=True)
                                    target_file = target_dir / file_name

                                    # Replace pluginfile with webservice pluginfile for token auth
                                    dl_url = file_url
                                    if "/pluginfile.php/" in dl_url:
                                        dl_url = dl_url.replace("/pluginfile.php/", "/webservice/pluginfile.php/")
                                    dl_url = f"{dl_url}&token={self.token}" if "?" in dl_url else f"{dl_url}?token={self.token}"

                                    r = requests.get(dl_url, verify=self.verify_ssl, stream=True, timeout=60)
                                    if r.status_code == 200:
                                        with open(target_file, "wb") as f:
                                            for chunk in r.iter_content(chunk_size=8192):
                                                f.write(chunk)

                                        res = self.db.record_file(
                                            course_id=clean_code,
                                            file_path=target_file,
                                            week_num=1,
                                            lecture_title=mod_name
                                        )
                                        downloaded.append({
                                            "course_id": clean_code,
                                            "file_name": file_name,
                                            "change": res["change"]
                                        })
            except Exception as e:
                print(f"[MoodleSync] WS sync error for course {course_id} ({e}). Falling back to session scraper...")

        # Method 2: Session Scraper (Visits course/view.php?id=...)
        if len(downloaded) == 0:
            try:
                course_url = f"{self.base_url}/course/view.php?id={course_id}"
                c_page = self.session.get(course_url, verify=self.verify_ssl, timeout=20)
                
                # Look for resource URLs
                resource_matches = re.findall(r'href=["\'](https?://lms\.nust\.edu\.pk/(?:mod/resource/view\.php\?id=\d+|pluginfile\.php/[^"\']+))["\']', c_page.text)
                
                # Also look for links with instancename
                instance_matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>[\s\S]*?<span class="instancename">(.*?)<', c_page.text)
                
                all_links = set(resource_matches)
                title_map = {}
                for url, raw_t in instance_matches:
                    clean_t = re.sub(r'<[^>]+>', '', raw_t).strip()
                    title_map[url] = clean_t
                    if "resource" in url or "pluginfile" in url:
                        all_links.add(url)

                for link in all_links:
                    try:
                        resp = self.session.get(link, verify=self.verify_ssl, stream=True, timeout=30)
                        # Check Content-Disposition or final URL for filename
                        cd = resp.headers.get("content-disposition", "")
                        fname = ""
                        fn_match = re.search(r'filename=["\']?([^"\';\n]+)["\']?', cd)
                        if fn_match:
                            fname = fn_match.group(1).strip()
                        else:
                            fname = Path(resp.url.split("?")[0]).name

                        ext = Path(fname).suffix.lower()
                        if ext in (".pdf", ".pptx", ".ppt", ".txt", ".docx") and fname:
                            target_dir = self.download_dir / clean_code / "Lectures"
                            target_dir.mkdir(parents=True, exist_ok=True)
                            target_file = target_dir / fname

                            with open(target_file, "wb") as f:
                                for chunk in resp.iter_content(chunk_size=8192):
                                    f.write(chunk)

                            lecture_title = title_map.get(link) or fname
                            res = self.db.record_file(
                                course_id=clean_code,
                                file_path=target_file,
                                week_num=1,
                                lecture_title=lecture_title
                            )
                            downloaded.append({
                                "course_id": clean_code,
                                "file_name": fname,
                                "change": res["change"]
                            })
                    except Exception as ex:
                        continue
            except Exception as e:
                print(f"[MoodleSync] Scraper fallback error for course {course_id}: {e}")

        return downloaded
