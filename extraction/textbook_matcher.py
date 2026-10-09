import re
from pathlib import Path
from typing import List, Dict, Any, Tuple
import math
from collections import Counter

class TextbookChapter:
    def __init__(self, chapter_title: str, chapter_num: str, text: str, start_page: int, end_page: int):
        self.chapter_title = chapter_title
        self.chapter_num = chapter_num
        self.text = text
        self.start_page = start_page
        self.end_page = end_page

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chapter_title": self.chapter_title,
            "chapter_num": self.chapter_num,
            "start_page": self.start_page,
            "end_page": self.end_page,
            "word_count": len(self.text.split())
        }

class TextbookMatcher:
    """Handles splitting large textbook PDFs by chapter, and matching lecture topics
    to relevant textbook sections using TF-IDF / keyword similarity.
    """

    def __init__(self):
        pass

    def extract_chapters_from_pdf(self, pdf_path: Path) -> List[TextbookChapter]:
        chapters = []
        try:
            import fitz
            doc = fitz.open(str(pdf_path))
            toc = doc.get_toc() # [[lvl, title, page], ...]

            if toc and len(toc) > 2:
                # Level 1 or 2 entries
                filtered = [item for item in toc if item[0] in (1, 2)]
                for i in range(len(filtered)):
                    title = filtered[i][1]
                    start_page = filtered[i][2]
                    end_page = filtered[i+1][2] - 1 if i + 1 < len(filtered) else len(doc)
                    if end_page < start_page:
                        end_page = start_page

                    chapter_text = []
                    for p in range(start_page - 1, min(end_page, len(doc))):
                        chapter_text.append(doc[p].get_text())

                    chap_num_match = re.search(r"(?:Chapter|Section|Ch\.?)\s*([0-9A-Za-z\.]+)", title, re.IGNORECASE)
                    chap_num = chap_num_match.group(1) if chap_num_match else str(i + 1)

                    chapters.append(TextbookChapter(
                        chapter_title=title,
                        chapter_num=chap_num,
                        text="\n".join(chapter_text),
                        start_page=start_page,
                        end_page=end_page
                    ))
            else:
                # Fallback: scan for "Chapter X" in text
                current_chap_title = "Introduction"
                current_chap_num = "1"
                current_pages = []
                start_p = 1

                for page_idx in range(len(doc)):
                    p_num = page_idx + 1
                    txt = doc[page_idx].get_text()
                    chap_match = re.search(r"^(?:Chapter|CHAPTER)\s+([0-9IVXLCDM]+)[:\.\s]*(.*)", txt, re.MULTILINE)
                    if chap_match and page_idx > 0:
                        if current_pages:
                            chapters.append(TextbookChapter(
                                chapter_title=current_chap_title,
                                chapter_num=current_chap_num,
                                text="\n".join(current_pages),
                                start_page=start_p,
                                end_page=p_num - 1
                            ))
                        current_chap_num = chap_match.group(1)
                        current_chap_title = chap_match.group(0).strip()
                        current_pages = [txt]
                        start_p = p_num
                    else:
                        current_pages.append(txt)

                if current_pages:
                    chapters.append(TextbookChapter(
                        chapter_title=current_chap_title,
                        chapter_num=current_chap_num,
                        text="\n".join(current_pages),
                        start_page=start_p,
                        end_page=len(doc)
                    ))
            doc.close()
        except Exception as e:
            print(f"[TextbookMatcher] Error splitting textbook: {e}")

        return chapters

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        words = re.findall(r"[a-zA-Z]{3,}", text.lower())
        stop_words = {
            "the", "and", "this", "that", "with", "from", "for", "have", "are", "which",
            "not", "can", "has", "but", "their", "more", "also", "will", "all", "its"
        }
        return [w for w in words if w not in stop_words]

    def find_relevant_chapters(self, lecture_text: str, chapters: List[TextbookChapter], top_k: int = 2) -> List[Dict[str, Any]]:
        """Calculate keyword similarity between a lecture and textbook chapters."""
        if not chapters:
            return []

        lecture_words = self._tokenize(lecture_text)
        lec_counter = Counter(lecture_words)
        lec_norm = math.sqrt(sum(v * v for v in lec_counter.values())) or 1.0

        scored = []
        for ch in chapters:
            ch_words = self._tokenize(ch.text[:50000])  # sample first 50k chars for speed
            ch_counter = Counter(ch_words)
            ch_norm = math.sqrt(sum(v * v for v in ch_counter.values())) or 1.0

            # Cosine similarity
            common = set(lec_counter.keys()) & set(ch_counter.keys())
            dot = sum(lec_counter[w] * ch_counter[w] for w in common)
            similarity = dot / (lec_norm * ch_norm)

            top_terms = [word for word, count in sorted([(w, lec_counter[w] * ch_counter[w]) for w in common], key=lambda x: x[1], reverse=True)[:5]]

            scored.append({
                "chapter_title": ch.chapter_title,
                "chapter_num": ch.chapter_num,
                "start_page": ch.start_page,
                "end_page": ch.end_page,
                "score": round(similarity * 100, 2),
                "matched_topics": top_terms,
                "reading_recommendation": f"Read Chapter {ch.chapter_num}: '{ch.chapter_title}' (pp. {ch.start_page}–{ch.end_page})"
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
