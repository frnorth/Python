
from arrays import Array

class AbstractArray(object):

	DEFAULT_CAPACITY=10

	def __init__(self):
		self._items=Array(AbstractArray.DEFAULT_CAPACITY)
		self._memsize=AbstractArray.DEFAULT_CAPACITY

	def __iter__(self):
		cursor=0
		while cursor < len(self):
			yield self._items[cursor]
			cursor+=1

	def mem(self):
		return self._memsize

	def checkmem(self):
		if self._size>=self._memsize:
			self._memsize=self._memsize*2
			tmp=Array(self._memsize)
			for i in range(self._size):
				tmp[i]=self._items[i]
			self._items=tmp
		if self._size<=int(self._memsize/4):
			self._memsize=int(self._memsize/2)
			tmp=Array(self._memsize)
			for i in range(self._size):
				tmp[i]=self._items[i]
			self._items=tmp

	def clear(self):
		self._size=0
		self._items=Array(AbstractArray.DEFAULT_CAPACITY)
