''' This .py has some problem '''
'''							  '''
class Fab(object):

	def __init__(self,max):
		self.max=max
		self.n=0
		self.a=0
		self.b=1

	def __iter__(self):
		return self

	def next(self):
		if self.n < self.max:
			I=self.b
			self.b=self.a+self.b
			self.a=I
			self.n+=1
			return I
		raise StopIteration()


def create_counter(n):
	print("create counter")
	while True:
		yield n
		print("increment n")
		n+=1

if __name__=="__main__":
	cnt=create_counter(5)
	print(cnt)
	print(cnt)
	print(next(cnt))
	print(next(cnt))
	print(next(cnt))

	for i in Fab(10):
		print(i,end=" ")
