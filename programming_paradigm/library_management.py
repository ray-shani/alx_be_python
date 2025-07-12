class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): True if the book is currently checked out, False otherwise.
                                This is a private attribute.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute, default to not checked out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({status})"

class Library:
    """
    Manages a collection of books.

    Attributes:
        _books (list): A private list to store Book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book instance to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Checks out a book by its title, if it's available.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title.lower() == title.lower():
                found = True
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"'{book.title}' has been checked out.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        if not found:
            print(f"Error: Book with title '{title}' not found in the library.")

    def return_book(self): # Modified: Removed 'title' parameter as requested
        """
        Attempts to return a book. This method now requires a title to be effective
        to return a specific book.
        (Note: This signature was modified based on user request.
        To return a specific book, a title parameter is typically needed.)
        """
        print("Error: To return a specific book, please use a method that accepts the book's title.")
        print("The 'return_book()' method without arguments cannot identify which book to return.")


    def list_available_books(self):
        """
        Lists all books that are currently available (not checked out).
        """
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("\n--- Available Books ---")
            for book in available_books:
                print(book)
            print("-----------------------")
        else:
            print("\nNo books currently available in the library.")

