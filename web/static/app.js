// SynapseLMS Client Logic

let currentCourse = "all";
let dueCards = [];
let currentCardIdx = 0;
let currentMCQs = [];
let mockTimerInterval = null;
let revisionModeActive = false;
let flashcardRevisionModeActive = false;

// ==================== DYNAMIC BACKEND CONFIGURATION ====================
let API_BASE = "";
if (window.location.hostname.includes("github.io") || window.location.protocol === "file:") {
  API_BASE = localStorage.getItem("synapse_api_base") || "http://127.0.0.1:8000";
}

async function apiFetch(endpoint, options = {}) {
  const url = endpoint.startsWith("http") ? endpoint : `${API_BASE}${endpoint}`;
  try {
    const res = await fetch(url, options);
    const contentType = res.headers.get("content-type") || "";
    
    if (!contentType.includes("application/json")) {
      const text = await res.text();
      if (text.trim().startsWith("<")) {
        const isGhPages = window.location.hostname.includes("github.io");
        throw new Error(
          isGhPages
            ? `Cannot connect to SynapseLMS backend at ${url}.\n\n` +
              `• You are viewing the GitHub Pages frontend.\n` +
              `• Ensure your local backend is running ('python main.py run') at ${API_BASE}.\n` +
              `• Click the 'Local (8000)' badge in the top right to change backend URL if needed.`
            : `Backend returned HTML instead of JSON. Ensure the FastAPI server is running on port 8000.`
        );
      }
      throw new Error(`Unexpected non-JSON response from server: ${text.slice(0, 150)}`);
    }

    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || data.message || `Server error (${res.status})`);
    }
    return data;
  } catch (err) {
    if (err.message.includes("Failed to fetch") || err.name === "TypeError") {
      throw new Error(
        `Backend unreachable at ${API_BASE || window.location.origin}.\n\n` +
        `• Make sure 'python main.py run' is currently running in your terminal.\n` +
        `• If you are accessing via browser, you can also open http://127.0.0.1:8000 directly.`
      );
    }
    throw err;
  }
}

