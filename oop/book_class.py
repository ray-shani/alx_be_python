class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates Python magic methods for initialization, deletion,
    and string representation.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # According to the desired "Expected Output", we do not print
        # a creation message here.

    def __del__(self):
        """
        Destructor method called when the Book object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the user-friendly string representation of the Book object.
        This is what is typically seen when print() is called on the object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object.
        This string should ideally be unambiguous and allow recreation
        of the object. It's typically used by developers for debugging.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

