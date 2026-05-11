import os
import PyPDF2
import docx
from typing import List, Dict, Any
from .logger import logger
from .utils import get_file_extension

class DocumentLoader:
    """Handles extraction of text from various file formats."""
    
    def __init__(self):
        self.supported_extensions = {'.pdf', '.docx', '.txt'}

    def load(self, file_path: str) -> str:
        """Load document content based on extension."""
        ext = get_file_extension(file_path)
        
        if ext == '.pdf':
            return self._load_pdf(file_path)
        elif ext == '.docx':
            return self._load_docx(file_path)
        elif ext == '.txt':
            return self._load_txt(file_path)
        else:
            logger.error(f"Unsupported file format: {ext}")
            raise ValueError(f"Unsupported file format: {ext}")

    def _load_pdf(self, file_path: str) -> str:
        text = ""
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"
            return text
        except Exception as e:
            logger.error(f"Error reading PDF {file_path}: {str(e)}")
            return ""

    def _load_docx(self, file_path: str) -> str:
        try:
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            logger.error(f"Error reading DOCX {file_path}: {str(e)}")
            return ""

    def _load_txt(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading TXT {file_path}: {str(e)}")
            return ""
