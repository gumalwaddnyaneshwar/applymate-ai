"""
ApplyMate AI - Utility Functions
"""
import pdfplumber
import PyPDF2
import io


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from an uploaded PDF file."""
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception:
        try:
            uploaded_file.seek(0)
            reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            return ""
    return text.strip()


def clean_text(text: str) -> str:
    return " ".join(text.split())


def truncate_text(text: str, max_chars: int = 4000) -> str:
    return text[:max_chars] if len(text) > max_chars else text
