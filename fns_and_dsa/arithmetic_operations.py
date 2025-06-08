def perform_operation(num1, num2, operation):
  """
  Performs a basic arithmetic operation based on the provided parameters.

  Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform. 
                     Accepts 'add', 'subtract', 'multiply', or 'divide'.

  Returns:
    The result of the arithmetic operation. If division by zero is attempted,
    it returns a specific error string. For invalid operations, it returns
    an informational string.
  """
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Division by zero is not allowed."
    else:
      return num1 / num2
  else:
    return "Error: Invalid operation specified."