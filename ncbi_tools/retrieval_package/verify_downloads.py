#!/usr/bin/env python3
"""
Verification script to check if both GenBank and FASTA files were downloaded correctly.
"""

import os
import glob
from pathlib import Path


def verify_downloads():
    """Check if both GenBank and FASTA files were downloaded."""
    print("=" * 60)
    print("NCBI Download Verification")
    print("=" * 60)
    
    # Check for downloads directory
    downloads_dir = Path("downloads")
    if not downloads_dir.exists():
        print("❌ Downloads directory not found!")
        print("   Make sure you've run the NCBI Data Retriever first.")
        return
    
    # Find all downloaded files
    genbank_files = list(downloads_dir.glob("*.genbank"))
    fasta_files = list(downloads_dir.glob("*.fasta"))
    
    print(f"\n📁 Downloads directory: {downloads_dir.absolute()}")
    print(f"📄 GenBank files found: {len(genbank_files)}")
    print(f"📄 FASTA files found: {len(fasta_files)}")
    
    # List GenBank files
    if genbank_files:
        print("\n🧬 GenBank files:")
        for file in genbank_files:
            size = file.stat().st_size
            print(f"   ✅ {file.name} ({size:,} bytes)")
    else:
        print("\n❌ No GenBank files found!")
    
    # List FASTA files
    if fasta_files:
        print("\n🧬 FASTA files:")
        for file in fasta_files:
            size = file.stat().st_size
            print(f"   ✅ {file.name} ({size:,} bytes)")
    else:
        print("\n❌ No FASTA files found!")
    
    # Check file contents
    print("\n🔍 Checking file contents...")
    
    for file in genbank_files + fasta_files:
        try:
            with open(file, 'r') as f:
                content = f.read(500)  # Read first 500 characters
                
            if file.suffix == '.genbank':
                if 'LOCUS' in content:
                    print(f"   ✅ {file.name} appears to be valid GenBank format")
                else:
                    print(f"   ⚠️  {file.name} may not be valid GenBank format")
            elif file.suffix == '.fasta':
                if content.startswith('>'):
                    print(f"   ✅ {file.name} appears to be valid FASTA format")
                else:
                    print(f"   ⚠️  {file.name} may not be valid FASTA format")
                    
        except Exception as e:
            print(f"   ❌ Error reading {file.name}: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    if genbank_files and fasta_files:
        print("🎉 SUCCESS: Both GenBank and FASTA files were downloaded!")
    elif genbank_files:
        print("⚠️  PARTIAL: Only GenBank files were downloaded.")
        print("   Check your config.yaml - make sure download_fasta: true")
    elif fasta_files:
        print("⚠️  PARTIAL: Only FASTA files were downloaded.")
        print("   Check your config.yaml - make sure download_genbank: true")
    else:
        print("❌ FAILED: No files were downloaded.")
        print("   Check the log file 'ncbi_retriever.log' for errors.")
    print("=" * 60)


if __name__ == "__main__":
    verify_downloads()
