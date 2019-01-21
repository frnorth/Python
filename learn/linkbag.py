from node import Node
class LinkBag(object):
	def __init__(self,sourceCollection=None):
		self._items=None
		self._size=0
		if sourceCollection:
			for item in sourceCollection:
				self.add(item)

	def __iter__(self):
		prob=self._items
		# while not prob is None:
		while prob!=None:
			yield prob._data
			prob=prob._after

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

#		if self._items._data==item:
#			self._items=self._items._after
#		else:
#			prob=self._items
#			while prob._after!=None:
#				if prob._after._data==item:
#					prob._after=prob._after._after
#				prob=prob._after

	def isEmpty(self):
		return len(self)==0

	def __len__(self):
		return self._size

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
		

if __name__=="__main__":
	l1=LinkBag()
	l1.add(1)
	l1.add(12)
	l1.add(23)
	l1.add(3)
	print(str(l1))
	l1.remove(12)
	print(str(l1))
