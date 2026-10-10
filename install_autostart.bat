@echo off
:: SynapseLMS - Install as Windows Startup Service
:: Run this ONCE as Administrator to auto-start on every Windows login

set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "TASK_NAME=SynapseLMS_AutoStart"
set "BAT_FILE=%SCRIPT_DIR%\start_silent.bat"

echo.
echo  ==========================================
echo   SynapseLMS - Installing Auto-Start
echo  ==========================================
echo.

:: Create a silent (no window) startup script
echo @echo off > "%BAT_FILE%"
echo cd /d "%SCRIPT_DIR%" >> "%BAT_FILE%"
echo start /min "" python main.py run >> "%BAT_FILE%"

:: Schedule the task to run at user login
schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1
schtasks /create /tn "%TASK_NAME%" /tr "\"%BAT_FILE%\"" /sc ONLOGON /delay 0001:00 /ru "%USERNAME%" /f

if errorlevel 1 (
    echo [ERROR] Failed to create task. Try running as Administrator.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] SynapseLMS will now start automatically when you log in!
echo           Server will be at: http://127.0.0.1:8000
echo.
echo [TIP] To remove auto-start, run: schtasks /delete /tn "%TASK_NAME%" /f
echo.
pause
