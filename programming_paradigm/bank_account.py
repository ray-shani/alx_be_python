class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount object with an optional initial balance.

        Args:
            initial_balance (int, float): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        # Changed the encapsulated attribute name from __account_balance to __current_balance
        self.__current_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (int, float): The amount to deposit. Must be a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__current_balance += amount
        print(f"Deposited ${amount:.2f}.")
        self.display_balance()

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (int, float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__current_balance >= amount:
            self.__current_balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            self.display_balance()
            return True
        else:
            print("Insufficient funds.")
            self.display_balance()
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Displaying the value of __current_balance and using the phrase "Current Balance:"
        print(f"Current Balance: ${self.__current_balance:.2f}")