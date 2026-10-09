// SynapseLMS Client Logic

let currentCourse = "all";
let dueCards = [];
let currentCardIdx = 0;
let currentMCQs = [];
let mockTimerInterval = null;
let revisionModeActive = false;
let flashcardRevisionModeActive = false;

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initModals();
  loadOverview();
  loadCourses();
  loadMCQs();
  loadFlashcards();
  loadWeakTopics();
  loadAudioDigests();
});

// ==================== TABS ====================
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      tabBtns.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));

      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      const targetContent = document.getElementById(targetId);
      if (targetContent) targetContent.classList.add("active");

      // Specific tab triggers
      if (targetId === "tab-mcq") loadMCQs();
      if (targetId === "tab-flashcards") loadFlashcards();
      if (targetId === "tab-weak") loadWeakTopics();
      if (targetId === "tab-exam") loadExamTab();
      if (targetId === "tab-audio") loadAudioDigests();
    });
  });
}

// ==================== COURSES & OVERVIEW ====================
async function loadCourses() {
  try {
    const res = await fetch("/api/courses");
    const data = await res.json();
    const selector = document.getElementById("courseSelector");
    const cheatSelect = document.getElementById("cheatSheetCourseSelect");
    
    // Clear dynamic options
    selector.innerHTML = '<option value="all">📚 All Enrolled Courses</option>';
    cheatSelect.innerHTML = '';

    data.courses.forEach(c => {
      const opt = document.createElement("option");
      opt.value = c;
      opt.textContent = `📖 ${c}`;
      selector.appendChild(opt);

      const opt2 = document.createElement("option");
      opt2.value = c;
      opt2.textContent = c;
      cheatSelect.appendChild(opt2);
    });

    selector.addEventListener("change", (e) => {
      currentCourse = e.target.value;
      loadOverview();
      loadMCQs();
      loadFlashcards();
      loadWeakTopics();
    });
  } catch (err) {
    console.error("Failed to load courses:", err);
  }
}

async function loadOverview() {
  try {
    const res = await fetch("/api/overview");
    const data = await res.json();

    document.getElementById("statFiles").textContent = data.stats.total_files || 0;
    document.getElementById("statMCQs").textContent = data.stats.total_mcqs || 0;
    document.getElementById("statCards").textContent = data.stats.total_flashcards || 0;
    document.getElementById("statAccuracy").textContent = `${data.stats.accuracy || 0}%`;
    document.getElementById("statExams").textContent = data.stats.upcoming_exams || 0;

    // Deadline banner
    const banner = document.getElementById("deadlineBanner");
    if (data.deadlines && data.deadlines.length > 0) {
      banner.style.display = "block";
      const d = data.deadlines[0];
      document.getElementById("bannerText").textContent = 
        `${d.title} (${d.course_id}) is due in ${d.hours_left}h! [${d.urgency}]`;
    } else {
      banner.style.display = "none";
    }

    // Exam countdown spotlight
    const examList = document.getElementById("overviewExamList");
    if (data.upcoming_exams && data.upcoming_exams.length > 0) {
      examList.innerHTML = data.upcoming_exams.map(ex => `
        <div class="exam-card">
          <div>
            <strong>${ex.exam_title} (${ex.course_id})</strong>
            <p class="text-muted">${ex.strategy}</p>
          </div>
          <div class="days-badge">${ex.days_left}d</div>
        </div>
      `).join("");
    }
  } catch (err) {
    console.error("Failed to load overview:", err);
  }
}

