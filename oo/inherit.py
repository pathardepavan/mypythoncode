#Salary Bank Account --> zero balance in them
#Normal Bank Account --> 500 Rs you will be fined
#Reusability
#Multiple Inheritance --> One class can inherit multiple classes
class BankAccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        #min balance should be 500
        if self.balance - amount < 500:
            raise Exception("Balance should be 500")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

class SalaryBankAccount(BankAccount):
    def __init__(self, name, balance):
        super(SalaryBankAccount, self).__init__(name, balance)

    def withdraw(self, amount):
        self.balance -= amount

acc1 = SalaryBankAccount('acc1', 1000)
acc1.deposit(500)
acc1.withdraw(500)
print(acc1.balance)
