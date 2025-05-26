# The input() function returns a string, so we convert it to an integer using int()
current_age_str = input("How old are you? ")
current_age = int(current_age_str)

# Define the current year and the future year
current_year = 2023
future_year = 2050

# Calculate the number of years to add
years_to_add = future_year - current_year

# Calculate the user's age in the future year
future_age = current_age + years_to_add

# Print the user's future age
print(f"In {future_year}, you will be {future_age} years old.")
