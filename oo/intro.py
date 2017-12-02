#Bank Account
#Operations -- withdraw, deposit, checkbalance
#Properties -- balance, name
#Entity --> Combination of both operations and properties
#class --> 
class BankAccount:
	branch = 'SBI'
	#constructor --> Initializer
	def __init__(self, name, balance):
		self.name= name
		self.balance = balance
	def __str__(self):
		return self.name + '=>' + str(self.balance)
	def __add__(self, other):
		b = self.balance + other.balance
		n = self.name
		return BankAccount(n, b)		
	
	@classmethod
	def emi_calc(cls, total, interest, duration):
		print('calculating logic here')

	@staticmethod
	def some_func():
		print('static called')
		
	def checkbalance(self):
		return self.balance
	
	def withdraw(self, amount):
		self.balance -= amount
		print("Remaining Balance:{}".format(self.balance))
	def deposit(self, amount):
		self.balance += amount
		print("Remaining Balance:{}".format(self.balance))
BankAccount.some_func()
#BankAccount.emi_calc(100000, 10, 12)
#print(BankAccount.branch)
#print(BankAccount)  	
#print(BankAccount('Account1', 1000))
#acc1 = BankAccount('acc1', 1000)
#acc2 = BankAccount('acc2', 500)
#print(acc1)
#print(acc2)
#Accessing individual properties of a object
#print(acc1.balance)
#print(acc1.name)
#print(acc2.balance)
#print(acc2.name)

#acc1.deposit(500)
#acc2.withdraw(500)
