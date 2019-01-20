
from arraybag import ArrayBag
from linkbag import LinkBag

def test(bagType):
	lyst=[2013,61,1973]
	print("The list of items added is:", lyst)
	b1=bagType(lyst)
	print("Expect 3:",len(b1))
	print("Exoect the bag's string:",b1)
	print("Expect True:",2013 in b1)
	print("Expect False:",2012 in b1)
	print("Expect the items on separate lines:")
	for item in b1:
		print(item)
	b1.clear()
	print("Expect {}:",b1)
	b1.add(25)
	b1.remove(25)
	print("Expect {}:",b1)
	b1=bagType(lyst)
	b2=bagType(b1)
	print("Expect True:",b1==b2)
	print("Expect False:",b1 is b2)
	for itm in lyst:
		b1.remove(item)
	print("Expect {}:",b1)
	print("Expect crash with KeyError:")
	b2.remove(99)

if None:
	print("yeah")
test(LinkBag)
	
