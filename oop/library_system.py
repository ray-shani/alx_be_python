# library_system.py

class Book:
    """
    Base class representing a generic book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the EBook.
            author (str): The author of the EBook.
            file_size (int): The file size of the EBook in KB.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a print book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the PrintBook.
            author (str): The author of the PrintBook.
            page_count (int): The number of pages in the PrintBook.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that manages a collection of books (composition).
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only Book instances (or derived classes) can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        for book in self.books:
            print(book)  # This will automatically call the __str__ method of each book object

