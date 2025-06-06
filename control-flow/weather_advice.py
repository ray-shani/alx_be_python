# weather_advice.py

# 1. Prompt the user for the current weather condition.
# The .lower() method is used to make the input case-insensitive (e.g., "Sunny" becomes "sunny").
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Provide clothing recommendations using conditional statements.
if weather == "sunny":
    # This block runs if the user enters "sunny".
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    # This block runs if the weather is not "sunny", but is "rainy".
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    # This block runs if the weather is neither "sunny" nor "rainy", but is "cold".
    print("Make sure to wear a warm coat and a scarf.")
else:
    # This block runs if the input is anything other than "sunny", "rainy", or "cold".
    print("Sorry, I don't have recommendations for this weather.")