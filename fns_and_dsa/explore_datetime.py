import datetime

def display_current_datetime():
    """
    Displays the current date and time formatted as YYYY-MM-DD HH:MM:SS.
    """
    # Obtain the current date and time
    current_date = datetime.datetime.now()
    # Format the date and time into the specified string format
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates the future date by adding
    those days to the current date, and displays it.
    """
    try:
        # Prompt user for the number of days to add
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)

        # Get the current date (without the time part)
        today = datetime.date.today()
        # Create a timedelta object representing the number of days to add
        days_to_add = datetime.timedelta(days=num_days)
        # Calculate the future date
        future_date = today + days_to_add

        # Format the future date into YYYY-MM-DD format
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

def main():
    """
    Main function to run the datetime exploration script.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
