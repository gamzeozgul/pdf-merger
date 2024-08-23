from PyPDF2 import PdfFileMerger
import os

def merge_pdfs(pdf_list, output_name):
    merger = PdfFileMerger()
    for pdf in pdf_list:
        if pdf.endswith('.pdf'):
            merger.append(pdf)
    merger.write(output_name)
    merger.close()

if __name__ == "__main__":
    # List your PDF files here
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
    if pdf_files:
        merge_pdfs(pdf_files, 'combined_document.pdf')
        print("PDFs merged successfully!")
    else:
        print("No PDF files found to merge.")