function updateBackendStatus() {
  const pill = document.getElementById("backendStatusLabel");
  const dot = document.getElementById("backendStatusDot");
  if (!pill) return;
  if (!API_BASE) {
    pill.textContent = "Local (8000)";
    if (dot) dot.className = "status-dot online";
  } else {
    const cleanDisplay = API_BASE.replace(/^https?:\/\//, "");
    pill.textContent = cleanDisplay.length > 18 ? cleanDisplay.slice(0, 15) + "..." : cleanDisplay;
    fetch(`${API_BASE}/api/overview`)
      .then(res => res.json())
      .then(() => { if (dot) dot.className = "status-dot online"; })
      .catch(() => { if (dot) dot.className = "status-dot offline"; });
  }
}

function promptBackendUrl() {
  const current = API_BASE || "http://127.0.0.1:8000";
  const newUrl = prompt(
    "Configure SynapseLMS Backend API URL:\n" +
    "(e.g. http://127.0.0.1:8000 for your local machine, or your deployed cloud server)",
    current
  );
  if (newUrl !== null) {
    const cleanUrl = newUrl.trim().replace(/\/+$/, "");
    localStorage.setItem("synapse_api_base", cleanUrl);
    API_BASE = cleanUrl;
    updateBackendStatus();
    loadOverview();
    loadCourses();
    loadMCQs();
    loadFlashcards();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initModals();
  updateBackendStatus();
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
    const data = await apiFetch("/api/courses");
    const selector = document.getElementById("courseSelector");
    const cheatSelect = document.getElementById("cheatSheetCourseSelect");
    
    selector.innerHTML = '<option value="all">📚 All Enrolled Courses</option>';
    cheatSelect.innerHTML = '';

    (data.courses || []).forEach(c => {
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
    const data = await apiFetch("/api/overview");

    document.getElementById("statFiles").textContent = data.stats.total_files || 0;
    document.getElementById("statMCQs").textContent = data.stats.total_mcqs || 0;
    document.getElementById("statCards").textContent = data.stats.total_flashcards || 0;
    document.getElementById("statAccuracy").textContent = `${data.stats.accuracy || 0}%`;
    document.getElementById("statExams").textContent = data.stats.upcoming_exams || 0;

    const banner = document.getElementById("deadlineBanner");
    if (data.deadlines && data.deadlines.length > 0) {
      banner.style.display = "block";
      const d = data.deadlines[0];
      document.getElementById("bannerText").textContent = 
        `${d.title} (${d.course_id}) is due in ${d.hours_left}h! [${d.urgency}]`;
    } else {
      banner.style.display = "none";
    }

    const examList = document.getElementById("overviewExamList");
    if (data.upcoming_exams && data.upcoming_exams.length > 0) {
      examList.innerHTML = data.upcoming_exams.map(ex => `
        <div class="exam-card">
          <div>
            <strong>${escapeHtml(ex.exam_title)} (${escapeHtml(ex.course_id)})</strong>
            <p class="text-muted">${escapeHtml(ex.strategy)}</p>
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
  container.innerHTML = '<div class="loading-spinner">Loading high-yield lecture questions...</div>';
  revisionModeActive = false;
  document.getElementById("revisionModeBanner").style.display = "none";

  try {
    const data = await apiFetch(`/api/mcqs?course_id=${currentCourse}&limit=10`);
    currentMCQs = data.questions || [];

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
    container.innerHTML = `<div class="empty-state">Failed to load questions: ${escapeHtml(err.message)}</div>`;
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
    const data = await apiFetch("/api/mcqs/generate", {
      method: "POST",
      body: formData
    });

    if (data.status === "success" && data.questions && data.questions.length > 0) {
      currentMCQs = data.questions;
      renderMCQCards(currentMCQs, container);
      loadOverview();
    } else {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <h3>No lecture materials found</h3>
          <p class="text-muted">${escapeHtml(data.message || "Please upload slides first.")}</p>
        </div>
      `;
    }
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Generation error: ${escapeHtml(err.message)}</div>`;
  } finally {
    btn.disabled = false;
    btn.innerHTML = origHtml;
  }
}

async function enterRevisionMode() {
  const container = document.getElementById("quizContainer");
  container.innerHTML = '<div class="loading-spinner">Loading all historical questions...</div>';
  revisionModeActive = true;

  try {
    const data = await apiFetch(`/api/mcqs/all?course_id=${currentCourse}&limit=100`);
    currentMCQs = data.questions || [];

    if (!currentMCQs || currentMCQs.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <h3>No historical questions found</h3>
          <p class="text-muted">Generate or ingest questions first to practice in revision mode.</p>
        </div>`;
      return;
    }

    const banner = document.getElementById("revisionModeBanner");
    banner.style.display = "block";
    banner.textContent = `📖 Revision Mode: Practicing ${currentMCQs.length} Questions for ${currentCourse === 'all' ? 'All Courses' : currentCourse}`;

    renderMCQCards(currentMCQs, container);
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Failed to load revision questions: ${escapeHtml(err.message)}</div>`;
  }
}

function renderMCQCards(questions, container) {
  container.innerHTML = questions.map((q, idx) => `
    <div class="mcq-card" id="mcq-${q.id}">
      <div class="mcq-header">
        <span class="mcq-topic-tag">${escapeHtml(q.topic || 'General')}</span>
        <span class="mcq-source-tag">📌 ${escapeHtml(q.source || 'Lecture Notes')}</span>
      </div>
      <div class="mcq-question">${idx + 1}. ${escapeHtml(q.question)}</div>
      <div class="mcq-options">
        ${(q.options || []).map((opt, optIdx) => `
          <button class="option-btn" onclick="submitAnswer(${q.id}, ${optIdx}, ${q.answer_idx})">
            <span class="opt-letter">${String.fromCharCode(65 + optIdx)}</span>
            <span class="opt-text">${escapeHtml(opt)}</span>
          </button>
        `).join("")}
      </div>
      <div class="mcq-explanation" id="exp-${q.id}">
        <strong>💡 Explanation:</strong> ${escapeHtml(q.explanation || 'Refer to referenced lecture slide.')}
        <div style="margin-top:0.8rem;">
          <button class="btn btn-secondary btn-sm" onclick="explainLikeStuck(${q.id}, '${escapeHtml(q.topic || '')}')">
            👶 Explain Like I'm Stuck (ELIS)
          </button>
        </div>
      </div>
    </div>
  `).join("");
}

async function submitAnswer(questionId, selectedIdx, correctIdx) {
  const card = document.getElementById(`mcq-${questionId}`);
  const buttons = card.querySelectorAll(".option-btn");
  const exp = document.getElementById(`exp-${questionId}`);

  buttons.forEach(b => b.disabled = true);
  const isCorrect = (selectedIdx === correctIdx);

  if (isCorrect) {
    buttons[selectedIdx].classList.add("correct");
  } else {
    buttons[selectedIdx].classList.add("wrong");
    buttons[correctIdx].classList.add("correct");
  }

  exp.classList.add("visible");

  const formData = new FormData();
  formData.append("question_id", questionId);
  formData.append("selected_idx", selectedIdx);
  formData.append("is_correct", isCorrect);

  try {
    await apiFetch("/api/mcq/attempt", { method: "POST", body: formData });
    loadOverview();
  } catch (err) {
    console.error("Failed to record answer attempt:", err);
  }
}

async function explainLikeStuck(questionId, topic) {
  const modal = document.getElementById("stuckModal");
  const content = document.getElementById("stuckContent");
  modal.style.display = "flex";
  content.innerHTML = '<div class="loading-spinner">Simplifying principle & building analogy...</div>';

  const formData = new FormData();
  formData.append("question_id", questionId);
  formData.append("topic", topic);

  try {
    const data = await apiFetch("/api/explain_stuck", { method: "POST", body: formData });
    content.innerHTML = `
      <div class="elis-box">
        <h4>🎈 Simplified Concept</h4>
        <p>${escapeHtml(data.simple_explanation || '')}</p>
        <h4>🌍 Real-World Analogy</h4>
        <p>${escapeHtml(data.analogy || '')}</p>
        <h4>🎯 Key Rule to Remember</h4>
        <p>${escapeHtml(data.takeaway || '')}</p>
      </div>
    `;
  } catch (err) {
    content.textContent = "Could not generate simplification: " + err.message;
  }
}

// ==================== FLASHCARDS (SM-2) ====================
async function loadFlashcards() {
  flashcardRevisionModeActive = false;
  try {
    const data = await apiFetch(`/api/flashcards?course_id=${currentCourse}`);
    dueCards = data.cards || [];
    currentCardIdx = 0;
    renderFlashcard();
  } catch (err) {
    console.error("Failed to load flashcards:", err);
  }
}

async function loadAllFlashcardsForRevision() {
  flashcardRevisionModeActive = true;
  try {
    const data = await apiFetch(`/api/flashcards?course_id=${currentCourse}&mode=all`);
    dueCards = data.cards || [];
    currentCardIdx = 0;
    renderFlashcard();
  } catch (err) {
    console.error("Failed to load revision flashcards:", err);
  }
}

function renderFlashcard() {
  const card = document.getElementById("flashcard");
  const countEl = document.getElementById("cardCount");
  card.classList.remove("flipped");

  if (!dueCards || dueCards.length === 0) {
    document.getElementById("cardFront").textContent = "🎉 All caught up!";
    document.getElementById("cardBack").textContent = "No flashcards due right now.";
    document.getElementById("cardTopic").textContent = "Completed";
    countEl.textContent = "0 of 0";
    return;
  }

  const c = dueCards[currentCardIdx];
  document.getElementById("cardTopic").textContent = c.topic || "Concept";
  document.getElementById("cardFront").textContent = c.front;
  document.getElementById("cardBack").textContent = c.back;
  countEl.textContent = `${currentCardIdx + 1} of ${dueCards.length} ${flashcardRevisionModeActive ? '(Revision Mode)' : ''}`;
}

document.getElementById("flashcard").addEventListener("click", () => {
  document.getElementById("flashcard").classList.toggle("flipped");
});

document.querySelectorAll(".rating-btn").forEach(btn => {
  btn.addEventListener("click", async (e) => {
    e.stopPropagation();
    if (!dueCards || dueCards.length === 0) return;

    const rating = parseInt(btn.getAttribute("data-rating"));
    const card = dueCards[currentCardIdx];

    const formData = new FormData();
    formData.append("card_id", card.id);
    formData.append("rating", rating);

    try {
      await apiFetch("/api/flashcard/review", { method: "POST", body: formData });
    } catch (err) {
      console.error(err);
    }

    currentCardIdx++;
    if (currentCardIdx >= dueCards.length) {
      dueCards = [];
      renderFlashcard();
      loadOverview();
    } else {
      renderFlashcard();
    }
  });
});

// ==================== WEAK TOPICS RADAR ====================
async function loadWeakTopics() {
  const container = document.getElementById("weakTopicsContainer");
  container.innerHTML = '<div class="loading-spinner">Analyzing recall errors...</div>';

  try {
    const data = await apiFetch(`/api/weak_topics?course_id=${currentCourse}`);
    const topics = data.weak_topics || [];

    if (!topics || topics.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <p class="text-muted">✨ No weak topics detected yet! Complete more quizzes to calibrate radar.</p>
        </div>`;
      return;
    }

    container.innerHTML = topics.map(t => `
      <div class="glass-panel" style="margin-bottom:0.8rem; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <strong>${escapeHtml(t.topic)}</strong> (${escapeHtml(t.course_id)})
          <div class="text-muted" style="font-size:0.8rem;">
            Total Attempts: ${t.total_attempts} | Incorrect: ${t.incorrect_attempts}
          </div>
        </div>
        <div style="text-align:right;">
          <span class="badge badge-danger">${t.error_rate}% Error Rate</span>
          <div style="font-size:0.8rem; margin-top:0.2rem; color:var(--text-muted)">Priority: ${t.priority_score}</div>
        </div>
      </div>
    `).join("");
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Error: ${escapeHtml(err.message)}</div>`;
  }
}

document.getElementById("btnStartWeekendQuiz").addEventListener("click", async () => {
  const container = document.getElementById("weakTopicsContainer");
  container.innerHTML = '<div class="loading-spinner">Assembling targeted weak-topic recovery quiz...</div>';

  try {
    const data = await apiFetch(`/api/weekend_quiz?course_id=${currentCourse}`);
    const questions = data.questions || [];

    if (!questions || questions.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <h3>No weak-topic questions found</h3>
          <p class="text-muted">Complete more quizzes to identify weak areas first.</p>
        </div>`;
      return;
    }

    container.innerHTML = `
      <div style="margin-bottom: 1.5rem;">
        <span class="badge badge-accent">🎯 Targeted Weak-Topic Calibration (${questions.length} Questions)</span>
      </div>
      <div id="weekendQuizList"></div>
    `;

    renderMCQCards(questions, document.getElementById("weekendQuizList"));
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Error: ${escapeHtml(err.message)}</div>`;
  }
});

// ==================== EXAMS & MOCK ENGINE ====================
async function loadExamTab() {
  const container = document.getElementById("examListContainer");
  container.innerHTML = '<div class="loading-spinner">Loading exam schedule...</div>';

  try {
    const data = await apiFetch("/api/exams");
    const exams = data.exams || [];

    if (!exams || exams.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <p class="text-muted">No exams scheduled. Click '+ Add Exam' to track your midterm and final exam deadlines.</p>
        </div>`;
      return;
    }

    container.innerHTML = exams.map(ex => `
      <div class="glass-panel" style="margin-bottom: 1rem; display: flex; justify-content:space-between; align-items:center;">
        <div>
          <h3>${escapeHtml(ex.exam_title)} (${escapeHtml(ex.course_id)})</h3>
          <p class="text-muted">Exam Date: ${escapeHtml(ex.exam_date)} | Target: ${ex.target_score}%</p>
          <div style="margin-top:0.4rem;">
            <span class="badge badge-accent">${escapeHtml(ex.strategy_badge || ex.strategy || 'Normal')}</span>
          </div>
        </div>
        <div>
          <button class="btn btn-primary glow-button" onclick="launchMockExam('${escapeHtml(ex.course_id)}')">
            ⏱️ Launch Mock Exam
          </button>
        </div>
      </div>
    `).join("");
  } catch (err) {
    container.innerHTML = `<div class="empty-state">Error: ${escapeHtml(err.message)}</div>`;
  }
}

