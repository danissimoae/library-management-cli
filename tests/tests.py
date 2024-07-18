import unittest
import asyncio
import os
import json
from src.library import Library

TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'test_database.json')

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(data_file=TEST_DATA_FILE)
        with open(TEST_DATA_FILE, 'w') as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(TEST_DATA_FILE):
            os.remove(TEST_DATA_FILE)

    def test_add_book(self):
        async def run_test():
            book = await self.library.add_book("Test Title", "Test Author", 2024)
            self.assertEqual(book['title'], "Test Title")
            self.assertEqual(book['author'], "Test Author")
            self.assertEqual(book['year'], 2024)
            self.assertEqual(book['status'], "в наличии")

        asyncio.run(run_test())

    def test_delete_book(self):
        async def run_test():
            book = await self.library.add_book("Test Title", "Test Author", 2024)
            book_id = book['id']
            deleted_book_id = await self.library.delete_book(book_id)
            self.assertEqual(deleted_book_id, book_id)
            books = await self.library.display_books()
            self.assertEqual(len(books), 0)

        asyncio.run(run_test())

    def test_search_books(self):
        async def run_test():
            await self.library.add_book("Test Title", "Test Author", 2024)
            results = await self.library.search_books("Test Title", "title")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['title'], "Test Title")

        asyncio.run(run_test())

    def test_display_books(self):
        async def run_test():
            await self.library.add_book("Test Title", "Test Author", 2024)
            books = await self.library.display_books()
            self.assertEqual(len(books), 1)
            self.assertEqual(books[0]['title'], "Test Title")

        asyncio.run(run_test())

    def test_update_status(self):
        async def run_test():
            await self.library.add_book("Test Title", "Test Author", 2024)
            updated_book = await self.library.update_status(1, "выдана")
            self.assertEqual(updated_book['status'], "выдана")

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
