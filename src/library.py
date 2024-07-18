import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'database', 'database.json')


class Library:
    """Движок управления библиотекой"""
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.books = []

    async def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.books = json.load(f)
        else:
            self.books = []

    async def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.books, f, indent=4)

    async def add_book(self, title, author, year):
        await self.load_data()
        new_book = {
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        await self.save_data()
        return new_book

    async def delete_book(self, book_id):
        await self.load_data()
        book_to_delete = next((book for book in self.books if book['id'] == book_id), None)
        if book_to_delete:
            self.books = [book for book in self.books if book['id'] != book_id]
            await self.save_data()
            return book_id
        else:
            return None

    async def search_books(self, query, field):
        await self.load_data()
        return [book for book in self.books if str(book[field]).lower() == str(query).lower()]

    async def display_books(self):
        await self.load_data()
        return self.books

    async def update_status(self, book_id, new_status):
        await self.load_data()
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                await self.save_data()
                return book
        return None
