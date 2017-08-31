@echo off
:top
timeout /T 10 /nobreak >nul
echo Press any button to hibernate 
timeout /T -1 >nul
shutdown -h
goto top