// ==================== QUIZ & MCQS ====================
async function loadMCQs() {
  const container = document.getElementById("quizContainer");
  container.innerHTML = '<div class="loading-spinner">Loading AI-generated lecture questions...</div>';
  revisionModeActive = false;
  document.getElementById("revisionModeBanner").style.display = "none";

  try {
    const res = await fetch(`/api/mcqs?course_id=${currentCourse}&limit=10`);
    const data = await res.json();
    currentMCQs = data.questions;

    if (!currentMCQs || currentMCQs.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <h3>No AI-generated questions available yet.</h3>
          <p class="text-muted">Click 'Ingest Slides' to parse a lecture and auto-generate MCQs, or use 'AI Regen' to regenerate from existing slides.</p>
        </div>`;
      return;
    }

    renderMCQCards(currentMCQs, container);
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Failed to load questions: ${err.message}</div>`;
  }
}

async function generateTenMCQs() {
  const btn = document.getElementById("btnGenerate10MCQs");
  const origHtml = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="btn-icon">⏳</span> Generating 10 MCQs...';

  const container = document.getElementById("quizContainer");
  const banner = document.getElementById("revisionModeBanner");
  if (banner) banner.style.display = "none";
  revisionModeActive = false;

  container.innerHTML = `
    <div class="glass-panel text-center" style="padding: 2.5rem 1.5rem;">
      <div class="loading-spinner" style="margin: 0 auto 1rem;"></div>
      <h3 style="margin-bottom:0.5rem;">🧠 Gemini AI is Generating 10 MCQs...</h3>
      <p class="text-muted">Analyzing course lecture slides and crafting 4-choice conceptual exam questions with citations.</p>
    </div>
  `;

  const formData = new FormData();
  formData.append("course_id", currentCourse);
  formData.append("count", 10);

  try {
    const res = await fetch("/api/mcqs/generate", {
      method: "POST",
      body: formData
    });
    const data = await res.json();

    if (data.status === "success" && data.questions && data.questions.length > 0) {
      currentMCQs = data.questions;
      renderMCQCards(currentMCQs, container);
      loadOverview();
    } else {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <h3>⚠️ Could Not Generate MCQs</h3>
          <p class="text-muted">Please ensure you have configured a valid Gemini API key in your .env file.</p>
          <button class="btn btn-primary" onclick="loadMCQs()" style="margin-top:0.8rem;">Load Existing Questions</button>
        </div>
      `;
    }
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Generation failed: ${err.message}</div>`;
  } finally {
    btn.disabled = false;
    btn.innerHTML = origHtml;
  }
}

async function enterRevisionMode() {
  const container = document.getElementById("quizContainer");
  const banner = document.getElementById("revisionModeBanner");
  container.innerHTML = '<div class="loading-spinner">Loading all MCQs from question bank...</div>';
  revisionModeActive = true;

  try {
    const res = await fetch(`/api/mcqs/all?course_id=${currentCourse}&limit=100`);
    const data = await res.json();
    currentMCQs = data.questions;

    if (!currentMCQs || currentMCQs.length === 0) {
      container.innerHTML = `<div class="glass-panel text-center"><h3>No MCQs in the bank yet.</h3><p class="text-muted">Ingest lecture slides to generate AI MCQs first.</p></div>`;
      banner.style.display = "none";
      return;
    }

    document.getElementById("revisionCount").textContent = currentMCQs.length;
    banner.style.display = "block";
    renderMCQCards(currentMCQs, container);
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Error loading MCQs: ${err.message}</div>`;
  }
}

function exitRevisionMode() {
  loadMCQs();
}

function renderMCQCards(questions, container) {
  container.innerHTML = questions.map((q, idx) => `
    <div class="quiz-card" id="mcq-card-${q.id}">
      <div class="quiz-meta">
        <span class="tag-course">${q.course_id}</span>
        <span class="tag-source">📍 ${q.source}</span>
        <span class="text-muted">Topic: ${q.topic}</span>
        ${q.generated_by === 'heuristic' ? '<span style="color:#f59e0b;font-size:0.75rem;">⚠️ Template</span>' : '<span style="color:#10b981;font-size:0.75rem;">✨ AI</span>'}
      </div>
      <div class="quiz-question">${idx + 1}. ${escapeHtml(q.question)}</div>
      <div class="quiz-options" id="opts-${q.id}">
        ${q.options.map((opt, oIdx) => `
          <button class="opt-btn" onclick="submitMCQAnswer(${q.id}, ${oIdx})">
            <strong>${String.fromCharCode(65 + oIdx)}.</strong> ${escapeHtml(opt)}
          </button>
        `).join("")}
      </div>
      <div class="quiz-feedback" id="feedback-${q.id}" style="display: none;"></div>
    </div>
  `).join("");
}

async function submitMCQAnswer(mcqId, chosenIdx) {
  const feedbackEl = document.getElementById(`feedback-${mcqId}`);
  const optsContainer = document.getElementById(`opts-${mcqId}`);
  const btns = optsContainer.querySelectorAll(".opt-btn");

  btns.forEach(b => b.disabled = true);

  const formData = new FormData();
  formData.append("mcq_id", mcqId);
  formData.append("user_answer", chosenIdx);

  try {
    const res = await fetch("/api/mcq/attempt", { method: "POST", body: formData });
    const result = await res.json();

    btns[result.correct_answer].classList.add("correct");
    if (!result.is_correct) {
      btns[chosenIdx].classList.add("wrong");
    }

    feedbackEl.style.display = "block";
    if (result.is_correct) {
      feedbackEl.innerHTML = `
        <p style="color: #34d399; font-weight: 600;">✅ Excellent! That's correct.</p>
        <p class="text-muted" style="margin-top: 0.4rem;">${escapeHtml(result.explanation)}</p>
      `;
    } else {
      feedbackEl.innerHTML = `
        <p style="color: #f87171; font-weight: 600;">❌ Incorrect.</p>
        <p class="text-muted" style="margin-top: 0.4rem;">${escapeHtml(result.explanation)}</p>
        <button class="btn btn-sm btn-outline" style="margin-top: 0.8rem;" 
                onclick="openStuckExplainer(${mcqId}, ${result.correct_answer}, ${chosenIdx})">
          💡 Explain Like I'm Stuck
        </button>
      `;
    }

    loadOverview();
  } catch (err) {
    console.error("Attempt error:", err);
  }
}

// ==================== EXPLAIN LIKE I'M STUCK ====================
async function openStuckExplainer(mcqId, correctIdx, userIdx) {
  const modal = document.getElementById("stuckModal");
  const loading = document.getElementById("stuckLoading");
  const content = document.getElementById("stuckContent");

  modal.style.display = "flex";
  loading.style.display = "block";
  content.innerHTML = "";

  const mcq = currentMCQs.find(q => q.id === mcqId);
  if (!mcq) return;

  const formData = new FormData();
  formData.append("question", mcq.question);
  formData.append("correct_option", mcq.options[correctIdx]);
  formData.append("user_option", mcq.options[userIdx]);
  formData.append("explanation", mcq.explanation);

  try {
    const res = await fetch("/api/explain_stuck", { method: "POST", body: formData });
    const data = await res.json();
    loading.style.display = "none";
    content.innerHTML = `<pre style="white-space: pre-wrap; font-family: var(--font-body); line-height: 1.6;">${escapeHtml(data.simple_explanation)}</pre>`;
  } catch (err) {
    loading.style.display = "none";
    content.textContent = "Error generating analogy: " + err.message;
  }
}

// ==================== FLASHCARDS (SM-2) ====================
async function loadFlashcards() {
  try {
    const res = await fetch(`/api/flashcards?course_id=${currentCourse}`);
    const data = await res.json();
    dueCards = data.flashcards || [];
    currentCardIdx = 0;
    flashcardRevisionModeActive = false;

    const banner = document.getElementById("flashcardModeBanner");
    if (banner) banner.style.display = "none";

    const counter = document.getElementById("flashcardCounter");
    counter.textContent = `${dueCards.length} cards due`;

    showCard();
  } catch (err) {
    console.error("Error loading flashcards:", err);
  }
}

async function loadAllFlashcardsForRevision() {
  try {
    const res = await fetch(`/api/flashcards?course_id=${currentCourse}&mode=all`);
    const data = await res.json();
    dueCards = data.flashcards || [];
    currentCardIdx = 0;
    flashcardRevisionModeActive = true;

    const banner = document.getElementById("flashcardModeBanner");
    if (banner) {
      document.getElementById("flashcardRevCount").textContent = dueCards.length;
      banner.style.display = "block";
    }

    const counter = document.getElementById("flashcardCounter");
    counter.textContent = `${dueCards.length} total cards`;

    showCard();
  } catch (err) {
    console.error("Error loading all flashcards:", err);
  }
}

function exitFlashcardRevisionMode() {
  loadFlashcards();
}

function showCard() {
  const flipCard = document.getElementById("flipCard");
  const frontText = document.getElementById("cardFrontText");
  const backText = document.getElementById("cardBackText");
  const topicFront = document.getElementById("cardTopicFront");
  const controls = document.getElementById("sm2Controls");

  flipCard.classList.remove("flipped");

  if (!dueCards || dueCards.length === 0 || currentCardIdx >= dueCards.length) {
    frontText.textContent = "🎉 All caught up! No flashcards due.";
    backText.textContent = "Great work! Return tomorrow for your scheduled SM-2 review.";
    topicFront.textContent = "Done";
    controls.style.display = "none";
    return;
  }

  const card = dueCards[currentCardIdx];
  topicFront.textContent = `${card.course_id} • ${card.topic}`;
  frontText.textContent = card.front;
  backText.textContent = card.back;
  controls.style.display = "flex";
}

document.getElementById("flipCard").addEventListener("click", () => {
  document.getElementById("flipCard").classList.toggle("flipped");
});

document.querySelectorAll(".btn-sm2").forEach(btn => {
  btn.addEventListener("click", async (e) => {
    e.stopPropagation();
    if (!dueCards[currentCardIdx]) return;
    const quality = btn.getAttribute("data-quality");
    const cardId = dueCards[currentCardIdx].id;

    const formData = new FormData();
    formData.append("card_id", cardId);
    formData.append("quality", quality);

    await fetch("/api/flashcard/review", { method: "POST", body: formData });

    currentCardIdx++;
    showCard();
    const remaining = dueCards.length - currentCardIdx;
    const label = flashcardRevisionModeActive ? `${remaining} of ${dueCards.length} cards` : `${remaining} cards due`;
    document.getElementById("flashcardCounter").textContent = label;
  });
});

// ==================== WEAK TOPICS RADAR ====================
async function loadWeakTopics() {
  const list = document.getElementById("weakTopicsList");
  list.innerHTML = '<div class="loading-spinner">Analyzing question attempt history...</div>';

  try {
    const res = await fetch(`/api/weak_topics?course_id=${currentCourse}`);
    const data = await res.json();
    const topics = data.weak_topics || [];

    if (topics.length === 0) {
      list.innerHTML = '<div class="empty-state">No weak topics logged yet. Answer quiz questions to build your radar!</div>';
      return;
    }

    list.innerHTML = topics.map(t => {
      const color = t.accuracy < 50 ? "#f43f5e" : (t.accuracy < 75 ? "#f59e0b" : "#10b981");
      return `
        <div class="weak-topic-item">
          <div>
            <strong>${escapeHtml(t.topic)}</strong>
            <span class="text-muted" style="margin-left: 0.5rem;">(${t.course_id})</span>
            <div style="font-size: 0.8rem; color: var(--text-muted);">
              ${t.correct_count} correct / ${t.total_attempts} attempts
            </div>
          </div>
          <div class="weak-topic-bar-wrap">
            <div class="accuracy-bar-bg">
              <div class="accuracy-bar-fill" style="width: ${t.accuracy}%; background: ${color};"></div>
            </div>
          </div>
          <div style="font-weight: 700; color: ${color}; min-width: 50px; text-align: right;">
            ${t.accuracy}%
          </div>
        </div>
      `;
    }).join("");
  } catch (err) {
    list.innerHTML = `<div class="empty-state">Error loading weak topics: ${err.message}</div>`;
  }
}

document.getElementById("btnStartWeekendQuiz").addEventListener("click", async () => {
  const container = document.getElementById("quizContainer");
  document.getElementById("tabBtnMCQ").click();
  container.innerHTML = '<div class="loading-spinner">Synthesizing 15 targeted questions from your weak areas...</div>';

  try {
    const res = await fetch(`/api/weekend_quiz?course_id=${currentCourse}`);
    const data = await res.json();
    currentMCQs = data.questions;

    if (!currentMCQs || currentMCQs.length === 0) {
      container.innerHTML = '<div class="empty-state">Not enough questions to compile weekend quiz.</div>';
      return;
    }

    container.innerHTML = `
      <div class="glass-panel" style="margin-bottom: 1.5rem; border-color: var(--accent-rose);">
        <h3>🎯 Targeted Weekend Diagnostic Quiz</h3>
        <p class="text-muted">15 questions heavily weighted on the topics you previously missed.</p>
      </div>
    ` + currentMCQs.map((q, idx) => `
      <div class="quiz-card" id="mcq-card-${q.id}">
        <div class="quiz-meta">
          <span class="tag-course">${q.course_id}</span>
          <span class="tag-source">📍 ${q.source}</span>
          <span class="text-muted">Targeted Weak Topic: ${q.topic}</span>
        </div>
        <div class="quiz-question">${idx + 1}. ${escapeHtml(q.question)}</div>
        <div class="quiz-options" id="opts-${q.id}">
          ${q.options.map((opt, oIdx) => `
            <button class="opt-btn" onclick="submitMCQAnswer(${q.id}, ${oIdx})">
              <strong>${String.fromCharCode(65 + oIdx)}.</strong> ${escapeHtml(opt)}
            </button>
          `).join("")}
        </div>
        <div class="quiz-feedback" id="feedback-${q.id}" style="display: none;"></div>
      </div>
    `).join("");
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Error: ${err.message}</div>`;
  }
});

// ==================== EXAM TAB & TIMED MOCKS ====================
async function loadExamTab() {
  const grid = document.getElementById("examScheduleGrid");
  try {
    const res = await fetch("/api/exams");
    const data = await res.json();

    if (!data.exams || data.exams.length === 0) {
      grid.innerHTML = '<div class="empty-state">No exams registered. Add an exam to see your countdown timeline.</div>';
      return;
    }

    grid.innerHTML = data.exams.map(ex => `
      <div class="glass-panel">
        <div class="panel-header">
          <div>
            <h3>${ex.exam_title} (${ex.course_id})</h3>
            <span class="pill pill-success">${ex.phase}</span>
          </div>
          <div class="days-badge">${ex.days_left} Days Left</div>
        </div>
        <p class="text-muted"><strong>Target Score:</strong> ${ex.target_score}%</p>
        <p class="text-muted"><strong>Recommended Strategy:</strong> ${ex.strategy}</p>
        <button class="btn btn-sm btn-accent" style="margin-top: 1rem;" 
                onclick="startMockExam('${ex.course_id}')">
          ⚡ Launch Timed Mock for ${ex.course_id}
        </button>
      </div>
    `).join("");
  } catch (err) {
    console.error(err);
  }
}

async function startMockExam(courseId) {
  const container = document.getElementById("mockExamContainer");
  const area = document.getElementById("mockQuestionsArea");
  container.style.display = "block";
  window.scrollTo({ top: container.offsetTop - 80, behavior: 'smooth' });

  const res = await fetch(`/api/mock_exam?course_id=${courseId}&question_count=15&time_limit_minutes=20`);
  const data = await res.json();

  let seconds = 20 * 60;
  clearInterval(mockTimerInterval);
  const timerEl = document.getElementById("mockTimer");

  mockTimerInterval = setInterval(() => {
    seconds--;
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    timerEl.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    if (seconds <= 0) {
      clearInterval(mockTimerInterval);
      alert("Time is up! Exam auto-submitted.");
    }
  }, 1000);

  area.innerHTML = data.questions.map((q, idx) => `
    <div class="quiz-card" style="margin-top: 1rem;">
      <div class="quiz-question">${idx + 1}. ${escapeHtml(q.question)}</div>
      <div class="quiz-options">
        ${q.options.map((opt, oIdx) => `
          <button class="opt-btn" onclick="this.classList.toggle('correct')">
            ${String.fromCharCode(65 + oIdx)}. ${escapeHtml(opt)}
          </button>
        `).join("")}
      </div>
    </div>
  `).join("");
}

// ==================== AUDIO DIGESTS ====================
async function loadAudioDigests() {
  const container = document.getElementById("audioDigestsContainer");
  try {
    const res = await fetch("/api/audio_digests");
    const data = await res.json();
    const digests = data.digests || [];

    if (digests.length === 0) {
      container.innerHTML = '<div class="empty-state">No audio digests generated yet. Ingest lectures to synthesize daily briefs!</div>';
      return;
    }

    container.innerHTML = digests.map(d => `
      <div class="audio-item">
        <strong>${escapeHtml(d.title)}</strong>
        <p class="text-muted" style="margin: 0.5rem 0;">${escapeHtml(d.script_text.substring(0, 200))}...</p>
        ${d.audio_path ? `
          <div class="audio-controls">
            <audio controls src="/api/audio/play/${encodeURIComponent(d.audio_path.split('\\\\').pop().split('/').pop())}"></audio>
          </div>
        ` : '<p class="text-muted" style="font-size:0.8rem;">Text transcript generated.</p>'}
      </div>
    `).join("");
  } catch (err) {
    console.error(err);
  }
}

// ==================== CHEAT SHEETS & VAULT ====================
document.getElementById("btnLoadCheatSheet").addEventListener("click", async () => {
  const select = document.getElementById("cheatSheetCourseSelect");
  const course = select.value;
  if (!course) return;

  const contentEl = document.getElementById("cheatSheetContent");
  contentEl.innerHTML = '<div class="loading-spinner">Generating 1-page formula & definition matrix...</div>';

  try {
    const res = await fetch(`/api/cheatsheet?course_id=${course}`);
    const data = await res.json();
    contentEl.textContent = data.content || "No concepts extracted yet.";
  } catch (err) {
    contentEl.textContent = "Error: " + err.message;
  }
});

// ==================== MODALS & FORMS ====================
function initModals() {
  // Sync now button
  document.getElementById("btnSyncNow").addEventListener("click", async () => {
    const btn = document.getElementById("btnSyncNow");
    btn.textContent = "🔄 Syncing...";
    btn.disabled = true;

    try {
      const formData = new FormData();
      formData.append("lms_type", "folder");
      const res = await fetch("/api/sync", { method: "POST", body: formData });
      const data = await res.json();
      alert(`Sync completed! ${data.synced_count} files checked, ${data.processed_count} new lectures processed.`);
      loadOverview();
      loadCourses();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("Sync failed: " + err.message);
    } finally {
      btn.innerHTML = '<span class="btn-icon">🔄</span> Sync Pipeline';
      btn.disabled = false;
    }
  });

  // NUST LMS Modal
  const nustModal = document.getElementById("nustModal");
  document.getElementById("btnNustModal").addEventListener("click", () => nustModal.style.display = "flex");
  document.getElementById("btnCloseNustModal").addEventListener("click", () => nustModal.style.display = "none");

  document.getElementById("nustLoginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const progress = document.getElementById("nustProgress");
    const submitBtn = document.getElementById("btnSubmitNust");
    progress.style.display = "block";
    submitBtn.disabled = true;

    const formData = new FormData();
    formData.append("username", document.getElementById("nustUsername").value);
    formData.append("password", document.getElementById("nustPassword").value);

    try {
      const res = await fetch("/api/moodle/login", { method: "POST", body: formData });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Authentication failed");

      nustModal.style.display = "none";
      alert(`🎉 Connected to NUST LMS!\nDiscovered ${data.enrolled_courses.length} courses: ${data.enrolled_courses.join(", ")}\nIngested ${data.synced_files} slide decks.`);
      loadOverview();
      loadCourses();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("NUST LMS Connection Error: " + err.message);
    } finally {
      progress.style.display = "none";
      submitBtn.disabled = false;
    }
  });

  // Upload Modal
  const uploadModal = document.getElementById("uploadModal");
  document.getElementById("btnUploadModal").addEventListener("click", () => uploadModal.style.display = "flex");
  document.getElementById("btnCloseUploadModal").addEventListener("click", () => uploadModal.style.display = "none");

  document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const progress = document.getElementById("uploadProgress");
    const submitBtn = document.getElementById("btnSubmitUpload");
    progress.style.display = "block";
    submitBtn.disabled = true;

    const formData = new FormData();
    formData.append("course_id", document.getElementById("uploadCourse").value);
    formData.append("week_num", document.getElementById("uploadWeek").value);
    formData.append("file", document.getElementById("uploadFile").files[0]);

    try {
      const res = await fetch("/api/upload_lecture", { method: "POST", body: formData });
      const data = await res.json();
      uploadModal.style.display = "none";
      alert(`Lecture ingested successfully! Study materials generated.`);
      loadOverview();
      loadCourses();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("Upload failed: " + err.message);
    } finally {
      progress.style.display = "none";
      submitBtn.disabled = false;
    }
  });

  // Exam Modal
  const examModal = document.getElementById("addExamModal");
  document.getElementById("btnAddExamModalOpen").addEventListener("click", () => examModal.style.display = "flex");
  document.getElementById("btnCloseExamModal").addEventListener("click", () => examModal.style.display = "none");

  document.getElementById("addExamForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("course_id", document.getElementById("modalExamCourse").value);
    formData.append("exam_title", document.getElementById("modalExamTitle").value);
    formData.append("exam_date", document.getElementById("modalExamDate").value);
    formData.append("target_score", document.getElementById("modalExamScore").value);

    try {
      await fetch("/api/exams/add", { method: "POST", body: formData });
      examModal.style.display = "none";
      loadOverview();
      loadExamTab();
    } catch (err) {
      alert("Failed to save exam: " + err.message);
    }
  });

  // Stuck modal close
  document.getElementById("btnCloseStuckModal").addEventListener("click", () => {
    document.getElementById("stuckModal").style.display = "none";
  });
  document.getElementById("btnGotItStuck").addEventListener("click", () => {
    document.getElementById("stuckModal").style.display = "none";
  });

  // On-demand 10 AI MCQs Generation
  const btnGen10 = document.getElementById("btnGenerate10MCQs");
  if (btnGen10) {
    btnGen10.addEventListener("click", () => generateTenMCQs());
  }

  document.getElementById("btnRefreshQuiz").addEventListener("click", () => loadMCQs());

  // Practice Old MCQs (Revision Mode)
  document.getElementById("btnRevisionMode").addEventListener("click", () => enterRevisionMode());

  // Review All Flashcards (Revision Mode)
  document.getElementById("btnReviewAllCards").addEventListener("click", () => loadAllFlashcardsForRevision());

  // Delete Low-Quality (heuristic/template) MCQs and Flashcards
  document.getElementById("btnDeleteLowQuality").addEventListener("click", async () => {
    if (!confirm("This will permanently DELETE all template-generated (non-AI) MCQs and flashcards.\n\nOnly AI-generated content (Gemini/OpenAI) will be kept. This action cannot be undone.\n\nContinue?")) return;

    const btn = document.getElementById("btnDeleteLowQuality");
    btn.innerHTML = '<span class="btn-icon">⏳</span> Deleting...';
    btn.disabled = true;

    try {
      const res = await fetch(`/api/mcqs/heuristic?course_id=${currentCourse}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Deletion failed");

      alert(`✅ Cleanup Complete!\n\n🗑️ Deleted: ${data.deleted_mcqs} low-quality MCQs\n🗑️ Deleted: ${data.deleted_flashcards} heuristic flashcards\n\nOnly high-quality AI-generated content remains.`);
      loadOverview();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("Deletion failed: " + err.message);
    } finally {
      btn.innerHTML = '<span class="btn-icon">🗑️</span> Delete Low-Quality';
      btn.disabled = false;
    }
  });

  // AI Regeneration button — wipes old MCQs and calls Gemini for all lectures
  document.getElementById("btnRegenAI").addEventListener("click", async () => {
    if (!confirm("This will DELETE all current MCQs and regenerate them using Gemini AI from your lecture slides.\n\nThis may take several minutes. Continue?")) return;

    const btn = document.getElementById("btnRegenAI");
    btn.innerHTML = '<span class="btn-icon">⏳</span> Generating...';
    btn.disabled = true;

    try {
      const res = await fetch("/api/regenerate_mcqs", { method: "POST" });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Regeneration failed");

      alert(`✅ AI Generation Complete!\n\n📝 New MCQs: ${data.new_mcqs}\n🗂️ New Flashcards: ${data.new_flashcards}\n📁 Files processed: ${data.files_reprocessed}`);
      loadOverview();
      loadMCQs();
      loadFlashcards();
      loadWeakTopics();
    } catch (err) {
      alert("AI Regeneration failed: " + err.message);
    } finally {
      btn.innerHTML = '<span class="btn-icon">🤖</span> AI Regen';
      btn.disabled = false;
    }
  });

}

function escapeHtml(text) {
  if (!text) return "";
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
