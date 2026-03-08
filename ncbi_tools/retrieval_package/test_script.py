#!/usr/bin/env python3
"""
Test script for NCBI Data Retriever
===================================

This script tests the basic functionality of the NCBI Data Retriever
without actually downloading from NCBI (to avoid API calls during testing).
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the current directory to the path so we can import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ncbi_data_retriever import NCBIDataRetriever


def test_file_reading():
    """Test reading accession IDs from different file formats."""
    print("Testing file reading functionality...")
    
    # Test with sample text file
    try:
        retriever = NCBIDataRetriever.__new__(NCBIDataRetriever)
        accession_ids = retriever._read_accession_ids("sample_accession_list.txt")
        print(f"✓ Text file: Found {len(accession_ids)} accession IDs")
        print(f"  Sample IDs: {accession_ids[:3]}")
    except Exception as e:
        print(f"✗ Text file test failed: {e}")
    
    # Test with sample CSV file
    try:
        accession_ids = retriever._read_accession_ids("sample_accession_list.csv")
        print(f"✓ CSV file: Found {len(accession_ids)} accession IDs")
        print(f"  Sample IDs: {accession_ids[:3]}")
    except Exception as e:
        print(f"✗ CSV file test failed: {e}")


def test_config_loading():
    """Test configuration file loading."""
    print("\nTesting configuration loading...")
    
    try:
        retriever = NCBIDataRetriever.__new__(NCBIDataRetriever)
        config = retriever._load_config("sample_config.yaml")
        print("✓ Configuration loaded successfully")
        print(f"  Email: {config['email']}")
        print(f"  Input file: {config['input_file_path']}")
        print(f"  Output path: {config['output_path']}")
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")


def test_accession_cleaning():
    """Test accession ID cleaning functionality."""
    print("\nTesting accession ID cleaning...")
    
    try:
        retriever = NCBIDataRetriever.__new__(NCBIDataRetriever)
        
        # Test with various formats
        test_ids = [
            "NM_001123456",
            "  NM_001234567  ",
            "Accession: NM_001345678",
            "ACC: NM_001456789",
            "ID: NM_001567890",
            "invalid_id_with_spaces",
            "",
            "NM_001678901"
        ]
        
        cleaned_ids = retriever._clean_accession_ids(test_ids)
        print(f"✓ Cleaned {len(test_ids)} input IDs to {len(cleaned_ids)} valid IDs")
        print(f"  Valid IDs: {cleaned_ids}")
    except Exception as e:
        print(f"✗ Accession cleaning test failed: {e}")


def main():
    """Run all tests."""
    print("=" * 60)
    print("NCBI Data Retriever - Test Suite")
    print("=" * 60)
    
    # Check if sample files exist
    required_files = [
        "sample_accession_list.txt",
        "sample_accession_list.csv", 
        "sample_config.yaml"
    ]
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print(f"✗ Missing required test files: {missing_files}")
        return
    
    # Run tests
    test_config_loading()
    test_file_reading()
    test_accession_cleaning()
    
    print("\n" + "=" * 60)
    print("Test suite completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()