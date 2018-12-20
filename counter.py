class Counter(object):
	''' sub class of object '''

	# class variables
	instances=0;

	# constructor
	def __init__(self):
		''' set up the counter '''
		Counter.instances+=1
		self.reset()

	# mutator methods
	def reset(self):
		''' set the counter to 0 '''
		self._value=0

	def increment(self,amount=1):
		''' adds amont to the counter '''
		self._value+=amount

	def decrement(self,amount=1):
		''' subtracts amount from the counter '''
		self._value-=amount

	# accessor methods
	def getValue(self):
		''' returns the counter's value '''
		return self._value

	def __str__(self):
		''' returns the sting representation of the counter '''
		return str(self._value)

	def __eq__(self,other):
		''' returns true if self equals other or false otherwise '''
		if self is other:
			print("the same")
			return True
		if type(self) != type(other):
			print("different type")
			return False
		return self._value==other._value

if __name__=="__main__":
	c1=Counter()
	c2=Counter()
	c1==c1
	c1==c2










