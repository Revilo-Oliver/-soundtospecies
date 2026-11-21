@echo off
cd /d "c:\Users\olive\OneDrive\ドキュメント\SoundToSpecies"
echo Starting Sound to Species development server in a new window...
echo.

rem Start the Django dev server in a new terminal window bound to all interfaces
start "DjangoServer" cmd /k "python manage.py runserver 0.0.0.0:8000"

rem Wait a moment then open the browser to the local address
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/"

echo Server launched. Close this window to stop opening the browser.
pause
