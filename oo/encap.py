#Private Variable --> accessible only inside class
#Name mangling
#Public --> Any body can access
#Protected --> Conventional
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount

    def getbalance(self):
        return self.__balance

    def setbalance(self, amount):
        self.__balance = amount

acc1 = BankAccount('acc1', 1000)