async function launchMockExam(courseId) {
  const modal = document.getElementById("mockExamModal");
  const content = document.getElementById("mockQuestionsContainer");
  modal.style.display = "flex";
  content.innerHTML = '<div class="loading-spinner">Assembling timed mock exam...</div>';

  try {
    const data = await apiFetch(`/api/mock_exam?course_id=${courseId}&question_count=15&time_limit_minutes=20`);
    const questions = data.questions || [];

    if (!questions || questions.length === 0) {
      content.innerHTML = '<p class="text-muted text-center">Not enough lecture questions to assemble a full mock exam.</p>';
      return;
    }

    let remainingSeconds = data.time_limit_minutes * 60;
    const timerDisplay = document.getElementById("mockTimerDisplay");

    if (mockTimerInterval) clearInterval(mockTimerInterval);
    mockTimerInterval = setInterval(() => {
      remainingSeconds--;
      const mins = Math.floor(remainingSeconds / 60);
      const secs = remainingSeconds % 60;
      timerDisplay.textContent = `⏱️ ${mins}:${secs < 10 ? '0' : ''}${secs}`;

      if (remainingSeconds <= 0) {
        clearInterval(mockTimerInterval);
        alert("⏰ Time's up! Submitting your mock exam answers.");
      }
    }, 1000);

    renderMCQCards(questions, content);
  } catch (err) {
    content.innerHTML = `<div class="empty-state">Error: ${escapeHtml(err.message)}</div>`;
  }
}

