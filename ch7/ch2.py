class Account:
    def __init__(self, balance):
        if(balance < 0):
            print("Liquid!!!")
        self.balance = balance if balance > 0 else 0
    def credit(self, val):
        self.balance += val
    def debit(self, val):
        self.balance -= val
    def getBalance(self):
        return self.balance
    

account = Account(-2)

account.credit(100)
account.debit(9)

account.credit(28)
account.credit(3)

account.debit(16)

print(f'Balance : {account.getBalance()}')