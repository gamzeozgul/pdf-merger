# PDF Merger

**PDF Merger** is a Python script designed to merge multiple PDF files into a single PDF document. This tool is simple to use and requires minimal setup.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [License](#license)

## Description

**PDF Merger** provides a straightforward way to combine multiple PDF files into one. Whether you need to merge reports, documents, or any other PDFs, this script automates the process efficiently.

## Requirements

- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **PyPDF2 library**: A Python library for PDF manipulation.

## Installation

To get started with **PDF Merger**, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gamzeozgul/pdf-merger.git

2. **Navigate to the project directory:**

    ```bash
   cd pdf-merger

3. **Install the required library:**

    ```bash
   pip install PyPDF2

## Usage

1. **Place your PDF files:** Put all the PDF files you want to merge into the project directory.

2. **Run the script:** Execute the script with Python to merge the PDFs.

    ```bash
   python pdf_merger.py

After running the script, a new file named combined_bsuni_docs.pdf will be created in the project directory. This file contains all the merged PDFs.

## Script Overview

- **Imports:**

   -PyPDF2: For handling PDF files.

   -os: For directory and file operations.


- **Functionality:**

  -Lists all PDF files in the directory.

  -Merges these PDFs into one.

  -Saves the combined PDF as combined_bsuni_docs.pdf.
