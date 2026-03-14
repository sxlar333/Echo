@echo off
echo =======================================================
echo.
echo Checking for Python and installing dependencies...
echo Please open a GitHub issue if you run into problems.
echo.
echo =======================================================

:: Define Python version and download URL
set PYTHON_VERSION=3.11.8
set PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set PYTHON_INSTALLER_NAME=python-installer-%PYTHON_VERSION%.exe
set PYTHON_INSTALLER_PATH=%TEMP%\%PYTHON_INSTALLER_NAME%

:: Check if Python is already installed and in PATH
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed and found in PATH.
) else (
    echo Python not found, attempting to install...

    :: Download Python installer using PowerShell
    echo Downloading Python %PYTHON_VERSION%...
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_INSTALLER_URL%', '%PYTHON_INSTALLER_PATH%')"
    if %errorlevel% neq 0 (
        echo Failed to download Python installer. Please check your internet connection or try installing manually.
        goto :eof
    )

    :: Install Python
    echo Installing Python %PYTHON_VERSION% silently... This may take a few minutes.
    start /wait %PYTHON_INSTALLER_PATH% /quiet InstallAllUsers=1 PrependPath=1
    if %errorlevel% neq 0 (
        echo Python installation failed. Please try installing manually.
        goto :eof
    )
    echo Python installed successfully!

    del %PYTHON_INSTALLER_PATH% >nul 2>&1

    timeout /t 5 /nobreak >nul
)

echo Upgrading pip and installing Python packages...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip. Please check your Python installation.
    goto :eof
)

python -m pip install colorama colorist pystyle requests discord.py beautifulsoup4 rich
if %errorlevel% neq 0 (
    echo Failed to install Python packages. Please check your internet connection or Python setup.
    goto :eof
)

echo.
echo Setup complete. Press any key to run the tool.
pause

python multi-tool.py