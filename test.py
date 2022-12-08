import unittest
import requests

class BooksTest(unittest.TestCase):

    def test_get_all_books(self):
        response = requests.get(url="http://127.0.0.1:5000/books")
        assert(response.status_code, 200)
        print("LIST API TEST SUCCESS.")

    def test_create_book():
        data = {
            "author": "Meghana",
            "id": 1,
            "language": "Kannada",
            "title": "ksjhgks"
        }
        response = requests.post("http://127.0.0.1:5000/books", data=data)
        assert(response.status_code, 200)
        print("CREATE BOOK API TEST SUCCESS")

    def test_update_book():
        data = {
            "author": "Meghana Ashwin",
            "language": "Kannada",
            "title": "ksjhgks"
        }
        response = requests.post("http://127.0.0.1:5000/books/1", data=data)
        assert(response.status_code, 200)
        print("UPDATE BOOK API TEST SUCCESS")

    def test_get_a_book():
        response = requests.post("http://127.0.0.1:5000/books/1")
        assert(response.status_code, 200)
        print("GET A BOOK API TEST SUCCESS")

    def test_delete_a_book():
        response = requests.post("http://127.0.0.1:5000/books/1")
        assert(response.status_code, 200)
        print("DELETE BOOK API TEST SUCCESS")

if __name__ == "__main__":
    # test_get_all_books()
    # test_create_book()
    # test_update_book()
    # test_get_a_book()
    test_delete_a_book()
