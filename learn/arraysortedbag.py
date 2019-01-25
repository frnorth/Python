
from arraybag import ArrayBag

class ArraySortedBag(ArrayBag):

	def __init__(self,sourceCollection=None):
		ArrayBag.__init__(self,sourceCollection)

	def __contains__(self,item):
		left=0
		right=len(self)-1
		while left<=right:
			midPoint=(left+right)//2
			if self._items[midPoint]==item:
				return True
			elif self._items[midPoint]>item:
				right=midPoint-1
			else:
				left=midPoint+1
		return False

	def add(self,item):
		if self.isEmpty() or item >=self._items[len(self)-1]:
			ArrayBag.add(self,item)
		else:
			targetIndex=0
			while item>self._items[targetIndex]:
				targetIndex+=1
			for i in range(len(self),targetIndex,-1):
				self._items[i]=self._items[i-1]
			self._items[targetIndex]=item
			self._size+=1
		self.checkmem()

	def __eq__(self,other):
		if self is other:
			return True
		if type(self)!=type(other) or len(self)!=len(other):
			return False
		for i in range(len(self)):
			if self._items[i]!=other._items[i]:
				return False
		return True










