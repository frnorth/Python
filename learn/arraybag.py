
from arrays import Array
from abstractbag import AbstractBag
from abstractarray import AbstractArray

class ArrayBag(AbstractBag,AbstractArray):
	# DEFAULT_CAPACITY=10

	def __init__(self,sourceCollection=None):
		AbstractArray.__init__(self)
		AbstractBag.__init__(self,sourceCollection)

	#def __iter__(self):
	#	cursor=0
	#	while cursor < len(self):
	#		yield self._items[cursor]
	#		cursor+=1

	#def clear(self):
	#	self._size=0
	#	self._items=Array(ArrayBag.DEFAULT_CAPACITY)

	def add(self,item):
		self._items[len(self)]=item
		self._size+=1
		self.checkmem()

#	def checkmem(self):
#		if self._size>=self._memsize:
#			self._memsize=self._memsize*2
#			tmp=Array(self._memsize)
#			for i in range(self._size):
#				tmp[i]=self._items[i]
#			self._items=tmp
#		if self._size<=int(self._memsize/4):
#			self._memsize=int(self._memsize/2)
#			tmp=Array(self._memsize)
#			for i in range(self._size):
#				tmp[i]=self._items[i]
#			self._items=tmp

	def remove(self,item):
		if not item in self:
			raise KeyError(str(item)+" not in bag")
		targetIndex=0
		for targetItem in self:
			if targetItem == item:
				break
			targetIndex+=1
		for i in range(targetIndex,len(self)-1):
			self._items[i]=self._items[i+1]
		self._size-=1
		self.checkmem()

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
	print(a1,end="\n\n")

	# test __add__
	a2=a1
	a3=a1+a2
	print(a3,end="\n\n")

	#test __eq__
	print(a1==a1)
	print(a1==a2)
	print(a1==a3,end="\n\n")

	#test remove ?
	a3.remove(1)
	a3.remove(2)
	a3.remove(0)
	a3.remove(0)
	a3.remove(1)
	a3.remove(10)
	a3.remove(10)
	print(a3)
	print(len(a3))
	print(len(a3._items))
	print(a3._memsize)
	a3=a3+a1+a1+a1
	print(a3)
	print(len(a3))
	print(len(a3._items))
	print(mem(a3))

	c1=ArrayBag()
	for i in range(20):
		c1.add('ha')
	print(c1,len(c1._items))
	print()
