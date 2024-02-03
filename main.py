# main.py
from text_extraction.common_interface import TextExtractionModule
from config import TEXT_EXTRACTION_CONFIG
import os

def main():
    # Directory containing PDF files
    pdf_directory = 'data/networking'

    # Specify the module name based on your requirement
    module_name = TEXT_EXTRACTION_CONFIG["modules"][1]  # Dynamically load the first configured module
    
    # Construct the output directory path dynamically based on the module name
    output_directory = os.path.join('output', f'{module_name}_outputs')
    print(f"Using {module_name} for text extraction, output will be saved to {output_directory}")
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the appropriate extractor
    extractor = TextExtractionModule.get_extractor(module_name)

    # Loop over all PDF files in the specified directory
    for filename in os.listdir(pdf_directory):
        print(filename)
        if filename.endswith('.pdf'):
            # Construct the full path to the PDF file
            pdf_path = os.path.join(pdf_directory, filename)
            # Construct the output text file path
            output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")
            
            # Use the extractor
            text = extractor.extract_text(pdf_path)
            
            # Save the extracted text to a file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            print(f"Extracted text from {filename} saved to {output_file_path}")

if __name__ == "__main__":
    main()



