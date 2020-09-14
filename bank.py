class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposite(self, cash):
        self.balance += cash

    def withdraw(self, cash):
        self.balance -= cash

        if (self.balance < 0):
            self.overdraft_fees += 35
        return cash

my_account = BankAccount("saving")

my_account.deposite(500)
print('my {} balance is now: ${}'.format(my_account.kind, my_account.balance))

my_account.withdraw(120)
print('my {} balance is now: ${}'.format(my_account.kind, my_account.balance))

my_account.withdraw(1000)
print('my overdraft fee is {}, my {} balance is now: ${}'.format(my_account.overdraft_fees, my_account.kind, my_account.balance))
