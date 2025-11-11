import fitz  # PyMuPDF
import docx
import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text content from a PDF using pdfplumber.
    Returns a clean string of all text.
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}"
