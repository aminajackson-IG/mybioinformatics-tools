#!/usr/bin/env python3
"""
Test script to verify both GenBank and FASTA downloads work
"""

import os
import sys
from pathlib import Path

# Add the current directory to the path so we can import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ncbi_data_retriever import NCBIDataRetriever


def test_both_formats():
    """Test downloading both GenBank and FASTA formats."""
    print("=" * 60)
    print("Testing Both GenBank and FASTA Downloads")
    print("=" * 60)
    
    # Create a test configuration
    test_config = {
        'email': 'test@example.com',
        'input_file_path': 'sample_accession_list.txt',
        'output_path': 'test_downloads/',
        'batch_size': 2,  # Small batch for testing
        'delay_between_requests': 1.0,
        'download_genbank': True,
        'download_fasta': True
    }
    
    # Create a temporary config file
    import yaml
    with open('test_config.yaml', 'w') as f:
        yaml.dump(test_config, f)
    
    try:
        # Initialize retriever with test config
        retriever = NCBIDataRetriever('test_config.yaml')
        
        # Test reading accession IDs
        print("\n1. Testing file reading...")
        accession_ids = retriever._read_accession_ids('sample_accession_list.txt')
        print(f"   Found {len(accession_ids)} accession IDs: {accession_ids}")
        
        # Test cleaning accession IDs
        print("\n2. Testing accession ID cleaning...")
        cleaned_ids = retriever._clean_accession_ids(accession_ids)
        print(f"   Cleaned to {len(cleaned_ids)} valid IDs: {cleaned_ids}")
        
        # Test downloading (this will actually make API calls)
        print("\n3. Testing downloads...")
        print("   This will make actual API calls to NCBI!")
        response = input("   Continue? (y/n): ")
        
        if response.lower() == 'y':
            retriever.retrieve_data()
            print("\n✅ Test completed! Check the test_downloads/ folder for results.")
        else:
            print("   Test skipped.")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        # Clean up test config file
        if os.path.exists('test_config.yaml'):
            os.remove('test_config.yaml')


if __name__ == "__main__":
    test_both_formats()
