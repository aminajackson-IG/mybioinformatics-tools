#!/usr/bin/env python3
"""
Installation Script for NCBI Data Retriever
===========================================

This script helps students install the required packages and set up the tool.
"""

import subprocess
import sys
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Python 3.7 or higher is required!")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True


def install_requirements():
    """Install required packages."""
    print("\n📦 Installing required packages...")
    
    try:
        # Check if pip is available
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
        
        # Install requirements with upgrade flag
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ All packages installed successfully!")
            
            # Verify critical packages
            print("\n🔍 Verifying critical packages...")
            critical_packages = ['requests', 'PyYAML', 'pandas', 'python-docx', 'openpyxl']
            
            for package in critical_packages:
                try:
                    if package == 'PyYAML':
                        __import__('yaml')
                    elif package == 'python-docx':
                        __import__('docx')
                    else:
                        __import__(package)
                    print(f"   ✅ {package}")
                except ImportError:
                    print(f"   ❌ {package} - installation may have failed")
                    return False
            
            return True
        else:
            print(f"❌ Error installing packages: {result.stderr}")
            print("\n🔧 Trying individual package installation...")
            return install_packages_individually()
            
    except subprocess.CalledProcessError:
        print("❌ Error: pip is not available!")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def install_packages_individually():
    """Install packages one by one if batch installation fails."""
    packages = [
        'requests>=2.28.0',
        'PyYAML>=6.0',
        'pandas>=1.5.0',
        'openpyxl>=3.0.0',
        'python-docx>=0.8.11',
        'lxml>=4.6.0',
        'et-xmlfile>=1.1.0'
    ]
    
    success_count = 0
    for package in packages:
        try:
            print(f"   Installing {package}...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", package
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"   ✅ {package}")
                success_count += 1
            else:
                print(f"   ❌ {package}: {result.stderr}")
        except Exception as e:
            print(f"   ❌ {package}: {e}")
    
    if success_count >= 4:  # At least core packages
        print(f"\n✅ {success_count}/{len(packages)} packages installed successfully")
        return True
    else:
        print(f"\n❌ Only {success_count}/{len(packages)} packages installed")
        return False


def create_sample_files():
    """Create sample configuration and data files."""
    print("\n📝 Creating sample files...")
    
    # Check if config.yaml exists
    if not os.path.exists("config.yaml"):
        print("   Creating config.yaml from sample...")
        try:
            with open("sample_config.yaml", "r") as src:
                content = src.read()
            with open("config.yaml", "w") as dst:
                dst.write(content)
            print("   ✅ config.yaml created")
        except Exception as e:
            print(f"   ❌ Error creating config.yaml: {e}")
    else:
        print("   ✅ config.yaml already exists")
    
    # Check if sample data files exist
    sample_files = ["sample_accession_list.txt", "sample_accession_list.csv"]
    for file in sample_files:
        if os.path.exists(file):
            print(f"   ✅ {file} exists")
        else:
            print(f"   ⚠️  {file} not found (optional)")


def run_test():
    """Run a basic test to verify installation."""
    print("\n🧪 Running installation test...")
    
    try:
        result = subprocess.run([
            sys.executable, "test_script.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Installation test passed!")
            return True
        else:
            print(f"❌ Installation test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False


def main():
    """Main installation process."""
    print("=" * 60)
    print("NCBI Data Retriever - Installation Script")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("\n❌ Installation failed!")
        print("Please try installing packages manually:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Create sample files
    create_sample_files()
    
    # Run test
    if run_test():
        print("\n" + "=" * 60)
        print("🎉 Installation completed successfully!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Edit config.yaml with your email address")
        print("2. Prepare your accession ID file")
        print("3. Run: python ncbi_data_retriever.py")
        print("\nFor detailed instructions, see README.md")
    else:
        print("\n⚠️  Installation completed with warnings.")
        print("The tool may still work, but please check the error messages above.")


if __name__ == "__main__":
    main()