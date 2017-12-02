def sum(x,y,*args):
	print(type(args))
	print(args)
	sum=0
	for num in args:
		sum+=num
	print(sum+x+y)

sum(10,20,30,40,50)

#Required Arguments
#default arguments
#keyword arguments
#variable length arguments

