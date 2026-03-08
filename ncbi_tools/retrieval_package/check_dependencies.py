#!/usr/bin/env python3
"""
Dependency Checker for NCBI Data Retriever
==========================================

This script checks if all required dependencies are installed correctly.
"""

import sys
import importlib


def check_python_version():
    """Check Python version compatibility."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required!")
        return False
    else:
        print("✅ Python version is compatible")
        return True


def check_package(package_name, import_name=None, description=""):
    """Check if a package is installed and importable."""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name} - {description}")
        return True
    except ImportError:
        print(f"❌ {package_name} - {description} (MISSING)")
        return False


def main():
    """Check all dependencies."""
    print("=" * 60)
    print("NCBI Data Retriever - Dependency Checker")
    print("=" * 60)
    
    # Check Python version
    python_ok = check_python_version()
    print()
    
    # Check required packages
    print("Checking required packages:")
    required_packages = [
        ("requests", "requests", "HTTP requests for NCBI API"),
        ("PyYAML", "yaml", "YAML configuration file support"),
        ("pandas", "pandas", "CSV and Excel file support"),
        ("openpyxl", "openpyxl", "Excel file support"),
        ("python-docx", "docx", "Word document support"),
        ("lxml", "lxml", "XML processing (required by python-docx)"),
    ]
    
    required_ok = 0
    for package, import_name, description in required_packages:
        if check_package(package, import_name, description):
            required_ok += 1
    
    print()
    print("Checking optional packages:")
    optional_packages = [
        ("et-xmlfile", "et_xmlfile", "XML file support (required by openpyxl)"),
        ("python-dateutil", "dateutil", "Date utilities (required by pandas)"),
        ("pytz", "pytz", "Timezone support (required by pandas)"),
        ("numpy", "numpy", "Numerical computing (required by pandas)"),
    ]
    
    optional_ok = 0
    for package, import_name, description in optional_packages:
        if check_package(package, import_name, description):
            optional_ok += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Required packages: {required_ok}/{len(required_packages)}")
    print(f"Optional packages: {optional_ok}/{len(optional_packages)}")
    
    if required_ok == len(required_packages):
        print("\n🎉 All required packages are installed!")
        print("You can now run the NCBI Data Retriever.")
    else:
        print(f"\n❌ {len(required_packages) - required_ok} required packages are missing.")
        print("Please install missing packages using:")
        print("   pip install -r requirements.txt")
        print("   or")
        print("   python install.py")
    
    if optional_ok < len(optional_packages):
        print(f"\n⚠️  {len(optional_packages) - optional_ok} optional packages are missing.")
        print("Some features may not work correctly.")
    
    print("\nFor help, see README.md or contact your instructor.")


if __name__ == "__main__":
    main()
