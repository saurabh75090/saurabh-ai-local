@echo off
cd /d "%~dp0"

echo Starting Saurabh AI...
echo.

REM Check if Ollama is already running
powershell -Command "try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434 -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"

if errorlevel 1 (
    echo Starting Ollama...
    start "Ollama" cmd /k "ollama serve"
    timeout /t 4 /nobreak >nul
) else (
    echo Ollama is already running.
)

echo Starting Streamlit app...
start "Saurabh AI - App" cmd /k ".venv\Scripts\python.exe -m streamlit run app.py"

timeout /t 4 /nobreak >nul

echo Starting public ngrok link...
start "Saurabh AI - ngrok" cmd /k "ngrok http 8501"

echo.
echo Saurabh AI started!
timeout /t 3 >nul
exit