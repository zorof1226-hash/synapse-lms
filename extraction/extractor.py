import re
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

try:
    from pptx import Presentation
except ImportError:
    Presentation = None

class DocumentChunk:
    def __init__(self, course_id: str, lecture_title: str, slide_num: int, heading: str, text: str, source_tag: str):
        self.course_id = course_id
        self.lecture_title = lecture_title
        self.slide_num = slide_num
        self.heading = heading
        self.text = text
        self.source_tag = source_tag

    def to_dict(self) -> Dict[str, Any]:
        return {
            "course_id": self.course_id,
            "lecture_title": self.lecture_title,
            "slide_num": self.slide_num,
            "heading": self.heading,
            "text": self.text,
            "source_tag": self.source_tag
        }

class DocumentExtractor:
    """Extracts slide-by-slide or page-by-page text chunks from PDF, PPTX, or text files,
    preserving exact page/slide citations (e.g. 'Lec 3, Slide 12').
    """

    def __init__(self):
        pass

    def extract_file(self, file_path: Path, course_id: str = "General", lecture_title: Optional[str] = None) -> List[DocumentChunk]:
        suffix = file_path.suffix.lower()
        title = lecture_title or file_path.stem

        if suffix == ".pdf":
            return self._extract_pdf(file_path, course_id, title)
        elif suffix in (".pptx", ".ppt"):
            return self._extract_pptx(file_path, course_id, title)
        elif suffix in (".txt", ".md"):
            return self._extract_text(file_path, course_id, title)
        else:
            return []

    def _extract_pdf(self, file_path: Path, course_id: str, lecture_title: str) -> List[DocumentChunk]:
        chunks = []
        if not fitz:
            # Fallback if fitz is not found
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            chunks.append(DocumentChunk(course_id, lecture_title, 1, lecture_title, text, f"{lecture_title}, Page 1"))
            return chunks

        doc = fitz.open(str(file_path))
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            page_num = page_idx + 1
            page_text = page.get_text().strip()
            if not page_text:
                continue

            # Identify a potential slide/section heading from the first non-empty line
            lines = [l.strip() for l in page_text.splitlines() if l.strip()]
            heading = lines[0] if lines else f"Page {page_num}"
            source_tag = f"{lecture_title}, p.{page_num}"

            chunks.append(DocumentChunk(
                course_id=course_id,
                lecture_title=lecture_title,
                slide_num=page_num,
                heading=heading[:80],
                text=page_text,
                source_tag=source_tag
            ))
        doc.close()
        return chunks

    def _extract_pptx(self, file_path: Path, course_id: str, lecture_title: str) -> List[DocumentChunk]:
        chunks = []
        if not Presentation:
            return chunks

        try:
            prs = Presentation(str(file_path))
            for slide_idx, slide in enumerate(prs.slides):
                slide_num = slide_idx + 1
                texts = []
                heading = f"Slide {slide_num}"

                if slide.shapes.title and slide.shapes.title.text.strip():
                    heading = slide.shapes.title.text.strip()

                for shape in slide.shapes:
                    if hasattr(shape, "text") and shape.text.strip():
                        texts.append(shape.text.strip())

                if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
                    notes = slide.notes_slide.notes_text_frame.text.strip()
                    if notes:
                        texts.append(f"[Presenter Notes: {notes}]")

                combined_text = "\n".join(texts).strip()
                if not combined_text:
                    continue

                source_tag = f"{lecture_title}, Slide {slide_num}"
                chunks.append(DocumentChunk(
                    course_id=course_id,
                    lecture_title=lecture_title,
                    slide_num=slide_num,
                    heading=heading[:80],
                    text=combined_text,
                    source_tag=source_tag
                ))
            return chunks
        except Exception as e:
            print(f"[DocumentExtractor] PPTX parsing error for {file_path.name} ({e}). Attempting raw text extraction...")
            # Fallback for legacy .ppt or uncompressed files: extract readable ASCII strings
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                import re
                words = re.findall(rb"[a-zA-Z0-9\s.,;:\-'\"]{4,}", content)
                decoded = [w.decode("latin1", errors="ignore").strip() for w in words if len(w.strip()) > 3]
                full_text = " ".join(decoded[:500])
                if full_text:
                    chunks.append(DocumentChunk(
                        course_id=course_id,
                        lecture_title=lecture_title,
                        slide_num=1,
                        heading=lecture_title,
                        text=full_text,
                        source_tag=f"{lecture_title}, Slide 1"
                    ))
            except Exception as ex:
                print(f"[DocumentExtractor] Raw fallback also failed: {ex}")
            return chunks

    def _extract_text(self, file_path: Path, course_id: str, lecture_title: str) -> List[DocumentChunk]:
        chunks = []
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Split on markdown headers (# or ##)
        sections = re.split(r"\n(?=#{1,3}\s+)", content)
        for idx, sec in enumerate(sections):
            sec_clean = sec.strip()
            if not sec_clean:
                continue
            lines = sec_clean.splitlines()
            first_line = lines[0].lstrip("#").strip() if lines else f"Section {idx+1}"
            source_tag = f"{lecture_title}, Sec {idx+1}"

            chunks.append(DocumentChunk(
                course_id=course_id,
                lecture_title=lecture_title,
                slide_num=idx + 1,
                heading=first_line[:80],
                text=sec_clean,
                source_tag=source_tag
            ))
        return chunks
