class Calculator:
    """
    A class demonstrating the usage of static methods and class methods.
    It performs basic arithmetic operations.
    """

    # Class attribute accessible by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not require access to class-specific or instance-specific data.

        Args:
            a (int/float): The first number.
            b (int/float): The second number.

        Returns:
            int/float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It uses the 'cls' parameter to access class attributes,
        in this case, 'calculation_type'.

        Args:
            cls: The class itself (automatically passed).
            a (int/float): The first number.
            b (int/float): The second number.

        Returns:
            int/float: The product of a and b.
        """
        # Accessing the class attribute using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

