import os
import csv
# import docx  # Uncomment this and add to requirements.txt to use .docx
from Bio import Entrez, SeqIO

# Replace this with your real email
Entrez.email = "your_email@example.com"


def get_ids_from_docx(file_path):
    """Extracts text from each paragraph of a .docx file."""
    # doc = docx.Document(file_path)
    # return [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return []  # Placeholder


def fetch_ncbi_records(input_file, db="nucleotide"):
    ext = os.path.splitext(input_file)[-1].lower()
    ids = []

    # Logic to handle different file types
    if ext == ".docx":
        ids = get_ids_from_docx(input_file)
    elif ext == ".csv":
        with open(input_file, 'r') as f:
            ids = [line.split(',')[0].strip() for line in f]
    else:  # Default for .txt or other raw text
        with open(input_file, 'r') as f:
            ids = [line.strip() for line in f]

    print(f"Fetching {len(ids)} records from {db}...")

    # Note the files will be inside the folder where you are running your script.
    # You can easily change the file names from record.gb or record.fasta to something else
    # Fetch FASTA
    with Entrez.efetch(db=db, id=ids, rettype="fasta", retmode="text") as handle:
        with open("records.fasta", "w") as out:
            out.write(handle.read())

    # Fetch GenBank
    with Entrez.efetch(db=db, id=ids, rettype="gb", retmode="text") as handle:
        with open("records.gb", "w") as out:
            out.write(handle.read())

    print("Done! Files saved: records.fasta, records.gb")


# if you to use a protein database you can pass in value for the protein db='protein' here.
# Use full/absolute path alternatively put your accession file inside the folder where you're
# running the script
fetch_ncbi_records("accessions.txt")
