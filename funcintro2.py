#define function 2 arguments and prints squares of numbers between them
def square(x,y):
	result = []
	for num in range(x,y+1):
		result.append(num**2)
	return result

print(square(1,10))






#def sum(x,y):
#	return x+y

#s = sum(10,20)
#print(s)
