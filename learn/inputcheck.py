
# inputcheck(xx)中的xx参数只是一个标示, 提醒要输入了, 而不是输入的量储存在xx这个参数中

def inputcheck(label):
	''' if input number is not decimalism, input again'''

	inputnum=input(label)
	try:
		trynum=int(inputnum)
		return trynum
	except ValueError:
		print("error input:",inputnum)
		return inputcheck(label)

if __name__=="__main__":
	inputnum=inputcheck("input: ")
	print("num is:",inputnum)
