
from arrays import Array
from abstractstack import AbstractStack
from abstractarray import AbstractArray

class ArrayStack(AbstractStack,AbstractArray):

	def __init__(self,sourceCollection=None):
		AbstractArray.__init__(self)
		AbstractStack.__init__(self,sourceCollection)

	#def __iter__(self):
	#	cursor=0
	#	while cursor <len(self):
	#		yield self._items[cursor]
	#		cursor+=1

	def peek(self):
		return self._items[len(self)-1]

	#def clear(self):
	#	self._size=0
	#	self._items=Array(ArrayStack.DEFAULT_CAPACITY)

	def push(self,item):
		self._items[len(self)]=item
		self._size+=1
		self.checkmem()

	def pop(self):
		oldItem=self._items[len(self)-1]
		self._size-=1
		return oldItem
		self.checkmem()







