class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


def main():
    account = BankAccount("Mariam", 1000)
    print("Initial Balance:", account.get_balance())

    account.deposit(500)
    print("After deposit:", account.get_balance())

    account.withdraw(300)
    print("After withdraw:", account.get_balance())


if __name__ == "__main__":
    main()
