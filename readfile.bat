@ECHO OFF
title Read File

cd /d %~dp0
echo You are currently in %CD%

:START
echo Input Filepath of .txt file to Read
set/p "txt=>"
python readTXT.py %txt%


:END
