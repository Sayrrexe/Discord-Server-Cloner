#!/bin/bash

# Проверка наличия Python
if ! command -v python3 &> /dev/null
then
    echo "Python3 не найден. Установка Python3..."
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip
fi

# Создание виртуального окружения
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Активация виртуального окружения
source .venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск скрипта
python3 main.py
