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

	def __getitem__(self,index):
		if index>self._length-1:
			print("out of range")
			return -1
		prob=self._items
		for i in range(index):
			prob=prob.next
		return prob.data

	def find(self,fdata):
		prob=self._items
		j=0
		i=0
		while prob!=None:
			i+=1
			if fdata==self._items.data:
				j+=1
				print("%5d"%i,self._items.data)
			prob=prob.next
		if j==0:
			print("not found")


if __name__=="__main__":
	node1=Node("A",None)
	node2=Node("B",node1)
	print(node2.data)
	print(node2.next.data)

	node=None
	for i in range(0,5):
		node=Node(i,node)
	print(node.next.next.data)
#	while node!=None:
#		print(node.data,end=' ')
#		node=node.next
	print()

	prob=node
	while prob!=None:
		print(prob.data,end=" ")
		prob=prob.next
	print()

	l1=Link(6,0)
	print(l1[4])
	l1.find(1)