document.getElementById("btnCloseMockModal").addEventListener("click", () => {
  if (mockTimerInterval) clearInterval(mockTimerInterval);
  document.getElementById("mockExamModal").style.display = "none";
});

// ==================== AUDIO DIGESTS ====================
async function loadAudioDigests() {
  const container = document.getElementById("audioListContainer");
  try {
    const data = await apiFetch("/api/audio_digests");
    const digests = data.digests || [];

    if (!digests || digests.length === 0) {
      container.innerHTML = `
        <div class="glass-panel text-center">
          <p class="text-muted">No synthesized audio lecture digests yet. Run sync to generate.</p>
        </div>`;
      return;
    }

    container.innerHTML = digests.map(d => `
      <div class="audio-item">
        <strong>🎧 ${escapeHtml(d.lecture_title)}</strong>
        <p class="text-muted" style="font-size:0.8rem;">${escapeHtml(d.course_id)}</p>
        ${d.audio_path ? `
          <div class="audio-controls">
            <audio controls src="${API_BASE}/api/audio/play/${encodeURIComponent(d.audio_path.split('\\\\').pop().split('/').pop())}"></audio>
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
    const data = await apiFetch(`/api/cheatsheet?course_id=${course}`);
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
      const data = await apiFetch("/api/sync", { method: "POST", body: formData });
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
      const data = await apiFetch("/api/moodle/login", { method: "POST", body: formData });
      nustModal.style.display = "none";
      alert(`🎉 Connected to NUST LMS!\nDiscovered ${(data.enrolled_courses || []).length} courses: ${(data.enrolled_courses || []).join(", ")}\nIngested ${data.synced_files || 0} slide decks.`);
      loadOverview();
      loadCourses();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("NUST LMS Connection Error:\n\n" + err.message);
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
      await apiFetch("/api/upload_lecture", { method: "POST", body: formData });
      uploadModal.style.display = "none";
      alert("Lecture ingested successfully! High-quality study materials generated.");
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
      await apiFetch("/api/exams/add", { method: "POST", body: formData });
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

  // Delete Low-Quality MCQs and Flashcards
  document.getElementById("btnDeleteLowQuality").addEventListener("click", async () => {
    if (!confirm("This will permanently DELETE all template-generated or low-quality questions.\n\nOnly verified, high-quality questions will be kept. Continue?")) return;

    const btn = document.getElementById("btnDeleteLowQuality");
    btn.innerHTML = '<span class="btn-icon">⏳</span> Filtering...';
    btn.disabled = true;

    try {
      const data = await apiFetch(`/api/mcqs/heuristic?course_id=${currentCourse}`, { method: "DELETE" });
      alert(`✅ Cleanup Complete!\n\n🗑️ Filtered: ${data.deleted_mcqs || 0} low-quality MCQs\n🗑️ Filtered: ${data.deleted_flashcards || 0} low-quality flashcards\n\nOnly high-quality academic study content remains.`);
      loadOverview();
      loadMCQs();
      loadFlashcards();
    } catch (err) {
      alert("Cleanup failed: " + err.message);
    } finally {
      btn.innerHTML = '<span class="btn-icon">🗑️</span> Delete Low-Quality';
      btn.disabled = false;
    }
  });

  // AI Regeneration button — wipes old MCQs and calls Gemini for all lectures
  document.getElementById("btnRegenAI").addEventListener("click", async () => {
    if (!confirm("This will regenerate questions using Gemini AI from your lecture slides.\n\nThis will take a moment. Continue?")) return;

    const btn = document.getElementById("btnRegenAI");
    btn.innerHTML = '<span class="btn-icon">⏳</span> Generating...';
    btn.disabled = true;

    try {
      const data = await apiFetch("/api/regenerate_mcqs", { method: "POST" });
      alert(`✅ AI Generation Complete!\n\n📝 New MCQs: ${data.new_mcqs || 0}\n🗂️ New Flashcards: ${data.new_flashcards || 0}\n📁 Files processed: ${data.files_reprocessed || 0}`);
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
