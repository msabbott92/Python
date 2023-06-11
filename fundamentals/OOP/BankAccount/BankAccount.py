class BankAccount:

    accounts_total = []

    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts_total.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount <= 0:
            print("Insufficent funds")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}" )
        print(f"Interest Rate: ${self.int_rate}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def display_all(cls):
        sum = 0
        for account in cls.accounts_total:
            sum = account.balance 
        return sum


account1 = BankAccount(500, 0.01)
account2 = BankAccount(100, 0.01)


account1.deposit(60).deposit(100).deposit(150).withdraw(400).yield_interest().display_account_info()
account2.deposit(50).deposit(50).withdraw(20).withdraw(20).withdraw(20).withdraw(50).yield_interest().display_account_info()

