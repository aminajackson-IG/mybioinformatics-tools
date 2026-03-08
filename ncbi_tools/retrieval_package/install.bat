@echo off
echo ============================================================
echo NCBI Data Retriever - Windows Installation Script
echo ============================================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found! Installing packages...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo.
echo Next steps:
echo 1. Edit config.yaml with your email address
echo 2. Prepare your accession ID file
echo 3. Run: python ncbi_data_retriever.py
echo.
echo For detailed instructions, see README.md
echo.
pause