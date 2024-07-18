import asyncio
import click
from src.library import Library

library = Library()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('title')
@click.argument('author')
@click.argument('year')
def add(title, author, year):
    """Добавить книгу"""
    new_book = asyncio.run(library.add_book(title, author, year))
    click.echo(f"Книга '{new_book['title']}' добавлена с ID {new_book['id']}.")


@cli.command()
@click.argument('book_id', type=int)
def delete(book_id):
    """Удалить книгу по ID"""
    book_id = asyncio.run(library.delete_book(book_id))
    click.echo(f"Книга с ID {book_id} удалена.")


@cli.command()
@click.argument('field')
@click.argument('query')
def search(field, query):
    """Поиск книги по полю (title, author, year) и значению"""
    result = asyncio.run(library.search_books(query, field))
    if result:
        for book in result:
            click.echo(
                f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
    else:
        click.echo("Книги не найдены.")


@cli.command()
def display():
    """Показать все книги"""
    books = asyncio.run(library.display_books())
    if books:
        for book in books:
            click.echo(
                f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
    else:
        click.echo("Библиотека пуста.")


@cli.command()
@click.argument('book_id', type=int)
@click.argument('new_status')
def update(book_id, new_status):
    """Изменить статус книги"""
    updated_book = asyncio.run(library.update_status(book_id, new_status))
    if updated_book:
        click.echo(f"Статус книги с ID {updated_book['id']} обновлен на '{new_status}'.")
    else:
        click.echo(f"Книга с ID {book_id} не найдена.")


if __name__ == "__main__":
    cli()
