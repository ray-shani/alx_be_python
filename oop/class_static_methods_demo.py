class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    It performs basic arithmetic operations.
    """

    # Class attribute accessible by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method to perform addition.
        Static methods do not receive an implicit first argument (like self or cls).
        They behave like regular functions, but are part of the class's namespace.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method to perform multiplication.
        Class methods receive the class itself as the first implicit argument (conventionally 'cls').
        This allows them to access or modify class attributes or call other class methods.

        Args:
            cls: The class itself (Calculator in this case).
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        # Accessing a class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

