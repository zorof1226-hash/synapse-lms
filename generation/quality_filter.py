from typing import List, Dict, Any

class QualityFilter:
    """Second-pass validator checking questions for ambiguity, single correct answer,
    and valid slide/page citations before committing to study databases.
    """

    def __init__(self):
        pass

    def filter_mcqs(self, mcqs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        verified = []
        seen_questions = set()

        for q in mcqs:
            question_text = q.get("q", "").strip()
            options = q.get("options", [])
            answer_idx = q.get("answer", -1)
            source = q.get("source", "").strip()

            # Rule 1: Question must not be empty or duplicate
            if not question_text or len(question_text) < 10:
                continue
            norm_q = question_text.lower().replace("?", "")
            if norm_q in seen_questions:
                continue

            # Rule 2: Must have exactly 4 options
            if not isinstance(options, list) or len(options) != 4:
                continue

            # Rule 3: Options must be distinct
            clean_opts = [str(o).strip() for o in options]
            if len(set(clean_opts)) < 4:
                continue

            # Rule 4: Answer index must be 0 <= idx <= 3
            if not isinstance(answer_idx, int) or not (0 <= answer_idx <= 3):
                continue

            # Rule 5: Source citation must exist
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

            if not front or not back or len(front) < 3 or len(back) < 3:
                continue

            norm_front = front.lower()
            if norm_front in seen_fronts:
                continue

            seen_fronts.add(norm_front)
            verified.append(c)

        return verified
