import json

from generation.llm_generator import LLMGenerator


class DummyResponse:
    def __init__(self, status_code, payload=None, text=""):
        self.status_code = status_code
        self._payload = payload or {}
        self.text = text or json.dumps(self._payload)

    def json(self):
        return self._payload


def test_generate_focused_mcqs_retries_next_model_after_400(monkeypatch):
    calls = []

    def fake_post(url, json, timeout):
        calls.append(url)
        if len(calls) == 1:
            return DummyResponse(400, {"error": "model not found"}, "model not found")
        return DummyResponse(
            200,
            {
                "candidates": [{
                    "content": {
                        "parts": [{
                            "text": json.dumps({
                                "mcqs": [{
                                    "q": "What is the primary concept?",
                                    "options": ["A", "B", "C", "D"],
                                    "answer": 0,
                                    "explanation": "The correct option matches the lecture.",
                                    "source": "Lecture 1, Slide 2",
                                    "topic": "Foundations"
                                }]
                            })
                        }]
                    }
                }]
            },
        )

    monkeypatch.setattr("requests.post", fake_post)

    generator = LLMGenerator(gemini_key="test-key")
    mcqs = generator.generate_focused_mcqs("some lecture text", course_id="CS-101", count=1)

    assert len(mcqs) == 1
    assert len(calls) >= 2
    assert mcqs[0]["generated_by"] == "ai"
