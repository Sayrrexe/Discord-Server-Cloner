@echo off

REM Проверка Python
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python не найден. Установка Python...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
)

REM Установка виртуального окружения
if not exist .venv (
    python -m venv .venv
)

REM Активация виртуального окружения
call .venv\Scripts\activate

REM Установка зависимостей
pip install -r requirements.txt

REM Запуск скрипта
python main.py

pause
