def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors like division by zero and non-numeric input.

    Args:
        numerator: The top number in the division.
        denominator: The bottom number in the division.

    Returns:
        A string indicating an error or the result of the division.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        # Catch non-numeric input
        return "Error: Please enter numeric values only."
    