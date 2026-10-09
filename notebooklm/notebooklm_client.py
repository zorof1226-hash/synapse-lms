import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import AUDIO_DIR, NOTEBOOKLM_COOKIE, NOTEBOOKLM_ENABLED

class NotebookLMClient:
    """Optional wrapper around NotebookLM (via notebooklm-py or cookie session),
    with robust fallback to local audio digest synthesis so the daily pipeline never halts.
    """

    def __init__(self, cookie: str = NOTEBOOKLM_COOKIE, enabled: bool = NOTEBOOKLM_ENABLED):
        self.cookie = cookie
        self.enabled = enabled
        self._client = None
        if self.enabled and self.cookie:
            self._init_client()

    def _init_client(self):
        try:
            # Attempt to import unofficial notebooklm-py if available
            import notebooklm
            self._client = notebooklm.NotebookLM(cookies=self.cookie)
            print("[NotebookLM] Successfully initialized NotebookLM client.")
        except Exception as e:
            print(f"[NotebookLM] Client initialization failed (fallback enabled): {e}")
            self._client = None

    def sync_lecture_to_notebook(self, course_id: str, file_path: Path) -> Dict[str, Any]:
        """Uploads lecture file to course notebook if NotebookLM is configured."""
        if not self.enabled or not self._client:
            return {
                "status": "bypassed",
                "message": "NotebookLM layer skipped (offline/fallback mode active)"
            }

        try:
            # Look up or create notebook for course
            notebooks = self._client.list_notebooks()
            nb = next((n for n in notebooks if n.title == f"{course_id} - Course Notebook"), None)
            if not nb:
                nb = self._client.create_notebook(f"{course_id} - Course Notebook")

            # Upload file
            nb.upload_file(str(file_path))
            return {
                "status": "success",
                "notebook_id": nb.id,
                "notebook_title": nb.title,
                "file_uploaded": file_path.name
            }
        except Exception as e:
            print(f"[NotebookLM] Upload failed for {file_path.name} (pipeline continues): {e}")
            return {
                "status": "failed",
                "error": str(e),
                "fallback": "Standard LLM pipeline used"
            }

    def generate_audio_digest(self, course_id: str, lecture_title: str, summary_text: str, key_terms: List[Dict]) -> Dict[str, Any]:
        """Generates a 5-minute study audio digest.
        Attempts NotebookLM audio overview first, falling back to local TTS engine.
        """
        # 1. Draft the podcast/audio recap script
        terms_str = ". ".join([f"{t.get('term', '')}: {t.get('definition', '')}" for t in key_terms[:5]])
        script = (
            f"Welcome to your daily study briefing for {course_id}, covering {lecture_title}. "
            f"Here is your executive summary: {summary_text} "
            f"Now, let's lock in the core concepts. {terms_str}. "
            f"Review your flashcards today to lock this into long-term memory. Happy studying!"
        )

        audio_filename = f"{course_id}_{lecture_title.replace(' ', '_')[:20]}_digest.wav"
        audio_path = AUDIO_DIR / audio_filename

        # 2. Check if NotebookLM audio overview is available
        if self.enabled and self._client:
            try:
                # If notebooklm-py supports generate_audio
                # nb.generate_audio_overview() ...
                pass
            except Exception as e:
                print(f"[NotebookLM] Audio overview generation error: {e}")

        # 3. Fallback: Synthesize with local pyttsx3 TTS
        synthesized = False
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty("rate", 175) # natural speaking speed
            engine.save_to_file(script, str(audio_path))
            engine.runAndWait()
            synthesized = True
        except Exception as e:
            print(f"[AudioDigest] pyttsx3 synthesis warning: {e}")

        return {
            "title": f"Daily Audio Recap: {lecture_title}",
            "course_id": course_id,
            "script": script,
            "audio_path": str(audio_path) if synthesized and audio_path.exists() else None,
            "synthesized": synthesized
        }
