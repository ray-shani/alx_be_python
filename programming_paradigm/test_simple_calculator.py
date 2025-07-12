import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test class for the SimpleCalculator, inheriting from unittest.TestCase.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures a fresh calculator instance for every test.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method of SimpleCalculator.
        Covers positive numbers, negative numbers, and zero.
        """
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(10, 0), 10, "Should be 10")
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2, "Should be -2")
        self.assertEqual(self.calc.add(-5, 3), -2, "Should be -2")
        # Test mixed numbers and zero
        self.assertEqual(self.calc.add(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.add(100, -50), 50, "Should be 50")

    def test_subtraction(self): # Renamed from test_subtract
        """
        Test the subtract method of SimpleCalculator.
        Covers positive numbers, negative numbers, and zero.
        """
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 2), 3, "Should be 3")
        self.assertEqual(self.calc.subtract(10, 0), 10, "Should be 10")
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3, "Should be -3")
        self.assertEqual(self.calc.subtract(3, 5), -2, "Should be -2")
        # Test mixed numbers and zero
        self.assertEqual(self.calc.subtract(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.subtract(50, 100), -50, "Should be -50")

    def test_multiplication(self):
        """
        Test the multiply method of SimpleCalculator.
        Covers positive numbers, negative numbers, and multiplication by zero.
        """
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(10, 1), 10, "Should be 10")
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(-5, 3), -15, "Should be -15")
        # Test multiplication by zero
        self.assertEqual(self.calc.multiply(0, 5), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(-10, 0), 0, "Should be 0")

    def test_division(self):
        """
        Test the divide method of SimpleCalculator.
        Covers normal division and specifically handles division by zero.
        """
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5, "Should be 5")
        self.assertEqual(self.calc.divide(7, 2), 3.5, "Should be 3.5")
        self.assertEqual(self.calc.divide(-10, 2), -5, "Should be -5")
        self.assertEqual(self.calc.divide(10, -2), -5, "Should be -5")
        self.assertEqual(self.calc.divide(0, 5), 0, "Should be 0")

        # Test division by zero
        # We expect a ValueError to be raised when dividing by zero
        with self.assertRaises(ValueError) as cm:
            self.calc.divide(10, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero", "Error message should match")

        with self.assertRaises(ValueError) as cm:
            self.calc.divide(-5, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero", "Error message should match")

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
