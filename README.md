# TextExtractionBench
## Overview
Little framework for testing various text extraction techniques from documents using different Python libraries and techniques.
It will supports a range of libraries for extracting text from different document types, including PDFs, images, Word documents, and more, using both OCR (Optical Character Recognition) and non-OCR methods.

The project will follow the strcuture above:
```
/TextExtractionBench
    /docs                    # Documentation
    /tests                   # Test scripts and documents
    /text_extraction         # Text extraction modules
        __init__.py
        common_interface.py  # Defines the common interface
        module1.py           # Module for a specific library
        module2.py
        ...
    config.py                # Configuration settings
    main.py                  # Main script to run comparisons
    requirements.txt         # Python dependencies
```

## Features
- Modular design for easy addition or removal of text extraction libraries.
- Supports a wide array of document types.
- Comparative analysis of library performance, including accuracy, speed, and resource utilization.
- Configurable settings for detailed control over extraction parameters.
- Extensive documentation for each module and comparison metrics.

## Supported Libraries
The future supported librerias will be
- OCR Libraries: `pytesseract`, `easyocr`
- PDF and Office Document Libraries: `PyMuPDF` (fitz), `python-docx`, `PyPDF2`, `pdfplumber`
- General Text Extraction: `beautifulsoup4` for HTML content, `Textract` for diverse file formats.

## Getting Started

### Prerequisites
- Python 3.x
- Virtual environment (recommended)

### Installation
- clone the repo
- pip install -r requirements.txt

### Usage
To run the framework and test different text extraction libraries, execute:
python main.py
- Customize the `config.py` file to specify the libraries and settings you want to test.

-- documentation not finished yet


### Add a new module for text extraction
Add Your New Module to the Factory Method: Insert an additional elif block that checks for your new module's name and returns an instance of your module's extractor class.

```
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
    # Add your new module here
    elif module_name == 'new_method':
        from text_extraction.new_method_module import NewMethodExtractor
        return NewMethodExtractor(*args, **kwargs)
    else:
        raise ValueError(f"Unknown module: {module_name}")
```

If your new module requires specific configuration settings, update config.py to include these:
```
TEXT_EXTRACTION_CONFIG = {
    'modules': ['existing_module', 'new_method'],  # Add your new module to the list
    'new_method': {
        # Configuration parameters for your new module
    },
}
```

Implement the TextExtractionModule Interface: Import the common interface and define your class by extending TextExtractionModule. Implement all abstract methods, including any new ones you've added.

# new_method_module.py
```
from text_extraction.common_interface import TextExtractionModule
class NewMethodExtractor(TextExtractionModule):
    def extract_text(self, path):
        # Implementation of text extraction
        return "Extracted text"
    
    def new_method(self, param):
        # Implementation of the new method
        pass
```