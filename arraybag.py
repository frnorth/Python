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

	def __add__(self,other):
		result=ArrayBag(self)
		for item in other:
			result.add(item)
		return result

	def __eq__(self,other):
		if self is other:
			return True
		if type(self)!=type(other) or len(self)!=len(other):
			return False
		for item in self:
			if not item in other:
				return False
		return True			

	def remove(self,item):
		if not item in self:
			raise KeyError(str(item)+"not in bag")
		targetIndex=0
		for targetItem in self:
			if targetItem == item:
				break
			targetIndex+=1
		for i in range(targetIndex,len(self)-1):
			self._items[i]=self._items[i+1]
		self._size-=1
		if self._size<ArrayBag.DEFAULT_CAPACITY/2+1:
			tmp=Array(self._size,0)
			for i in range(self._size):
				tmp[i]=self._items[i]
			self._items=tmp

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
	for i in range(3):
		a1.add(i)
	for j in a1:
		print(j,end="  ")
	print("\n")

	# test __str__
	print(",".join("hhhh"))
	print(str(a1),end="\n\n")

	# test __add__
	a2=a1
	a3=a1+a2
	print(str(a3),end="\n\n")

	#test __eq__
	print(a1==a1)
	print(a1==a2)
	print(a1==a3,end="\n\n")

	#test remove ?
	a3.remove(1)
	a3.remove(2)
	a3.remove(0)
	a3.remove(1)
	a3.remove(10)
	a3.remove(10)
	print(str(a3))
	print(len(a3))
	print()
