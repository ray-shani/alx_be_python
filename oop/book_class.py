class Book:
    """
    A class to represent a book with title, author, and publication year.
    It demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Optional: Confirmation of creation

    def __del__(self):
        """
        Destructor method, called when the object is about to be destroyed.
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        This is what is typically seen when print() is called on the object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book object.
        This string should ideally be unambiguous and, if possible,
        recreate the object when evaluated (e.g., in a debugger).
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

