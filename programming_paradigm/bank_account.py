import sys # Import the sys module for precise output control

class BankAccount:
    """
    A class to represent a bank account, encapsulating balance and banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float or int): The starting balance for the account.
                                            Defaults to 0 if not provided.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            # Using sys.stdout.write for precise output without automatic newlines
            sys.stdout.write("Warning: Initial balance must be a non-negative numeric value. Setting to 0.")
            self._account_balance = 0.0
        else:
            self._account_balance = float(initial_balance) # Store balance as a float

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float or int): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            # Using sys.stdout.write for precise output without automatic newlines
            sys.stdout.write("Error: Deposit amount must be a positive numeric value.")
            return
        self._account_balance += float(amount)
        # Formatted to ensure consistent decimal representation (e.g., 67.0)
        # Using sys.stdout.write for exact control over output, no trailing newline
        sys.stdout.write(f"Deposited: ${float(amount)}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float or int): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            # Using sys.stdout.write for precise output without automatic newlines
            sys.stdout.write("Error: Withdrawal amount must be a positive numeric value.")
            return False

        if self._account_balance >= amount:
            self._account_balance -= float(amount)
            # Formatted to ensure consistent decimal representation (e.g., 67.0)
            # Using sys.stdout.write for exact control over output, no trailing newline
            sys.stdout.write(f"Withdrew: ${float(amount)}")
            return True
        else:
            # Formatted to ensure consistent decimal representation
            # Using sys.stdout.write for exact control over output, no trailing newline
            sys.stdout.write(f"Insufficient funds. Current balance: ${float(self._account_balance)}. "
                             f"Attempted withdrawal: ${float(amount)}")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Formatted to ensure consistent decimal representation
        # Using sys.stdout.write for exact control over output, no trailing newline
        sys.stdout.write(f"Current Balance: ${float(self._account_balance)}")

