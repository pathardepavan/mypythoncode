from logpackage import log
print("Before Error")
try:
	log.write("Entered the try block")
	#with open("sample10.txt","r") as fp:
	#	#Read the file
	#	content = fp.read()
	#	print(content)
	print(1/0)
except FileNotFoundError as e:
	log.write("File not found error occured")
	print("File not found error occured")
except ZeroDivisionError as e:
	log.write("Zero Division error occured")
	print("Zero Division error occured")
except Exception as e:
	log.write("Generic error occured")
	print("Generic error occured")
	print(e)
print("After Error")
