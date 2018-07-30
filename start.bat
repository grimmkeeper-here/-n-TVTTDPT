@echo off
title tool to start project
cd /d source
:while
echo ********************************
echo 1. Start Crawler
echo 2. Create Source
echo 3. Start Server
echo 4. Enter Site
echo 5. Exit
set /p input="Make your choice: "
if %input% == 1 (
    cd /d tool
    start call crawler.bat
    cd /d ..
)
if %input% == 2 (
    start python createSource.py
)
if %input% == 3 (
    start python hostServer.py
)
if %input% == 4 (
    start "" "webSource.html"
)
if %input% == 5 (
    Exit
)
goto while
pause