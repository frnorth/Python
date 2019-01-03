class Counter(object):

	instances=0;

	def __init__(self):
		Counter.instances+=1
		self.reset()

	def reset(self):
		self._value=0

	def increment(self,amount=1):
		self._value+=amount

	def decrement(self,amount=1):
		self._value-=amount

	def getValue(self):
		return self._value

	def __str__(self):
		return str(self._value)

	def __eq__(self,other):
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
	print(c1==c1)
	print(c1==c2)


