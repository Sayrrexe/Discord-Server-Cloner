# Discord Server Cloner

Discord Server Cloner — это инструмент для копирования структуры и настроек одного сервера Discord на другой. Позволяет перенести категории, роли, каналы и эмодзи с одного сервера на другой, используя пользовательский токен.

---

## Особенности
- Копирование категорий, текстовых и голосовых каналов, в том числе скрытых.
- Перенос ролей с настройками.
- Перенос эмодзи.
- Удобный интерфейс командной строки с инструкциями.

---

## Автоматический Запуск
Для Windows:
    запустите cloner.exe для использования в качестве приложения
    запустите run.bat он установит Python и позволит использовать и модифицировать приложение

Для Linux:
Запустите run.sh скрипт подготовит систему к использованию

    ```bash
    chmod +x run.sh
    ./run.sh
    ```
---

## Ручная установка

### 1. С Python:
- Установите зависимости:
  ```bash
  pip install -r requirements.txt
  ```
- Запустите приложение:
  ```bash
  python main.py
  ```

## Примечания
- **Токен безопасности**: Никогда не делитесь токеном, он предоставляет полный доступ к вашему аккаунту.
- **Совместимость**: Скрипт протестирован на Windows, Linux и MacOS.

---

## Поддержка
Если у вас возникли проблемы, создайте issue или свяжитесь с разработчиком.