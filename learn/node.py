class Node(object):
	def __init__(self,data,after=None):
		self._data=data
		self._after=after

class Link(object):

	def __init__(self,length=0,data=0):
		self._length=length
		self._items=None
		for i in range(length):
			self._items=Node(data,self._items)

	def printLink(self):
		if self._length==0:
			print("The Link is a None")
			return -1
		prob=self._items
		for i in range(self._length):
			print("%7d"%i,end='')
		print()
		while prob!=None:
			print("%7d"%prob._data,end='')
			prob=prob._after
		print()

	def __getitem__(self,index):
		if self._length==0:
			print("The Link is a None")
			return -1
		elif index>=self._length or index<0:
			print("out of range")
			return -1
		prob=self._items
		while index>0:
			prob=prob._after
			index-=1
		return prob._data

	def __setitem__(self,index,sdata):
		if self._length==0:
			print("The Link is a None")
			return -1
		elif index>=self._length or index<0:
			print("out of range")
			return -1
		prob=self._items
		while index>0:
			prob=prob._after
			index-=1
		prob._data=sdata

	def find(self,fdata):
		prob=self._items
		j=0
		i=0
		while prob!=None:
			if fdata==prob._data:
				j+=1
				print("%5d"%i,prob._data)
			prob=prob._after
			i+=1
		if j==0:
			print("not found")

	def replace(self,fdata,rdata):
		prob=self._items
		j=0
		i=0
		while prob!=None:
			if fdata==prob._data:
				j+=1
				prob._data=rdata
				print("%5d"%i,fdata,prob._data)
			prob=prob._after
			i+=1
		if j==0:
			print("not found")

	def insert(self,index,idata):
		prob=self._items
		if self._length==0:
			self._items=Node(idata)
		else:
			if index>self._length or index<0:
				print("out of range")
				return -1
			elif index==0:
				self._items=Node(idata,self._items)
			else:
				# mine:
				#while index>1:
				while index>1 and prob._after!=None:
					prob=prob._after
					index-=1
				prob._after=Node(idata,prob._after)
				# mine:
				#if prob._after==None:
				#	prob._after=Node(idata,None)
				#else:
				#	inode=Node(idata,prob._after)
				#	prob._after=inode
		self._length+=1

	def delete(self,index):
		prob=self._items
		if self._length==0:
			print("already empty")
		else:
			if index>=self._length or index<0:
				print("out of range")
				return -1
			elif index==0:
				self._items=self._items._after
			else:
				# mine:
				#while index>1:
				while index>1 and prob._after._after!=None:
					prob=prob._after
					index-=1
				prob._after=prob._after._after
				# mine:
				#if prob._after.after==None:
				#	prob._after=None
				#else:
				#	prob._after=prob._after.after
		self._length-=1

if __name__=="__main__":

	l0=Link()
	l0.printLink()
	print()

	l1=Link(6,0)
	l1.printLink()
	print()

	for i in range(6):
		l1[i]=i
	l1.printLink()
	print()

	l1.replace(5,66)
	l1.printLink()
	print()

	l1.insert(3,333)
	l1.printLink()
	print()

	l1.insert(7,999)
	l1.printLink()
	print()

	l1.insert(0,000)
	l1.printLink()
	l1[10]=0
	print(l1._length)
	print(l1._length,l1[9])
	print()

	l1.delete(4)
	l1.printLink()
	print()
