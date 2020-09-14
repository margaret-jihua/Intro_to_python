class BankAccount():
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if (self.pin == pin):
            if (self.balance < amount):
                print("Sorry, you don't have enough balance.")
            elif (self.balance == amount):
                print("Your account is now empty.")
            else:
                self.balance -= amount
                print("Your current balance is {}.".format(self.balance))
            return 
        else:
            print("The pin is incorrect")

my_account = BankAccount("saving",778)

my_account.deposite(500)
print('my {} balance is now: ${}'.format(my_account.kind, my_account.balance))

my_account.withdraw(120,887)
# print('my {} balance is now: ${}'.format(my_account.kind, my_account.balance))

# my_account.withdraw(1000)
# print('my overdraft fee is {}, my {} balance is now: ${}'.format(my_account.overdraft_fees, my_account.kind, my_account.balance))

my_account.withdraw(1000,778)
my_account.withdraw(50,778)