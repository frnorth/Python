'''
count the Fibonacci times
'''

from counter import Counter

def fib(n,c_counter):
	''' Count the number of calls of the Fibonacci '''
	c_counter.increment()
	if n<3:
		return 1
	else:
		return fib(n-1,c_counter)+fib(n-2,c_counter)

problemInitSize=2
print("%12s%15s"%("Problem Size","Calls"))
for count in range(5):
	counter=Counter()
	fib(problemInitSize,counter)
	print("%12d%15s"%(problemInitSize,counter))
	problemInitSize*=2
