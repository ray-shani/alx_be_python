import math

class Shape:
    """
    Base class for geometric shapes.
    Defines an area() method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape. This method should be overridden
        by any concrete derived class.
        Raises:
            NotImplementedError: If the method is not overridden in a derived class.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    Overrides the area() method to calculate the area of a rectangle.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a new Rectangle instance.
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    Overrides the area() method to calculate the area of a circle.
    """
    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle using the formula π * radius^2.
        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

