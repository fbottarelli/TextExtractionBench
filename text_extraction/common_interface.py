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
