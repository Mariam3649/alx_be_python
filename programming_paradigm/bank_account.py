class BankAccount:
    """A simple BankAccount class."""

    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional balance (default = 0)."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print current account balance with 2 decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

