# PDF Merger

## Description

A simple Python script to merge multiple PDF files into a single PDF document.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/gamzeozgul/pdf-merger.git
Navigate to the project directory:

sh
Copy code
cd pdf-merger
Install the required library:

sh
Copy code
pip install PyPDF2
Usage
Place your PDF files in the project directory.

Run the script:

sh
Copy code
python pdf_merger.py
The script will merge all PDF files in the directory into a file named combined_bsuni_docs.pdf.

Script Overview
Imports: PyPDF2 and os
Functionality:
Lists files in the directory
Filters and merges PDFs
Outputs a combined PDF
