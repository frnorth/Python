def binarySearch(target, sortedLyst):
	left = 0
	right = len(sortedLyst) - 1
	while left <= right:
		midpoint = (left+right) // 2
		if target == sortedLyst[midpoint]:
			return midpoint
		elif target < sortedLyst[midpoint]:
			right = midpoint -1
		else:
			left = midpoint + 1
	return -1

if __name__ == "__main__":
	list1=[1,2,3,5,7,9,15,25,42]
	print(binarySearch(42,list1))
