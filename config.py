import os
from pathlib import Path
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parent
_env = dotenv_values(BASE_DIR / ".env")

DATA_DIR = BASE_DIR / "data"
LMS_DOWNLOADS_DIR = DATA_DIR / "lms_downloads"
TEXTBOOKS_DIR = DATA_DIR / "textbooks"
AUDIO_DIR = DATA_DIR / "audio_digests"
EXPORTS_DIR = DATA_DIR / "exports"
DB_PATH = DATA_DIR / "study_system.db"

# Ensure runtime directories exist
for folder in [DATA_DIR, LMS_DOWNLOADS_DIR, TEXTBOOKS_DIR, AUDIO_DIR, EXPORTS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# API Keys & Credentials (prefer exact .env file value)
GEMINI_API_KEY = _env.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = _env.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY", "")
TELEGRAM_BOT_TOKEN = _env.get("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = _env.get("TELEGRAM_CHAT_ID") or os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_PROXY = _env.get("TELEGRAM_PROXY") or os.getenv("TELEGRAM_PROXY") or os.getenv("HTTPS_PROXY", "")

# LMS Settings
LMS_TYPE = os.getenv("LMS_TYPE", "folder")  # 'moodle', 'canvas', or 'folder'
MOODLE_URL = os.getenv("MOODLE_URL", "https://lms.nust.edu.pk")
MOODLE_TOKEN = os.getenv("MOODLE_TOKEN", "")
MOODLE_SESSION_COOKIE = os.getenv("MOODLE_SESSION_COOKIE", "")
MOODLE_VERIFY_SSL = os.getenv("MOODLE_VERIFY_SSL", "false").lower() in ("true", "1", "yes")
CANVAS_URL = os.getenv("CANVAS_URL", "")
CANVAS_TOKEN = os.getenv("CANVAS_TOKEN", "")

# NotebookLM Settings (Optional)
NOTEBOOKLM_COOKIE = os.getenv("NOTEBOOKLM_COOKIE", "")
NOTEBOOKLM_ENABLED = os.getenv("NOTEBOOKLM_ENABLED", "false").lower() in ("true", "1", "yes")

# Scheduler Defaults
DAILY_SYNC_TIME = os.getenv("DAILY_SYNC_TIME", "19:00")  # 7 PM
WEEKEND_QUIZ_DAYS = os.getenv("WEEKEND_QUIZ_DAYS", "saturday,sunday").split(",")

# Study System Configuration
DAILY_MCQ_COUNT = int(os.getenv("DAILY_MCQ_COUNT", "10"))
DAILY_FLASHCARD_COUNT = int(os.getenv("DAILY_FLASHCARD_COUNT", "15"))
WEEKEND_QUIZ_COUNT = int(os.getenv("WEEKEND_QUIZ_COUNT", "15"))

# Server Settings
WEB_HOST = os.getenv("WEB_HOST", "127.0.0.1")
WEB_PORT = int(os.getenv("WEB_PORT", "8000"))
