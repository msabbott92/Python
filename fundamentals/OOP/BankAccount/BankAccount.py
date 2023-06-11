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




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0,0.01)
    

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print(self.account.balance)

    def transfer_money(self, amount, name):
        if self.account.balance - amount > 0:
            self.account.withdraw(amount)
            name.account.deposit(amount)
            
        
        

user1 = User("Matt", "matt@email.com")
user2 = User("Sarah", "sarah@email.com")

user1.make_deposit(100).display_user_balance()
user2.make_deposit(200).display_user_balance()



user2.transfer_money(50,user1)

user2.display_user_balance()
user1.display_user_balance()

