from arrays import Array
class ArrayBag(object):
	DEFAULT_CAPACITY=10

	def __init__(self,sourceCollection=None):
		self._items=Array(ArrayBag.DEFAULT_CAPACITY)
		self._size=0
		if sourceCollection:
			for item in sourceCollection:
				self.add(item)

	def isEmpty(self):
		return len(self)==0

	def __len__(self):
		return self._size

	def clear(self):
		slef._size=0
		self._items=Array(ArrayBag.DEFAULT_CAPACITY)

	def add(self,item):
		self._items[len(self)]=item
		self._size+=1

	def __iter__(self):
		cursor=0
		while cursor < len(self):
			yield self._items[cursor]
			cursor+=1

	def __str__(self):
		return "{"+",".join(map(str,self))+"}"

if __name__=="__main__":
	a1=ArrayBag()
	print(a1.isEmpty(),end="\n\n")

	a1.add(10)
	print(a1._items[0])
	try:
		print(a1[0])
	except TypeError:
		print("TypeError",end="\n\n")

	# test the __iter__
	for i in range(5):
		a1.add(i)
	for j in a1:
		print(j,end="  ")
	print("\n")

	# test __str__
	print(",".join("hhhh"))
	print(str(a1))


