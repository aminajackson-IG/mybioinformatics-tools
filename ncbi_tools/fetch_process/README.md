# NCBI Bio-Data Downloader & Parser 

A lightweight Python utility built with **Biopython** to automate the retrieval of biological records from NCBI and transform complex GenBank metadata into a structured CSV format.

## Features
* **Multi-format Support:** Read Accession IDs from `.txt`, `.csv`, or `.docx` (commented support).
* **Dual Retrieval:** Downloads both **FASTA** (sequences) and **GenBank** (full metadata) files.
* **Feature Extraction:** Automatically parses **CDS (Coding Sequences)** and **Gene** locations/coordinates.
* **Cross-Platform:** Compatible with Windows, macOS, and Linux.

---

## Setup & Installation

1. **Clone or download** this repository.
2. **Open your Terminal**
   ```bash
   cd  mybioinformatics-tools/ncbi_tools/fetch_process
3. **Install dependencies** using the provided requirements file:
   ```bash
   pip install -r requirements.txt
4. **Running**
* ***Download FASTA and GenBank files*** 
    ```bash
       python ncbi_downloader.py
* ***Generate a csv file from GenBank***
    ```bash
       python gb_csv_generator.py
**Note:** Depending on your python install and path, you can also execute with python3 