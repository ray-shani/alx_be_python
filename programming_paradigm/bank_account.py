class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount object with an optional initial balance.

        Args:
            initial_balance (int, float): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
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
        # This line is responsible for the output, and it prints only once per call.
        print(f"Deposited: ${amount:.1f}")

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
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__current_balance:.2f}")