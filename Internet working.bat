@echo off
set loopNum=10
:veryTop
set loop=0
ping 10.0.30.1
ping 192.168.1.1
:top
ping google.com 
ping 8.8.8.8 
tracert -h 255 google.com
tracert -h 255 8.8.8.8
cls
set /a loop=(loop + 1)
::echo %loop%
if /I %loop% EQU %loopNum% goto veryTop
goto top