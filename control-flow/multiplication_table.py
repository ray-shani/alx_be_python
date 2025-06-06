try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# Use a for loop to iterate from 1 to 10
# The range(1, 11) function generates numbers from 1 up to (but not including) 11.
for i in range(1, 11):
    # Calculate the product of the user's number and the current loop number
    product = number * i
    
    # Print the result in the specified format "X * Y = Z"
    print(f"{number} * {i} = {product}")