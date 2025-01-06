import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        """Fixture that creates a new instance of BooksCollector before each test."""
        return BooksCollector()

    @pytest.mark.parametrize("book_name", ["Книга1", "Книга2", "A" * 40])
    def test_add_new_book_success(self, collector, book_name):
        """
        Tests the successful addition of a book to the dictionary.
        Parametrized to check multiple variants of book names.
        """
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre(), "The book was not added to the dictionary."

    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_add_new_book_wrong_name(self, collector, book_name):
        """
        Tests that a book with an incorrect name (empty string or more than 40 characters)
        is not added to the dictionary.
        """
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre(), "An invalid book name should not be added."

    def test_add_new_book_duplicate(self, collector):
        """
        Tests that the same book cannot be added twice.
        """
        book_name = "Моя книга"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)  # Attempt to add the same book again
        assert list(collector.get_books_genre().keys()).count(book_name) == 1, \
            "The book was added to the dictionary a second time."

    def test_added_book_has_empty_genre_by_default(self, collector):
        """
        After adding a new book, its genre should be empty (an empty string) by default.
        """
        book_name = "Безжанровая книга"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == "", "A newly added book should have an empty genre by default."

    def test_set_book_genre_success(self, collector):
        """
        Tests setting a valid genre for a book that exists in the dictionary.
        """
        book_name = "Жанровая книга"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Фантастика")
        assert collector.get_book_genre(book_name) == "Фантастика", "The book's genre was not set correctly."

    def test_set_book_genre_incorrect_genre(self, collector):
        """
        Tests that if an invalid genre is set, the book's genre remains unchanged.
        """
        book_name = "Нет такого жанра"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "НекорректныйЖанр")
        assert collector.get_book_genre(book_name) == "", "The genre should not change to an invalid value."

    def test_get_books_with_specific_genre(self, collector):
        """
        Tests that the method returns a list of books of the specified genre only.
        """
        # Add several books
        collector.add_new_book("Фильм-детектив")
        collector.add_new_book("Мультфильм добрый")
        collector.add_new_book("Комедия странная")
        # Set genres
        collector.set_book_genre("Фильм-детектив", "Детективы")
        collector.set_book_genre("Мультфильм добрый", "Мультфильмы")
        collector.set_book_genre("Комедия странная", "Комедии")
        # Verify
        assert collector.get_books_with_specific_genre("Детективы") == ["Фильм-детектив"], \
            "The detective list should only contain 'Фильм-детектив'."

    def test_get_books_for_children(self, collector):
        """
        Tests that the list of children's books does not include books whose genre has an age rating.
        """
        collector.add_new_book("Страшилка")
        collector.add_new_book("Смешарики")
        collector.set_book_genre("Страшилка", "Ужасы")  # This genre has an age rating
        collector.set_book_genre("Смешарики", "Мультфильмы")  # This genre does not
        assert collector.get_books_for_children() == ["Смешарики"], \
            "The children's book list should not include books with age-restricted genres."

    def test_add_book_in_favorites_success(self, collector):
        """
        Tests adding a book to favorites under correct conditions (book exists in the dictionary).
        """
        book_name = "Любимая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books(), "The book should be added to favorites."

    def test_add_book_in_favorites_when_not_in_genre_dict(self, collector):
        """
        Tests that a book not present in the dictionary cannot be added to favorites.
        """
        collector.add_book_in_favorites("Непонятная книга")
        assert "Непонятная книга" not in collector.get_list_of_favorites_books(), \
            "A book should not be added to favorites if it's not in the dictionary."

    def test_delete_book_from_favorites(self, collector):
        """
        Tests removing a book from favorites if it is already in the list.
        """
        book_name = "Книга для удаления"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books(), "The book should be removed from favorites."
