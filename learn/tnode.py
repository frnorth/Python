
class Tnode(object):

	def __init__(self,data,last=None,after=None):
		self._data=data
		self._last=last
		self._after=after

class Tlink(object):

	def __init__(self,length=0,data=0):
		if length<0:
			print("length need to be > 0")
			return -1
		self._length=length
		self._head=None
		self._tail=self._head
		if self._length>0:
			self._head=Tnode(data);
			self._tail=self._head
			for i in range(1,self._length):
				self._tail._after=Tnode(data,self._tail)
				self._tail=self._tail._after

if __name__=="__main__":
	tl1=Tlink(10)
	prob=tl1._head
	for i in range(10):
		prob._data=i
		print(prob._data,end="  ")
		prob=prob._after
	print()
	prob=tl1._tail
	for i in range(10):
		print(prob._data,end="  ")
		prob=prob._last
	print()
