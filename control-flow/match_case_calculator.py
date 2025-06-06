try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter only numbers.")
    exit()

# Ask the user to choose an operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using a Match Case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Handle the division by zero case
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        # Handle cases where the operation is not one of the expected choices
        print("Invalid operation selected. Please choose from +, -, *, /.")
