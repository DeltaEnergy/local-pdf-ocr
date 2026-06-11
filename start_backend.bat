@echo off
cd /d "%USERPROFILE%\OneDrive\Documents\local-pdf-ocr\backend"
call .venv\Scripts\activate.bat
uvicorn app:app --reload --port 8000
pause
