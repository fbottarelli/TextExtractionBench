# pdfplumber_module.py
from text_extraction.common_interface import TextExtractionModule
import pdfplumber
from config import TEXT_EXTRACTION_CONFIG  # Import the configuration

class PDFPlumberExtractor(TextExtractionModule):
    def __init__(self):
        # Load pdfplumber specific configurations
        self.config = TEXT_EXTRACTION_CONFIG.get('pdfplumber', {})
    
    def extract_text(self, path):
        """Extract text from a PDF file using pdfplumber."""
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text was extracted
                    text += page_text + "\n"
        return text

