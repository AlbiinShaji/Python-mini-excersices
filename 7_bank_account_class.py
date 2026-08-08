"""
Class-Based Example: BankAccount
Demonstrates OOP basics: __init__, methods, and state.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


if __name__ == "__main__":
    account = BankAccount("Alby", 1000)
    print(account)

    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)  # Should fail: insufficient funds

    print(account)
