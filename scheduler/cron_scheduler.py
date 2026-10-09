import time
import schedule
from datetime import datetime
from config import DAILY_SYNC_TIME, LMS_TYPE
from pipeline import StudyPipeline
from repetition.weak_tracker import WeakTopicTracker
from exam.exam_engine import ExamEngine

class StudyScheduler:
    """Manages recurring automated daily processing, weekend reviews,
    and deadline alerts.
    """

    def __init__(self):
        self.pipeline = StudyPipeline()
        self.weak_tracker = WeakTopicTracker(db=self.pipeline.db)
        self.exam_engine = ExamEngine(db=self.pipeline.db)

    def daily_job(self):
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [Daily] Running Daily Study Job...")
        # 1. Sync from LMS
        self.pipeline.run_sync(LMS_TYPE)
        # 2. Process pending materials (generates 10 MCQs & 15 Flashcards)
        results = self.pipeline.process_pending_files()
        print(f"[Daily Job] Processed {len(results)} new lectures.")

        # 3. Check deadlines
        alerts = self.exam_engine.check_deadlines_due_soon()
        if alerts:
            print(f"[Daily Job] [ALERT] {len(alerts)} assignment deadlines approaching!")

    def weekend_quiz_job(self):
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [Weekend] Running Weekend Weak-Topic Quiz Job...")
        quiz = self.weak_tracker.generate_weekend_quiz(total_questions=15)
        print(f"[Weekend Quiz] Generated targeted 15-question review quiz from weak areas.")
        return quiz

    def start_scheduler(self):
        print(f"[Scheduler] Active. Daily sync set for {DAILY_SYNC_TIME}. Weekend quizzes scheduled.")
        schedule.every().day.at(DAILY_SYNC_TIME).do(self.daily_job)
        schedule.every().saturday.at("09:00").do(self.weekend_quiz_job)
        schedule.every().sunday.at("09:00").do(self.weekend_quiz_job)

        while True:
            schedule.run_pending()
            time.sleep(30)
