# config.py

# Configuration for text extraction modules
TEXT_EXTRACTION_CONFIG = {
    'modules': ['pdfplumber'],  # List of modules to use for text extraction
    # Add module-specific configurations here
    'pdfplumber': {
        # Example configuration parameter for pdfplumber module
        'include_page_numbers': False,
    },
}
