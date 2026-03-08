# Quick Start Guide - NCBI Data Retriever

## 🚀 For Bio357 Students

This is a quick start guide for using the NCBI Data Retriever tool in the bio357 course.

### Step 1: Navigate to the Tool

Open your terminal/command prompt and navigate to the ncbi_tools folder:

```bash
cd /path/to/bio357/ncbi_tools
```

**Important**: Replace `/path/to/bio357` with the actual path where you downloaded the bio357 project.

### Step 2: Install Dependencies

Run the installation script:

```bash
python install.py
```

Or install manually:
```bash
pip install -r requirements.txt
```

Verify installation:
```bash
python check_dependencies.py
```

### Step 3: Configure the Tool

1. Open `config.yaml` in a text editor
2. Change the email address to your university email:
   ```yaml
   email: "your.name@university.edu"
   ```
3. Set the path to your accession ID file:
   ```yaml
   # IMPORTANT: Use FULL PATH to your file!
   input_file_path: "/Users/student/Documents/your_accession_list.txt"
   ```

**⚠️ Path Tips:**
- Use FULL PATHS to avoid confusion
- Mac/Linux: `/Users/yourname/Documents/file.txt`
- Windows: `C:\Users\yourname\Documents\file.txt`
- Or copy your file to the ncbi_tools folder and use just the filename

### Step 4: Prepare Your Data

Create a text file with your accession IDs (one per line):
```
NM_001123456
NM_001234567
XM_001345678
```

### Step 5: Run the Tool

```bash
python ncbi_data_retriever.py
```

### Step 6: Find Your Results

Your downloaded files will be in the `downloads/` folder:
- `downloads/batch_1_genbank.genbank` - GenBank files
- `downloads/batch_1_fasta.fasta` - FASTA files

## 🔧 Common Issues

**"No module named 'docx'" or "ImportError"**
- Run: `pip install python-docx`
- Or run: `python check_dependencies.py` to see all missing packages

**"Configuration file not found"**
- Make sure you're in the `bio357/ncbi_tools` folder

**"Input file not found"**
- Use FULL PATHS to your accession ID file
- Examples: `/Users/student/Documents/file.txt` or `C:\Users\student\Documents\file.txt`
- Or copy your file to the ncbi_tools folder

**"No valid accession IDs found"**
- Check your input file format
- Make sure there are no empty lines

## 📞 Need Help?

1. Check the full README.md for detailed instructions
2. Look at the log file `ncbi_retriever.log` for error details
3. Ask your instructor or TA

---

**That's it! Happy downloading! 🧬**
