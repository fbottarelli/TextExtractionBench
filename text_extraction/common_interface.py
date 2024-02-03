# common_interface.py
from abc import ABC, abstractmethod

class TextExtractionModule(ABC):
    """
    Abstract base class for text extraction modules.
    All modules must implement the extract_text method.
    """

    @abstractmethod
    def extract_text(self, path):
        """
        Extract text from the document at the given path.

        :param path: Path to the document from which text is to be extracted.
        :return: Extracted text as a string.
        """
        pass

    @staticmethod
    def get_extractor(module_name, *args, **kwargs):
        """
        Factory method to get the appropriate extractor based on the module name.

        :param module_name: Name of the module to use for extraction.
        :return: Instance of the extractor.
        """
        if module_name == 'pdfplumber':
            from text_extraction.pdfplumber_module import PDFPlumberExtractor
            return PDFPlumberExtractor(*args, **kwargs)
        elif module_name == 'pytesseract':
            from text_extraction.pytesseract_module import TesseractPDFExtractor
            return TesseractPDFExtractor(*args, **kwargs)
        else:
            raise ValueError(f"Unknown module: {module_name}")
