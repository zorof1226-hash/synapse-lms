import re
from typing import List, Dict, Any

ADMIN_KEYWORDS = [
    r"\bcourse\s*outline\b",
    r"\bsyllabus\b",
    r"\bcourse\s*code\b",
    r"\binstructor\b",
    r"\bprofessor\b",
    r"\boffice\s*hour",
    r"\bcredit\s*hour",
    r"\bgrading\s*polic",
    r"\bgrading\s*criteri",
    r"\bweightage\b",
    r"\bprerequisite\b",
    r"\btextbook\s*edition\b",
    r"\bcontact\s*email\b",
    r"\bdepartment\b",
    r"\buniversity\b",
    r"\bpassing\s*criteri",
    r"\battendance\s*polic",
    r"\blate\s*polic",
    r"\bcover\s*page\b",
    r"\bsubmission\s*deadlin",
    r"\bassignment\s*due\b",
    r"\blab\s*polic",
    r"\blab\s*manual\b",
    r"\bsemester\b",
    r"\bclass\s*timing",
]

TRIVIAL_STEM_PATTERNS = [
    r"^according to slide\s*\d+",
    r"^as (?:stated|shown|discussed) (?:on|in) slide\s*\d+",
    r"^the title of this (?:lecture|presentation|slide)",
    r"^what is the name of this (?:course|lecture)",
    r"^welcome to\b",
    r"^in this lecture we will\b",
    r"^table of contents\b",
    r"^any questions\b",
]

ABSURD_DISTRACTOR_PATTERNS = [
    r"to avoid computational overhead",
    r"replaces .* entirely",
    r"operates as a deprecated secondary mechanism",
    r"is only applicable in unconstrained",
    r"quantum mechanics",  # Common hallucinated absurdity in non-physics classes
    r"none of the above",
    r"all of the above",
    r"both a and b",
]

ADMIN_CARD_PATTERNS = [
    r"course code",
    r"instructor",
    r"professor",
    r"office hour",
    r"grading",
    r"credit hour",
    r"syllabus",
    r"prerequisite",
    r"textbook",
    r"attendance",
    r"deadline",
    r"due date",
    r"^agenda\b",
    r"^overview\b",
    r"^summary\b",
    r"^table of contents\b",
    r"^references\b",
    r"^questions\?\b",
    r"^introduction\b",
    r"^lecture outline\b",
]

class QualityFilter:
    """Rigorous multi-layer quality validator ensuring only high-yield, academically
    relevant, conceptual MCQs and flashcards are admitted to the study database.
    Eliminates administrative trivia, trivial slide headings, and nonsense distractors.
    """

    def __init__(self):
        pass

    def is_administrative_text(self, text: str) -> bool:
        """Checks if text contains course logistics or administrative trivia."""
        text_lower = text.lower()
        return any(re.search(pat, text_lower) for pat in ADMIN_KEYWORDS)

    def is_trivial_stem(self, stem: str) -> bool:
        """Checks if question stem is superficial slide-number trivia."""
        stem_lower = stem.lower().strip()
        return any(re.search(pat, stem_lower) for pat in TRIVIAL_STEM_PATTERNS)

    def filter_mcqs(self, mcqs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        verified = []
        seen_questions = set()

        for q in mcqs:
            question_text = q.get("q", "").strip()
            options = q.get("options", [])
            answer_idx = q.get("answer", -1)
            source = q.get("source", "").strip()

            # Rule 1: Question text length & non-empty
            if not question_text or len(question_text) < 20:
                continue

            # Rule 2: Reject administrative/syllabus questions
            if self.is_administrative_text(question_text):
                continue

            # Rule 3: Reject trivial presentation stems ("According to Slide 1...")
            if self.is_trivial_stem(question_text):
                continue

            # Rule 4: Deduplication
            norm_q = re.sub(r"[^\w\s]", "", question_text.lower()).strip()
            if norm_q in seen_questions:
                continue

            # Rule 5: Exactly 4 options required
            if not isinstance(options, list) or len(options) != 4:
                continue

            # Rule 6: Options must be distinct, non-trivial, and substantive
            clean_opts = [str(o).strip() for o in options]
            if len(set(clean_opts)) < 4:
                continue

            # Every option must be at least 3 characters
            if any(len(o) < 3 for o in clean_opts):
                continue

            # Rule 7: Reject joke or template heuristic distractors
            has_absurd = False
            for opt in clean_opts:
                opt_lower = opt.lower()
                if any(re.search(pat, opt_lower) for pat in ABSURD_DISTRACTOR_PATTERNS):
                    has_absurd = True
                    break
            if has_absurd:
                continue

            # Rule 8: Answer index must be valid (0 <= idx <= 3)
            if not isinstance(answer_idx, int) or not (0 <= answer_idx <= 3):
                continue

            # Rule 9: Ensure option length balance (avoid trivial giveaway where correct option is 10x longer)
            opt_lens = [len(o) for o in clean_opts]
            max_len = max(opt_lens)
            min_len = min(opt_lens)
            # If one option is 150+ chars and min is under 6 chars, likely giveaway
            if max_len > 150 and min_len < 6:
                continue

            # Rule 10: Citation
            if not source:
                q["source"] = "Lecture Notes"

            seen_questions.add(norm_q)
            verified.append(q)

        return verified

    def filter_flashcards(self, cards: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        verified = []
        seen_fronts = set()

        for c in cards:
            front = c.get("front", "").strip()
            back = c.get("back", "").strip()

            # Rule 1: Front and back minimum length
            if not front or not back or len(front) < 10 or len(back) < 12:
                continue

            front_lower = front.lower()

            # Rule 2: Reject administrative or slide navigation flashcards
            if any(re.search(pat, front_lower) for pat in ADMIN_CARD_PATTERNS):
                continue
            if self.is_administrative_text(front) or self.is_administrative_text(back):
                continue

            # Rule 3: Deduplication
            norm_front = re.sub(r"[^\w\s]", "", front_lower).strip()
            if norm_front in seen_fronts:
                continue

            seen_fronts.add(norm_front)
            verified.append(c)

        return verified
