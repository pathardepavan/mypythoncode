#if number is divisible by 3, print foo
# if number is divisible by 5 print bar
# else print number it self.
for x in range(1, 10):
	if x%3==0:
		print("foo")
	elif x%5==0:
		print("bar")
	else:
		print(x)

