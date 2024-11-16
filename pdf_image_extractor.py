#!/usr/bin/env python3

import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        images = page.get_images(full=True)
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_extension = base_image["ext"]
            
            # Save the image
            image_path = f"{output_folder}/page_{page_number + 1}_img_{img_index + 1}.{image_extension}"
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
    
    pdf_document.close()
    print(f"Images have been extracted to {output_folder}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./extract_images.py <pdf_path> <output_folder>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_folder = sys.argv[2]
    extract_images_from_pdf(pdf_path, output_folder)
