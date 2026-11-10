@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Linye3B.exe olusturuluyor...
py -m pip install --upgrade pyinstaller || goto hata
py -m PyInstaller --onefile --noconsole --name Linye3B --add-data "Linye3B.html;." linye3b_pc.py || goto hata
echo.
echo Tamam. Program: dist\Linye3B.exe
pause
exit /b 0
:hata
echo.
echo Bir hata olustu. Python kurulu mu kontrol edin.
pause
