def read():
	try:
		with open('logmessages.txt', 'r') as fp:
			return fp.read()
	except Exception as e:
		return e

def write(message):
	try:
		with open('logmessages.txt','a') as fp:
			fp.write("\n"+message)
			return True
		return False
	except Exception as e:
		return False
if __name__ == '__main__':
	print(write("test"))
	print(read())
	
