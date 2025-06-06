# pattern_drawing.py

# 1. Prompt User for Pattern Size
# Use a try-except block to handle non-integer inputs gracefully.
try:
    size = int(input("Enter the size of the pattern: "))
    
    # Check if the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # 2. Draw the Pattern
        # Initialize a counter for the rows
        row_counter = 0
        
        # Use a 'while' loop to iterate through each row
        while row_counter < size:
            # Inside the 'while' loop, use a 'for' loop to print the asterisks for the current row
            for _ in range(size):
                # Print an asterisk without moving to a new line
                print("* ", end="")
            
            # After the inner loop finishes, print a newline to move to the next row
            print()
            
            # Increment the row counter to proceed to the next row
            row_counter += 1

except ValueError:
    print("Invalid input. Please enter a valid integer.")