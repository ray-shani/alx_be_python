class BankAccount:
    def __init__(self, initial_balance=0):
      
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulation: use a private attribute

    def deposit(self, amount):
     
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        print(f"Deposited ${amount:.2f}.")
        self.display_balance()

    def withdraw(self, amount):
      
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            self.display_balance()
            return True
        else:
            print("Insufficient funds.")
            self.display_balance()
            return False

    def display_balance(self):
        
        print(f"Current balance: ${self.__account_balance:.2f}")