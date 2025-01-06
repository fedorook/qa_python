BooksCollector Tests

This project includes a BooksCollector class and a set of automated tests for it.
The BooksCollector class allows you to:
- Store books and their genres in a dictionary.
- Mark specific books as “favorites.”
- Retrieve books by genre or filter out those with an age rating.
- Tests Overview

All tests reside in the file tests.py. Here is what they cover:

Add a new book (valid names)
Verifies adding books with valid names (including edge cases up to 40 characters).

Add a new book (invalid names)
Checks that books with an empty name or exceeding 40 characters are not added.

Avoid duplicate books
Ensures a book with the same name cannot be added twice.

New book has an empty genre by default
Confirms that the genre is an empty string immediately after adding a new book.

Set a valid genre
Verifies that the genre is set properly for existing books and recognized genres.

Handle an invalid genre
Ensures the genre remains unchanged if the provided genre is not in the allowed list.

Get books by specific genre
Checks that only the correct books are returned for a given genre.

Get books for children
Verifies that books belonging to age-restricted genres are excluded.

Add a book to favorites (valid condition)
Confirms that a book in the dictionary can be successfully added to favorites.

Fail to add a non-existent book to favorites
Ensures that a book not in the dictionary does not appear in the favorites list.

Remove a book from favorites
Checks that removing a favorite book actually takes it out of the favorites list.

