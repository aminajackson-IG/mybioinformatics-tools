# NCBI Data Retriever

A user-friendly tool for downloading GenBank and FASTA files from NCBI databases using accession IDs. This tool is designed specifically for students and researchers who may not be familiar with programming.

## 🎯 What This Tool Does

This tool automatically downloads DNA/protein sequence files from NCBI (National Center for Biotechnology Information) using accession IDs. It can:

- Read accession IDs from multiple file formats (TXT, CSV, Excel, Word)
- Download GenBank format files (detailed sequence information)
- Download FASTA format files (simple sequence format)
- Handle large lists of accession IDs automatically
- Organize downloaded files in batches for easy management

## 📋 Prerequisites

Before using this tool, you need:

1. **Python 3.7 or higher** installed on your computer
2. **An email address** (required by NCBI for API access)
3. **A list of accession IDs** in one of the supported file formats

### Installing Python

If you don't have Python installed:

- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Mac**: Download from [python.org](https://www.python.org/downloads/) or use Homebrew
- **Linux**: Usually pre-installed, or install via package manager

## 🚀 Quick Start Guide

### Step 1: Navigate to the Tool

1. Open a terminal/command prompt
2. Navigate to the `bio357/ncbi_tools` directory:
   ```bash
   cd /path/to/bio357/ncbi_tools
   ```
   
   **Note**: Replace `/path/to/bio357` with the actual path to your bio357 folder.

### Step 2: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

**Alternative**: Run the installation script:
```bash
python install.py
```

**Verify Installation**: Check if all dependencies are installed correctly:
```bash
python check_dependencies.py
```

### Step 3: Prepare Your Data

Create a file with your accession IDs. You can use any of these formats:

#### Option A: Text File (.txt)
Create a file called `accession_list.txt` with one accession ID per line:
```
NM_001123456
NM_001234567
XM_001345678
```

#### Option B: CSV File (.csv)
Create a file with accession IDs in a column:
```csv
accession_id
NM_001123456
NM_001234567
XM_001345678
```

#### Option C: Excel File (.xlsx)
Create an Excel file with accession IDs in a column (any column name works).

#### Option D: Word Document (.docx)
Create a Word document with accession IDs (one per line or in a table).

### Step 4: Configure the Tool

1. Open the `config.yaml` file in a text editor
2. Update the following settings:

```yaml
# REQUIRED: Your email address
email: "your.email@university.edu"

# REQUIRED: Path to your input file
# IMPORTANT: Use the FULL PATH to your file!
input_file_path: "/Users/student/Documents/accession_list.txt"

# OPTIONAL: Where to save downloaded files
# IMPORTANT: Use the FULL PATH for best results!
output_path: "/Users/student/Documents/downloads/"
```

**⚠️ Important Path Information:**
- **Use FULL PATHS** to avoid confusion about where files are located
- **Mac/Linux**: `/Users/yourname/Documents/yourfile.txt`
- **Windows**: `C:\Users\yourname\Documents\yourfile.txt`
- **Relative paths** work if files are in the ncbi_tools folder: `accession_list.txt`

### Step 5: Run the Tool

In your terminal/command prompt, run:

```bash
python ncbi_data_retriever.py
```

The tool will:
- Read your accession IDs
- Download the corresponding GenBank and FASTA files
- Save them in organized batches
- Show progress and any errors

## 📁 File Formats Explained

### Input File Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| Text | `.txt` | Simple text file, one accession ID per line |
| CSV | `.csv` | Comma-separated values, accession IDs in any column |
| Excel | `.xlsx` | Excel spreadsheet, accession IDs in any column |
| Word | `.docx` | Word document, accession IDs in text or tables |

### Output File Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| GenBank | `.genbank` | Detailed sequence information with annotations |
| FASTA | `.fasta` | Simple sequence format with header and sequence |

## ⚙️ Configuration Options

The `config.yaml` file contains all the settings. Here's what each option does:

```yaml
# REQUIRED SETTINGS
email: "your.email@university.edu"        # Your email (NCBI requirement)
input_file_path: "accession_list.txt"     # Path to your input file

# OPTIONAL SETTINGS
output_path: "downloads/"                 # Where to save files (default: ncbi_tools folder)
batch_size: 200                          # How many IDs to process at once
delay_between_requests: 0.5              # Delay between requests (be nice to NCBI!)
download_genbank: true                   # Download GenBank files
download_fasta: true                     # Download FASTA files
```

## 📂 Understanding the File Structure

When you download the bio357 project, you'll see this structure:

```
bio357/
├── ncbi_blast/                    # BLAST analysis tools
│   ├── bio357_blast_runner.py
│   └── ...
└── ncbi_tools/                    # NCBI data retrieval tools
    ├── ncbi_data_retriever.py     # Main script
    ├── config.yaml                # Configuration file
    ├── requirements.txt           # Python dependencies
    ├── README.md                  # This file
    ├── install.py                 # Installation script
    ├── sample_accession_list.txt  # Sample data
    └── downloads/                 # Downloaded files (created when you run the tool)
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### "Configuration file not found"
- Make sure you're running the script from the `bio357/ncbi_tools` folder
- Check that `config.yaml` exists in the same folder

#### "Input file not found"
- **Use FULL PATHS** to your accession ID file
- Check that the file actually exists at the specified location
- Try copying your file to the ncbi_tools folder and using just the filename
- Examples of correct paths:
  - Mac/Linux: `/Users/student/Documents/accession_list.txt`
  - Windows: `C:\Users\student\Documents\accession_list.txt`
  - Relative: `accession_list.txt` (if file is in ncbi_tools folder)

#### "No valid accession IDs found"
- Check your input file format
- Make sure accession IDs are in the correct column (for CSV/Excel files)
- Remove any empty lines or invalid characters

#### "Error downloading from NCBI"
- Check your internet connection
- Verify your email address in the config file
- Try reducing the `batch_size` in config.yaml
- Increase the `delay_between_requests` value

#### "Permission denied" errors
- Make sure you have write permissions in the output directory
- Try running as administrator (Windows) or with sudo (Mac/Linux)

#### "Only GenBank files downloaded, no FASTA files"
- Check your `config.yaml` file - make sure `download_fasta: true`
- Verify that both `download_genbank: true` and `download_fasta: true` are set
- Run `python verify_downloads.py` to check what files were actually downloaded
- Check the log file for any FASTA-specific error messages

#### "Only FASTA files downloaded, no GenBank files"
- Check your `config.yaml` file - make sure `download_genbank: true`
- Verify that both `download_genbank: true` and `download_fasta: true` are set
- Run `python verify_downloads.py` to check what files were actually downloaded
- Check the log file for any GenBank-specific error messages

#### "Module not found" errors
- Make sure you've installed the requirements: `pip install -r requirements.txt`
- Try running the installation script: `python install.py`
- Check your installation: `python check_dependencies.py`
- If specific modules are missing, install them individually:
  ```bash
  pip install requests PyYAML pandas openpyxl python-docx lxml
  ```

#### "ImportError" or "Exception module" errors
- These are usually caused by missing dependencies
- Run `python check_dependencies.py` to identify missing packages
- Try installing packages individually if batch installation fails
- Make sure you're using Python 3.7 or higher

### Getting Help

1. Check the log file `ncbi_retriever.log` for detailed error messages
2. Verify your input file format matches the examples above
3. Test with a small list of accession IDs first
4. Contact your instructor or TA for assistance

## 📊 Understanding the Output

### File Organization

Downloaded files are organized in batches:
- `downloads/batch_1_genbank.genbank` - First batch of GenBank files
- `downloads/batch_1_fasta.fasta` - First batch of FASTA files
- `downloads/batch_2_genbank.genbank` - Second batch of GenBank files
- And so on...

### Verify Your Downloads

After running the tool, verify that both file types were downloaded correctly:

```bash
python verify_downloads.py
```

This verification script will show you:
- How many GenBank and FASTA files were downloaded
- File sizes and locations
- Whether the files are in the correct format
- Any issues with the downloads

### Log File

The tool creates a `ncbi_retriever.log` file that contains:
- Detailed progress information
- Error messages and warnings
- Summary of what was downloaded

## 🎓 Educational Notes

### What are Accession IDs?

Accession IDs are unique identifiers for biological sequences in NCBI databases:
- **NM_**: mRNA sequences
- **XM_**: Predicted mRNA sequences
- **NP_**: Protein sequences
- **XP_**: Predicted protein sequences
- **NC_**: Complete genomic sequences

### GenBank vs FASTA Format

- **GenBank format**: Contains detailed information including gene annotations, features, and metadata
- **FASTA format**: Simple format with just a header line and the sequence

### Why Use This Tool?

- **Automation**: Download hundreds of sequences automatically
- **Reliability**: Built-in error handling and retry mechanisms
- **Compliance**: Follows NCBI's guidelines for API usage
- **Flexibility**: Supports multiple input formats

## 🔬 Example Workflow

Here's a typical workflow for a student project:

1. **Research Phase**: Find accession IDs of interest from NCBI website
2. **Data Collection**: Create a list of accession IDs in Excel or text file
3. **Configuration**: Set up the config.yaml file with your email and file paths
4. **Download**: Run the tool to download all sequences
5. **Analysis**: Use the downloaded files in your bioinformatics analysis

## 📝 Best Practices

1. **Start Small**: Test with 5-10 accession IDs first
2. **Be Patient**: Large downloads can take time
3. **Check Results**: Always verify that your files downloaded correctly
4. **Keep Logs**: Save the log file for troubleshooting
5. **Respect Limits**: Don't overwhelm NCBI servers with too many requests

## 🆘 Support

If you encounter issues:

1. Read this README carefully
2. Check the log file for error details
3. Try the troubleshooting section above
4. Contact your course instructor or teaching assistant
5. Check NCBI's website for any service announcements

## 📄 License

This tool is provided for educational purposes. Please respect NCBI's terms of service and usage guidelines.

---

**Happy Researching! 🧬**

*This tool was created for Bio357 students to make NCBI data retrieval accessible and user-friendly.*