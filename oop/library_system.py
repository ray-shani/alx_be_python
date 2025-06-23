class Book:
    """
    Base class representing a generic book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    Additional attribute:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author) # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook object,
        including its file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book, inheriting from Book.
    Additional attribute:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook object,
        including its page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library, demonstrating composition by holding a collection of books.
    Attributes:
        books (list): A list to store various Book, EBook, or PrintBook instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book instances (or derived classes) can be added to the library.")

    def list_books(self):
        """
        Prints the details of all books currently in the library's collection.
        It uses the __str__ method of each book object for proper formatting.
        """
        if not self.books:
            print("The library is currently empty.")
            return

        print("\n--- Books in the Library ---")
        for book in self.books:
            print(book) # This will implicitly call the __str__ method of the respective book object
        print("----------------------------")

