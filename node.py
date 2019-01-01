class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next

if __name__=="__main__":
	node1=Node("A",None)
	node2=Node("B",node1)
	print(node2.data)
	print(node2.next.data)

	node=None
	for i in range(0,5):
		node=Node(i,node)
	print(node.next.next.data)
	while node!=None:
		print(node.data,end=' ')
		node=node.next
	print()
