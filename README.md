# Документация к library-management-cli

## Описание
Консольное приложение для управления библиотекой, позволяющее добавлять, удалять, искать и отображать книги. Данные хранятся в формате JSON.

## Реализованные функции
- **Добавление книги**: Пользователь вводит название книги, автора и год издания, после чего книга добавляется в библиотеку с уникальным ID и статусом "в наличии".
- **Удаление книги**: Пользователь вводит ID книги, которую нужно удалить.
- **Поиск книги**: Пользователь может искать книги по названию, автору или году издания.
- **Отображение всех книг**: Приложение выводит список всех книг с их ID, названием, автором, годом издания и статусом.
- **Изменение статуса книги**: Пользователь вводит ID книги и новый статус ("в наличии" или "выдана").
- **Написаны тесты**
- **Проект помещен в докер-контейнер**

## API
- **CLI команды**:
  - **add [title] [author] [year]**: Добавляет новую книгу.
  - **delete [book_id]**: Удаляет книгу по ID.
  - **search [field] [query]**: Ищет книги по полю (title, author, year) и значению.
  - **display**: Отображает все книги.
  - **update [book_id] [new_status]**: Изменяет статус книги.

## Используемые технологии
- **Python**: Основной язык программирования.
- **Click**: Библиотека для создания CLI.
- **Unittest**: Библиотека для тестирования.
- **Docker**: Платформа для контейнеризации.

## Запуск приложения
Шаг 1: Построение Docker образа
```bash
docker build -t library-management-cli .
```
Шаг 2: Запуск Docker контейнера
```bash
docker run -it --rm library-management-cli
```
## Запуск тестов
Запуск Docker контейнера с тестами
```bash
docker run -it --rm library-management-cli python -m unittest discover -s tests
```