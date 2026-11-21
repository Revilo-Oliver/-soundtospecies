@echo off
REM Start a preview static server in a new window and open browser
cd /d "%~dp0"
echo Starting preview server in new window...
start "PreviewServer" cmd /c "python -m http.server 8001"
REM small delay to let the server start
timeout /t 1 > nul
start "" "http://127.0.0.1:8001/"
exit /b
