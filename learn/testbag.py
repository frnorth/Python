
from arraybag import ArrayBag
from arraysortedbag import ArraySortedBag
from linkbag import LinkBag

def test(bagType):
	lyst=[2013,61,1973,999,456,78,932,399,21,146,2000,1983]
	print("The items of lyst is:", lyst)
	b1=bagType(lyst)
	print("len(b1): Expect // 12 //",len(b1))
	print("mem alloced for b1: Expect // 20 //",b1.mem())
	print("Expect the bag's string:",b1)
	print("21 in b1: Expect // True //",21 in b1)
	print("2012 in b1: Expect // False //",2012 in b1)
	print("Expect the items by tab:")
	for item in b1:
		print(item,end="\t")
	print()
	b1.clear()
	print("b1.clear(): Expect // {} //",b1)
	b1.add(25)
	b1.remove(25)
	print("b1.add(25), b1.remove(25): Expect // {} //",b1)
	b1=bagType(lyst)
	b2=bagType(b1)
	print("b1=bagType(lyst), b2=bagType(b1), b1==b2: Expect // True //",b1==b2)
	print("b1 is b2: Expect // False //",b1 is b2)
	for item in lyst:
		b1.remove(item)
	print("b1.remove the items in lyst: Expect // {} //",b1)
	print("b2.remove(99): Expect crash with KeyError:")
	b2.remove(99)

if None:
	print("yeah")
#test(LinkBag)
#test(ArrayBag)
test(ArraySortedBag)
	
