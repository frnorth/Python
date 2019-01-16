def inputcheck(num):
	''' if input number is not decimalism, input again'''

	inputnum=input(num)
	try:
		trynum=int(inputnum)
		return trynum
	except ValueError:
		print("error input:",inputnum)
		return inputcheck(num)

if __name__=="__main__":
	inputnum=inputcheck("input: ")
	print("num is:",inputnum)
