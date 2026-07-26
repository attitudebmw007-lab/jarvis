@echo off
REM Setup script for JARVIS - Windows Installation

echo ==================================================
echo.  🤖 JARVIS - AI Assistant Setup
echo ==================================================
echo.

REM Check Python version
echo ✓ Checking Python version...
python --version
echo.

REM Create virtual environment
echo ✓ Creating virtual environment...
python -m venv venv
echo.

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Upgrade pip
echo ✓ Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install requirements
echo ✓ Installing requirements...
pip install -r requirements.txt
echo.

REM Setup environment file
echo ✓ Setting up environment...
if not exist .env (
    copy .env.example .env
    echo.  ⚠️  Created .env file - Please add your OpenAI API key
) else (
    echo.  ✓ .env file already exists
)
echo.

REM Create necessary directories
echo ✓ Creating directories...
if not exist logs mkdir logs
if not exist data mkdir data
if not exist screenshots mkdir screenshots
echo.

echo ==================================================
echo.  ✅ Setup Complete!
echo ==================================================
echo.
echo 📝 Next steps:
echo.  1. Edit .env and add your OpenAI API key
echo.  2. Run: python launch.py
echo.
echo 🔗 Get your API key from:
echo.  https://platform.openai.com/api-keys
echo.

pause
