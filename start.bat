@echo off
title SynapseLMS Server
cd /d "%~dp0"

echo.
echo  ==========================================
echo   SynapseLMS - Starting Study System...
echo  ==========================================
echo.

:: Check if Python is available
where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.11+
    pause
    exit /b 1
)

:: Start the server in background
echo [INFO] Starting SynapseLMS server at http://127.0.0.1:8000
echo [INFO] Close this window to stop the server.
echo.

:: Wait 2 seconds then open browser
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://127.0.0.1:8000"

:: Run the server (this keeps the window open)
python main.py run

echo.
echo [INFO] Server stopped.
pause
