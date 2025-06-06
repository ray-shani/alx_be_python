# daily_reminder.py

# 1. Prompt the user for a single task and its attributes.
task = input("Enter your task: ")
# Use .lower() to make the checking case-insensitive for priority and time-bound status.
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Add a blank line for clean separation between the input prompts and the output message.
print()

# 2. Use a Match Case statement to process the task based on its priority.
match priority:
    case 'high' | 'medium' | 'low':
        # This block executes for any valid priority.
        # An 'if' statement is now used to check for time sensitivity.
        
        if time_bound == 'yes':
            # This message is for any task that requires immediate attention.
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            
        elif time_bound == 'no':
            # For non-time-bound tasks, provide different advice based on priority.
            if priority == 'high':
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
            elif priority == 'medium':
                print(f"Note: '{task}' is a medium priority task. Plan to get it done when you have a moment.")
            else:  # This handles the 'low' priority case.
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
                
        else:
            # This handles invalid 'yes' or 'no' input.
            print("Invalid input for time-bound status. Please answer with 'yes' or 'no'.")
            
    case _:
        # This default case handles any priority input that isn't 'high', 'medium', or 'low'.
        print(f"Invalid priority level '{priority}'. Please enter high, medium, or low.")