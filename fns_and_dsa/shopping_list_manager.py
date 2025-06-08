def display_menu():
    """Prints the main menu for the Shopping List Manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list application."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            # Display the shopping list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            print("--------------------------")

        elif choice == '4':
            print("Goodbye! Exiting the Shopping List Manager.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()