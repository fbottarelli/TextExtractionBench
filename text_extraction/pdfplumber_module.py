# module1.py - Example PDF text extraction module using pdfplumber
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # Adding a newline character after each page
    return text

if __name__ == "__main__":
    # Example usage
    pdf_path = "data/networking/http_pisa.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
