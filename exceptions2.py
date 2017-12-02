import pdb
pdb.set_trace()
try:
	#print(1/0)
	raise ZeroDivisionError
except ZeroDivisionError as e:
	print(e)
finally:	
	print("finally called")
