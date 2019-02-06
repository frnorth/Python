
from node import Node
from abstractstack import AbstractStack

class LinkStack(AbstractStack):

	def __init__(self,sourceCollection=None):
		self._items=None
		AbstractStack.__init__(self,sourceCollection)

	def __iter__(self):
		def visitNode(node):
			if not node is None:
				visitNode(node._after)
				tmpList.append(node._data)
		tmpList=list()
		visitNode(self._items)
		return iter(tmpList)

	def peek(self):
		if self.isEmpty():
			raise KeyError("The stack is empty.")
		return self._items._data

	def clear(self):
		self._size=0
		self._items=None

	def push(self,item):
		self._items=Node(item,self._items)
		self._size+=1

	def pop(self):
		if self.isEmpty():
			raise KeyError("The stack is empty.")
		oldItem=self._items._data
		self._items=self._items._after
		self._size-=1
		return oldItem


	
