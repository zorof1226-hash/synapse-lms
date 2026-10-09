import os
import json
import re
from typing import List, Dict, Any, Optional
from extraction.extractor import DocumentChunk
from config import GEMINI_API_KEY, OPENAI_API_KEY

STRICT_STUDY_PROMPT = """
You are an expert university professor and exam creator.
Analyze the following lecture chunks and generate high-yield study materials in strict JSON.

CRITICAL INSTRUCTIONS:
1. Grounding: Only use facts explicitly stated in the provided text. Never hallucinate.
2. Citations: Every MCQ and Short Answer must include the exact source citation (e.g. "{lecture_title}, Slide 4").
3. Question Quality: MCQs must have exactly 4 plausible options, with strictly ONE unambiguously correct answer.
4. Generate at least 10 MCQs and 15 flashcards. More is better.
5. Output Schema: You MUST respond ONLY with valid, parseable JSON matching this schema:
{{
  "summary": "High-level 2-3 paragraph summary synthesizing the lecture core themes.",
  "key_terms": [
    {{"term": "Term Name", "definition": "Clear concise definition grounded in the lecture."}}
  ],
  "mcqs": [
    {{
      "q": "Precise conceptual or analytical question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": 0,
      "explanation": "Detailed explanation of why the correct option is right and others are wrong.",
      "source": "Lec X, Slide Y",
      "topic": "Specific Subtopic"
    }}
  ],
  "flashcards": [
    {{"front": "Prompt or Question", "back": "Direct answer or formula", "topic": "Specific Subtopic"}}
  ],
  "short_answer": [
    {{"q": "Short open-ended conceptual question?", "model_answer": "Complete answer with key grading criteria.", "source": "Lec X, Slide Y"}}
  ]
}}

LECTURE CHUNKS:
{{chunks_text}}
"""

MCQ_FOCUSED_PROMPT = """
You are an expert university professor and exam creator for {course_id}.
Analyze the following lecture content and generate exactly {count} high-yield, conceptual multiple choice questions in strict JSON.

CRITICAL INSTRUCTIONS:
1. Grounding: Only test facts, mechanisms, formulas, and concepts explicitly stated in the provided text. Never hallucinate.
2. Question Quality: Each MCQ must test deep conceptual understanding, analytical thinking, or problem-solving.
3. Options: Provide exactly 4 plausible, distinct options. Strictly ONE unambiguously correct answer.
4. Explanations: Detail why the correct option is right and clarify the core principle.
5. Citations: Include the exact source/slide reference whenever available.

Output Schema: Respond ONLY with valid, parseable JSON matching this schema:
{{
  "mcqs": [
    {{
      "q": "Precise conceptual or analytical question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": 0,
      "explanation": "Detailed explanation of why the correct option is right.",
      "source": "Slide / Section reference",
      "topic": "Specific Topic Name"
    }}
  ]
}}

LECTURE CONTENT:
{chunks_text}
"""

GEMINI_MODEL_CANDIDATES = [
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-2.5-flash",
    "gemini-pro-latest",
]

def _clean_and_parse_json(raw_text: str) -> Dict[str, Any]:
    """Safely extracts and parses JSON even if wrapped in markdown fences or malformed."""
    text = (raw_text or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"(\{.*\})", text, re.DOTALL)
        if m:
            candidate = m.group(1)
            candidate = re.sub(r",\s*([\]\}])", r"\1", candidate)
            try:
                return json.loads(candidate)
            except Exception:
                pass
        raise

def _build_prompt(lecture_title: str, chunks_text: str) -> str:
    """Build the generation prompt with proper substitution."""
    return (STRICT_STUDY_PROMPT
            .replace("{{chunks_text}}", chunks_text[:35000])
            .replace("{lecture_title}", lecture_title)
            .replace("{{", "{").replace("}}", "}"))


