
from node import Node
from abstractbag import AbstractBag

class LinkBag(AbstractBag):
	def __init__(self,sourceCollection=None):
		self._items=None
		AbstractBag.__init__(self,sourceCollection)

	def __iter__(self):
		prob=self._items
		# while not prob is None:
		while prob!=None:
			yield prob._data
			prob=prob._after

	def mem(self):
		return len(self)

	def clear(self):
		self._size=0
		self=LinkBag()

	def add(self,item):
		self._items=Node(item,self._items)
		self._size+=1

	def remove(self,item):
		if not item in self:
			raise KeyError(str(item)+" not in bag")
		prob=self._items
		pprob=None
		for i in self:
			if i==item:
				break
			pprob=prob
			prob=prob._after
		if prob==self._items:
			self._items=self._items._after
		else:
			pprob._after=prob._after


if __name__=="__main__":
	l1=LinkBag()
	l1.add(1)
	l1.add(12)
	l1.add(23)
	l1.add(3)
	print(str(l1))
	l1.remove(12)
	print(str(l1))
