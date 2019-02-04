
from arraystack import ArrayStack
#from linkstack import LinkStack

def test(stackType):
	s=stackType()
	print("Length:",len(s))
	print("Empty:",s.isEmpty())
	print("Push 1-10")
	for i in range(10):
		s.push(i+1)
	print("Peeking:",s.peek())
	print("Items from bottom to top:",s)
	print("Length:",len(s))
	print("Empty:",s.isEmpty())
	theClone=stackType(s)
	print("Items in clone from bottom to top:",s)
	theClone.clear()
	print("Length of clone after clear:",len(theClone))
	print("Push 11")
	s.push(11)
	print("Poping items from top to bottom:",end="")
	while not s.isEmpty(): print(s.pop(),end=" ")
	print("\nLength:",len(s))
	print("Empty:",s.isEmpty())

test(ArrayStack)
#test(LinkStack)

