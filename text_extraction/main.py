from text_extraction.common_interface import TextExtractionModule
from text_extraction.pdfplumber import extract_text_from_pdf  # Assuming module1 is for pdfplumber
import config

class PDFPlumberModule(TextExtractionModule):
    def extract_text(self, path):
        return extract_text_from_pdf(path)

# Dynamically load modules based on configuration
# For simplicity, this example directly uses PDFPlumberModule
# In a full implementation, you might use importlib to dynamically import modules based on config.py

def main():
    # Example: Select the module based on configuration
    module_name = config.TEXT_EXTRACTION_CONFIG['modules'][0]
    
    if module_name == 'pdfplumber':
        module = PDFPlumberModule()
    else:
        raise ValueError(f"Unsupported module: {module_name}")
    
    # Example usage
    path = "path/to/your/pdf/file.pdf"
    text = module.extract_text(path)
    print(text)

if __name__ == "__main__":
    main()
