@echo off
echo [1/6] Sanal ortam olusturuluyor...
python -m venv venv

REM PowerShell'de script çalıştırma engelini geçici olarak kaldırıyoruz
powershell -Command "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"

echo [2/6] Sanal ortam aktif ediliyor...
call venv\Scripts\activate.bat

echo [3/6] pip guncelleniyor...
python -m pip install --upgrade pip

echo [4/6] Gereksinimler yukleniyor...
pip install flask gtts transformers sentencepiece torch protobuf

echo [5/6] Masaustune kisayol olusturuluyor...
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('$env:USERPROFILE\Desktop\Echoturk.lnk');$s.TargetPath='%cd%\venv\Scripts\python.exe';$s.Arguments=' app.py';$s.WorkingDirectory='%cd%';$s.WindowStyle=1;$s.IconLocation='%cd%\venv\Scripts\python.exe,0';$s.Save()"

echo [6/6] Kurulum tamamlandi. Masaustunde 'Echoturk' kisayolu olustu.
pause