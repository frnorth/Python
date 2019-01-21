class SavingsAccount(object):
	''' a class for saving account '''
	def __init__(self,name,pin,balance=0.0):
		self._name=name
		self._pin=pin
		self._balance=balance
	def __lt__(self,other):
		return self._name<other._name

if __name__=="__main__":
	s1=SavingsAccount("Tom",100)
	s2=SavingsAccount("Jack",101,2)
	print(s1<s2)
	print(s1>s2)
	print(s1==s2)
	print(s1._name)
