# pytesseract_module.py
from text_extraction.common_interface import TextExtractionModule
import pytesseract
from pdf2image import convert_from_path

class TesseractPDFExtractor(TextExtractionModule):
    def extract_text(self, path):
        """Extract text from a PDF file by converting its pages to images and using pytesseract."""
        text = ""
        # Convert PDF pages to images
        pages = convert_from_path(path)
        for page in pages:
            page_text = pytesseract.image_to_string(page)
            text += page_text + "\n"
        return text

