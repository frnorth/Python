class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next

class Link(object):

	def __init__(self,length,data=0):
		self._length=length
		self._items=None
		for i in range(length):
			self._items=Node(data,self._items)

	def printLink(self):
		prob=self._items
		for i in range(self._length):
			print("%7d"%i,end='')
		print()
		while prob!=None:
			print("%7d"%prob.data,end='')
			prob=prob.next
		print()
		

	def __getitem__(self,index):
		if index>self._length-1:
			print("out of range")
			return -1
		prob=self._items
		while index>0:
			prob=prob.next
			index-=1
		return prob.data

	def __setitem__(self,index,sdata):
		if index>self._length-1:
			print("out of range")
			return -1
		prob=self._items
		while index>0:
			prob=prob.next
			index-=1
		prob.data=sdata

	def find(self,fdata):
		prob=self._items
		j=0
		i=0
		while prob!=None:
			if fdata==prob.data:
				j+=1
				print("%5d"%i,prob.data)
			prob=prob.next
			i+=1
		if j==0:
			print("not found")

	def replace(self,fdata,rdata):
		prob=self._items
		j=0
		i=0
		while prob!=None:
			if fdata==prob.data:
				j+=1
				prob.data=rdata
				print("%5d"%i,fdata,prob.data)
			prob=prob.next
			i+=1
		if j==0:
			print("not found")

	def insert(self,index,idata):
		if index>self._length-1:
			print("out of range")
			return -1
		prob=self._items
		if index>0 and index<self._length-1:
			while index>1:
				prob=prob.next
				index-=1
			inode=Node(idata,prob.next)
			prob.next=inode
			self._length+=1


if __name__=="__main__":

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
