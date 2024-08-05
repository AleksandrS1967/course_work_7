# базовый образ Python
FROM python:3.12-slim

# рабочая директория в контейнере
WORKDIR /app

# копируем зависимости в контейнер
COPY /requirements.txt /

# устанавливаем зависимости
RUN pip install -r /requirements.txt --no-cache-dir

# копируем код приложения в контейнер
COPY . .