class LLMGenerator:
    """Generates strictly structured study materials (MCQs, flashcards, key terms, summary)
    using Gemini, OpenAI, or a robust offline NLP heuristic engine.
    """

    def __init__(self, gemini_key: str = None, openai_key: str = None):
        import config
        self.gemini_key = gemini_key or config.GEMINI_API_KEY
        self.openai_key = openai_key or config.OPENAI_API_KEY

    def generate_focused_mcqs(self, chunks_text: str, course_id: str = "Course", count: int = 10) -> List[Dict[str, Any]]:
        """Generates a focused batch of N MCQs (default 10) from lecture text using AI."""
        if not chunks_text or not chunks_text.strip():
            return []

        import config
        self.gemini_key = self.gemini_key or config.GEMINI_API_KEY
        self.openai_key = self.openai_key or config.OPENAI_API_KEY

        prompt = (MCQ_FOCUSED_PROMPT
                  .replace("{count}", str(count))
                  .replace("{course_id}", course_id)
                  .replace("{chunks_text}", chunks_text[:35000]))

        # Try Gemini
        if self.gemini_key:
            try:
                import requests
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"response_mime_type": "application/json"}
                }
                for model in GEMINI_MODEL_CANDIDATES:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.gemini_key}"
                    resp = requests.post(url, json=payload, timeout=45)
                    if resp.status_code == 200:
                        data = resp.json()
                        raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
                        parsed = json.loads(raw_text)
                        mcqs = parsed.get("mcqs", [])
                        for q in mcqs:
                            q["generated_by"] = "ai"
                        print(f"[LLMGenerator] Successfully generated {len(mcqs)} MCQs with {model}")
                        return mcqs
                    elif resp.status_code == 400:
                        error_text = (resp.text or "").lower()
                        if any(token in error_text for token in ["api key", "invalid", "forbidden", "permission"]):
                            print(f"[LLMGenerator] Gemini API key invalid (400): {resp.text[:150]}")
                            break
                    elif resp.status_code in (429, 503):
                        print(f"[LLMGenerator] Gemini model {model} rate limited or overloaded ({resp.status_code}), trying next model...")
                        continue
                    elif resp.status_code == 404:
                        print(f"[LLMGenerator] Gemini model {model} not available (404), trying next model...")
                        continue
            except Exception as e:
                print(f"[LLMGenerator] Gemini focused MCQ error: {e}")

        # Try OpenAI
        if self.openai_key:
            try:
                import requests
                url = "https://api.openai.com/v1/chat/completions"
                headers = {"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"}
                payload = {
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": "You output only valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    "response_format": {"type": "json_object"}
                }
                resp = requests.post(url, headers=headers, json=payload, timeout=45)
                if resp.status_code == 200:
                    content = resp.json()["choices"][0]["message"]["content"]
                    parsed = json.loads(content)
                    mcqs = parsed.get("mcqs", [])
                    for q in mcqs:
                        q["generated_by"] = "ai"
                    return mcqs
            except Exception as e:
                print(f"[LLMGenerator] OpenAI focused MCQ error: {e}")

        return []

    def generate_study_package(self, chunks: List[DocumentChunk], course_id: str, lecture_title: str) -> Dict[str, Any]:
        """Runs the generation pipeline, falling back gracefully if no API key is set."""
        if not chunks:
            return self._empty_package(lecture_title)

        # 1. Format chunks text for prompt
        chunks_text = "\n\n".join([
            f"--- [{c.source_tag}] {c.heading} ---\n{c.text}"
            for c in chunks
        ])

        # Try Gemini API if key is available
        if self.gemini_key:
            try:
                res = self._call_gemini(chunks_text, lecture_title)
                if res and "mcqs" in res:
                    # Tag as AI-generated
                    for q in res.get("mcqs", []):
                        q.setdefault("generated_by", "ai")
                    for fc in res.get("flashcards", []):
                        fc.setdefault("generated_by", "ai")
                    return res
            except Exception as e:
                print(f"[LLMGenerator] Gemini API error: {e}. Falling back...")

        # Try OpenAI API if key is available
        if self.openai_key:
            try:
                res = self._call_openai(chunks_text, lecture_title)
                if res and "mcqs" in res:
                    # Tag as AI-generated
                    for q in res.get("mcqs", []):
                        q.setdefault("generated_by", "ai")
                    for fc in res.get("flashcards", []):
                        fc.setdefault("generated_by", "ai")
                    return res
            except Exception as e:
                print(f"[LLMGenerator] OpenAI API error: {e}. Falling back...")

        # Fallback: High-quality rule-based heuristic generation engine
        print(f"[LLMGenerator] Using robust offline generator for {lecture_title}")
        return self._generate_heuristic(chunks, course_id, lecture_title)

    def _call_gemini(self, chunks_text: str, lecture_title: str) -> Optional[Dict[str, Any]]:
        import requests, time
        self.gemini_key = os.getenv("GEMINI_API_KEY", self.gemini_key)
        prompt = _build_prompt(lecture_title, chunks_text)
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"response_mime_type": "application/json"}
        }
        for model in GEMINI_MODEL_CANDIDATES:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.gemini_key}"
            for attempt in range(4):
                try:
                    resp = requests.post(url, json=payload, timeout=90)
                    if resp.status_code == 200:
                        data = resp.json()
                        raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
                        try:
                            parsed = _clean_and_parse_json(raw_text)
                            print(f"[LLMGenerator] Gemini success with model: {model}")
                            return parsed
                        except Exception as parse_err:
                            print(f"[LLMGenerator] JSON parse error from {model}: {parse_err}, trying next model candidate...")
                            break
                    elif resp.status_code == 400:
                        error_text = (resp.text or "").lower()
                        if any(token in error_text for token in ["api key", "invalid", "forbidden", "permission"]):
                            print(f"[LLMGenerator] Gemini API key is invalid (400): {resp.text[:200]}")
                            return None
                        print(f"[LLMGenerator] Gemini model {model} rejected request (400): {resp.text[:200]}")
                        break
                    elif resp.status_code == 429:
                        print(f"[LLMGenerator] {model} rate limited or quota exceeded (429), trying next model candidate...")
                        break
                    elif resp.status_code == 503:
                        print(f"[LLMGenerator] {model} overloaded (503), trying next model candidate...")
                        break
                    elif resp.status_code == 404:
                        print(f"[LLMGenerator] {model} not available (404), trying next model...")
                        break
                    else:
                        print(f"[LLMGenerator] Gemini HTTP {resp.status_code} ({model}): {resp.text[:200]}, trying next model...")
                        break
                except requests.exceptions.Timeout:
                    print(f"[LLMGenerator] {model} timed out, retrying...")
                    time.sleep(2)
                except Exception as e:
                    print(f"[LLMGenerator] Error with {model}: {e}")
                    break
        raise RuntimeError("All Gemini models failed or are unavailable.")



    def _call_openai(self, chunks_text: str, lecture_title: str) -> Optional[Dict[str, Any]]:
        import requests
        url = "https://api.openai.com/v1/chat/completions"
        prompt = _build_prompt(lecture_title, chunks_text)
        headers = {"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"}
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=45)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        return json.loads(content)

    def explain_stuck(self, question: str, correct_option: str, user_option: str, explanation: str) -> Dict[str, str]:
        """'Explain like I'm stuck' generator: provides simplified analogy and breakdown."""
        prompt = (
            f"Question: {question}\n"
            f"User chose: {user_option}\n"
            f"Correct answer: {correct_option}\n"
            f"Original explanation: {explanation}\n\n"
            "Explain this to a student who is completely stuck. "
            "1. Give a simple 5-year-old style intuitive breakdown.\n"
            "2. Give a memorable real-world analogy.\n"
            "3. State the exact 'aha!' mental model to never get this wrong again."
        )

        if self.gemini_key:
            try:
                import requests
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.gemini_key}"
                resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
                if resp.status_code == 200:
                    text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
                    return {"simple_explanation": text}
            except Exception:
                pass

        # Robust offline fallback breakdown
        return {
            "simple_explanation": (
                f"💡 Intuitive Breakdown:\n"
                f"You picked '{user_option}', but '{correct_option}' is the true answer. "
                f"Here is the key distinction: {explanation}\n\n"
                f"🚗 Real-world Analogy:\n"
                f"Think of this like an express highway vs a local street. '{user_option}' is what happens on the side roads, "
                f"whereas '{correct_option}' represents the foundational rule that controls the whole intersection.\n\n"
                f"🎯 Mental Hook:\n"
                f"Whenever you encounter this topic, remember: always verify the core definition first!"
            )
        }

    def _generate_heuristic(self, chunks: List[DocumentChunk], course_id: str, lecture_title: str) -> Dict[str, Any]:
        """High-yield heuristic study generator built for local execution without API keys."""
        all_text = " ".join([c.text for c in chunks])
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", all_text) if len(s.strip()) > 30]

        # Extract definitions and key concepts
        key_terms = []
        mcqs = []
        flashcards = []
        short_answers = []

        seen_terms = set()
        for chunk in chunks:
            lines = [l.strip() for l in chunk.text.splitlines() if l.strip()]
            for line in lines:
                # Look for definitions "X is Y", "X refers to Y", "X: Y"
                match = re.match(r"^([A-Z][A-Za-z0-9\s\-]{2,30})[:\—\-]\s*(.{20,})", line)
                if not match:
                    match = re.match(r"^([A-Z][A-Za-z0-9\s\-]{2,30})\s+(?:is defined as|refers to|means|is a)\s+(.{20,})", line, re.IGNORECASE)

                if match:
                    term = match.group(1).strip()
                    definition = match.group(2).strip()
                    if term.lower() not in seen_terms and len(term.split()) <= 4:
                        seen_terms.add(term.lower())
                        key_terms.append({"term": term, "definition": definition[:200]})
                        flashcards.append({
                            "front": f"What is {term}?",
                            "back": definition[:250],
                            "topic": chunk.heading,
                            "generated_by": "heuristic"
                        })

        # Ensure at least 5 key terms
        if len(key_terms) < 5:
            for chunk in chunks:
                if chunk.heading and chunk.heading not in seen_terms and len(chunk.heading) > 4:
                    seen_terms.add(chunk.heading.lower())
                    key_terms.append({
                        "term": chunk.heading,
                        "definition": chunk.text[:180].replace("\n", " ") + "..."
                    })
                    flashcards.append({
                        "front": f"Explain the principle of {chunk.heading}",
                        "back": chunk.text[:220].replace("\n", " "),
                        "topic": chunk.heading,
                        "generated_by": "heuristic"
                    })

        # Build MCQs from chunk headings and statements
        for idx, chunk in enumerate(chunks[:12]):
            heading = chunk.heading or f"Concept {idx+1}"
            first_sentence = chunk.text.split(".")[0].strip() if "." in chunk.text else chunk.text[:100]
            if len(first_sentence) < 15:
                continue

            question = f"According to {chunk.source_tag}, what is the primary role or definition associated with {heading}?"
            correct_ans = first_sentence[:120]
            distractor1 = f"It replaces {heading} entirely to avoid computational overhead."
            distractor2 = f"It operates as a deprecated secondary mechanism only."
            distractor3 = f"It is only applicable in unconstrained, static environments."

            options = [correct_ans, distractor1, distractor2, distractor3]
            # Deterministic rotation so answer isn't always 0
            ans_idx = idx % 4
            options[0], options[ans_idx] = options[ans_idx], options[0]

            mcqs.append({
                "q": question,
                "options": options,
                "answer": ans_idx,
                "explanation": f"Grounded in {chunk.source_tag}: '{first_sentence}'.",
                "source": chunk.source_tag,
                "topic": heading,
                "generated_by": "heuristic"
            })

            if len(mcqs) >= 10:
                break

        # Short answers
        for chunk in chunks[:4]:
            short_answers.append({
                "q": f"Summarize the core mechanism of {chunk.heading} and how it applies to {course_id}.",
                "model_answer": f"Based on {chunk.source_tag}: {chunk.text[:250]}",
                "source": chunk.source_tag
            })

        summary = (
            f"This lecture on '{lecture_title}' covers key fundamentals across {len(chunks)} slides/sections. "
            f"Major themes include {', '.join([c.heading for c in chunks[:4]])}. "
            f"Mastery of these concepts is crucial for upcoming course assessments."
        )

        return {
            "summary": summary,
            "key_terms": key_terms[:10],
            "mcqs": mcqs,
            "flashcards": flashcards[:15],
            "short_answer": short_answers
        }

    def _empty_package(self, lecture_title: str) -> Dict[str, Any]:
        return {
            "summary": f"No extractable text found for {lecture_title}.",
            "key_terms": [],
            "mcqs": [],
            "flashcards": [],
            "short_answer": []
        }
