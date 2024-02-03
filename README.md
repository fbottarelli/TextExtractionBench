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
