import json
import logging
import socket
from typing import Optional
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_PROXY
from db.database import Database
from generation.llm_generator import LLMGenerator
from repetition.weak_tracker import WeakTopicTracker
from exam.exam_engine import ExamEngine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_telegram_reachability(timeout=4) -> bool:
    try:
        sock = socket.create_connection(("api.telegram.org", 443), timeout=timeout)
        sock.close()
        return True
    except Exception:
        return False

class StudyTelegramBot:
    """Telegram Bot interface for interactive mobile quizzes, flashcards,
    weak-topic reviews, and 'Explain like I'm stuck' breakdowns.
    """

    def __init__(self, token: str = TELEGRAM_BOT_TOKEN, proxy: str = TELEGRAM_PROXY, db: Database = None):
        self.token = token
        self.proxy = proxy
        self.db = db or Database()
        self.generator = LLMGenerator()
        self.weak_tracker = WeakTopicTracker(db=self.db)
        self.exam_engine = ExamEngine(db=self.db)

    def is_configured(self) -> bool:
        return bool(self.token)

    def run(self):
        if not self.is_configured():
            print("[TelegramBot] TELEGRAM_BOT_TOKEN not set. Skipping Telegram bot runner.")
            return

        try:
            from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
            from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
        except ImportError:
            print("[TelegramBot] python-telegram-bot not installed or version incompatible.")
            return

        builder = Application.builder().token(self.token)
        if self.proxy:
            print(f"[TelegramBot] Using configured proxy: {self.proxy}")
            builder = builder.proxy(self.proxy).get_updates_proxy(self.proxy)
        else:
            print("[TelegramBot] Testing connection to api.telegram.org...")
            if not check_telegram_reachability():
                print("\n" + "="*68)
                print("[TelegramBot] [WARNING] CANNOT CONNECT TO api.telegram.org (Connection Timed Out)")
                print("="*68)
                print("Notice: Direct access to Telegram's servers is restricted by ISPs in Pakistan.")
                print("\nTo connect and run the bot:")
                print("  Option A (Recommended): Turn on a VPN (e.g., Cloudflare WARP 1.1.1.1,")
                print("             ProtonVPN, etc.) and run 'python main.py bot' again.")
                print("  Option B: Set a proxy in your .env file:")
                print("             TELEGRAM_PROXY=http://127.0.0.1:YOUR_PORT")
                print("="*68 + "\n")
                return

        async def on_startup(application: Application):
            bot_info = await application.bot.get_me()
            print("\n" + "="*68)
            print(">> [TelegramBot] ONLINE AND POLLING SUCCESSFULLY!")
            print(f">> Bot Name    : {bot_info.first_name}")
            print(f">> Bot Username: @{bot_info.username}")
            print(f">> Direct Link : https://t.me/{bot_info.username}")
            print("="*68)
            print(">> Open Telegram and send /start to interact!")
            print(">> Available commands: /start, /quiz, /courses, /weak, /exam, /weekend")
            print("="*68 + "\n")

        app = builder.post_init(on_startup).build()

        async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
            msg = (
                "🎓 *Automated Study System Bot*\n\n"
                "Available Commands:\n"
                "• `/quiz [course]` - Take an interactive MCQ\n"
                "• `/flashcards [course]` - Review SM-2 spaced repetition cards\n"
                "• `/weak` - View weak topics & error rates\n"
                "• `/weekend` - Take 15-question targeted weekend review quiz\n"
                "• `/exam` - Check exam countdown & cram status\n"
                "• `/courses` - List all synchronized courses"
            )
            await update.message.reply_text(msg, parse_mode="Markdown")

        async def courses_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
            courses = self.db.get_all_courses()
            if not courses:
                await update.message.reply_text("No courses synced yet. Ingest lecture slides first!")
                return
            courses_list = "\n".join([f"• `{c}`" for c in courses])
            await update.message.reply_text(f"📚 *Enrolled Courses:*\n{courses_list}", parse_mode="Markdown")

        async def quiz_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
            args = context.args
            course_id = args[0] if args else None

            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM mcqs"
                params = []
                if course_id:
                    query += " WHERE course_id = ?"
                    params.append(course_id)
                query += " ORDER BY RANDOM() LIMIT 1"
                cursor.execute(query, params)
                row = cursor.fetchone()

            if not row:
                await update.message.reply_text("No questions found for this query.")
                return

            q = dict(row)
            options = json.loads(q["options"])
            keyboard = []
            for i, opt in enumerate(options):
                keyboard.append([InlineKeyboardButton(f"{chr(65+i)}. {opt[:40]}", callback_data=f"ans:{q['id']}:{i}")])

            reply_markup = InlineKeyboardMarkup(keyboard)
            text = (
                f"📝 *[{q['course_id']}] {q['topic']}*\n\n"
                f"{q['question']}\n\n"
                f"📌 *Source*: `{q['source']}`"
            )
            await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

        async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
            query = update.callback_query
            await query.answer()
            data = query.data

            if data.startswith("ans:"):
                _, mcq_id_str, user_ans_str = data.split(":")
                mcq_id = int(mcq_id_str)
                user_ans = int(user_ans_str)

                result = self.db.log_quiz_attempt(mcq_id, user_ans)
                if "error" in result:
                    await query.edit_message_text("Question expired.")
                    return

                if result["is_correct"]:
                    reply_text = (
                        f"✅ *CORRECT! (+1)*\n\n"
                        f"{result['explanation']}\n\n"
                        f"📍 *Citation*: `{result['source']}`"
                    )
                    await query.edit_message_text(reply_text, parse_mode="Markdown")
                else:
                    stuck_btn = InlineKeyboardMarkup([[
                        InlineKeyboardButton("💡 Explain Like I'm Stuck", callback_data=f"stuck:{mcq_id}:{user_ans}")
                    ]])
                    reply_text = (
                        f"❌ *INCORRECT*\n\n"
                        f"Correct answer was Option {chr(65 + result['correct_answer'])}.\n\n"
                        f"📖 *Explanation*: {result['explanation']}\n"
                        f"📍 *Citation*: `{result['source']}`"
                    )
                    await query.edit_message_text(reply_text, reply_markup=stuck_btn, parse_mode="Markdown")

            elif data.startswith("stuck:"):
                _, mcq_id_str, user_ans_str = data.split(":")
                mcq_id = int(mcq_id_str)
                user_ans = int(user_ans_str)

                with self.db.get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT question, options, answer_idx, explanation FROM mcqs WHERE id = ?", (mcq_id,))
                    row = cursor.fetchone()

                if row:
                    opts = json.loads(row["options"])
                    stuck_resp = self.generator.explain_stuck(
                        question=row["question"],
                        correct_option=opts[row["answer_idx"]],
                        user_option=opts[user_ans],
                        explanation=row["explanation"]
                    )
                    await query.message.reply_text(stuck_resp["simple_explanation"])

        async def weak_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
            weaks = self.weak_tracker.get_topic_analytics()
            if not weaks:
                await update.message.reply_text("No quiz attempts recorded yet. Answer questions with /quiz first!")
                return

            lines = ["🎯 *Weak Topics Breakdown (Lowest Accuracy First):*\n"]
            for w in weaks:
                emoji = "🔴" if w["accuracy"] < 50 else ("🟡" if w["accuracy"] < 75 else "🟢")
                lines.append(f"{emoji} *{w['topic']}* ({w['course_id']}): {w['accuracy']}% ({w['correct_count']}/{w['total_attempts']})")
            await update.message.reply_text("\n".join(lines), parse_mode="Markdown")

        async def exam_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
            exams = self.exam_engine.get_upcoming_exams()
            if not exams:
                await update.message.reply_text("No upcoming exams configured.")
                return

            lines = ["📅 *Upcoming Exams & Revision Phases:*\n"]
            for ex in exams:
                lines.append(
                    f"• *{ex['exam_title']}* ({ex['course_id']})\n"
                    f"  ⏳ `{ex['days_left']} days left` (Date: {ex['exam_date']})\n"
                    f"  🔥 Phase: *{ex['phase']}*\n"
                    f"  💡 Strategy: {ex['strategy']}\n"
                )
            await update.message.reply_text("\n".join(lines), parse_mode="Markdown")

        app.add_handler(CommandHandler("start", start_cmd))
        app.add_handler(CommandHandler("courses", courses_cmd))
        app.add_handler(CommandHandler("quiz", quiz_cmd))
        app.add_handler(CommandHandler("weak", weak_cmd))
        app.add_handler(CommandHandler("exam", exam_cmd))
        app.add_handler(CallbackQueryHandler(callback_handler))

        print("[TelegramBot] Polling started...")
        app.run_polling()
