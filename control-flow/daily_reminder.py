# daily_reminder.py

# 1. Prompt the user for task details
task = input("Enter your task: ")
# Convert priority and time_bound inputs to lowercase for consistent checking
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Process the task using a Match Case statement for the priority
match priority:
    case 'high' | 'medium' | 'low':
        # This block runs for any valid priority.
        # Now, use an if statement to check if the task is time-bound.
        
        if time_bound == 'yes':
            # This message is for any task that is time-sensitive.
            reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"
            print(f"\nReminder: {reminder_message}")
            
        elif time_bound == 'no':
            # For non-time-bound tasks, the message varies by priority.
            if priority == 'high':
                print(f"\nReminder: '{task}' is a high priority task. Try to complete it soon.")
            elif priority == 'medium':
                print(f"\nNote: '{task}' is a medium priority task. Plan to get it done.")
            else: # This handles the 'low' priority case
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
                
        else:
            # Handle invalid input for the time-bound question
            print("\nInvalid input for time-bound status. Please answer with 'yes' or 'no'.")
            
    case _:
        # This is the default case for the Match statement, handling any invalid priority input.
        print(f"\nInvalid priority level '{priority}'. Please enter high, medium, or low.")