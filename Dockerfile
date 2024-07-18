# Используем официальный образ Python в качестве базового
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY src/ /app/src/
COPY tests/ /app/tests/
COPY requirements.txt /app/
COPY README.md /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Определяем команду для запуска приложения
CMD ["python", "src/cli/cli.py"]
