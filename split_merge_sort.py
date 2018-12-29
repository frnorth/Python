
def merge(lyst,lystCopy,left,middle,right):
	i=left
	il=left
	ir=middle
	while i<=right:
		if lyst[il]<=lyst[ir]:
			lystCopy[i]=lyst[il]
			il+=1
		if lyst[il]>=lyst[ir]
			lystCopy[i]=lyst[ir]
			ir+=1
		

def splitMerg(lyst,lystCopy,left,right):
	middle=(left+right)//2
	if right-left>1:
		splitMerg(lyst,lystCopy,left,middle-1)
		splitMerg(lyst,lystCopy,middle,right)
	merge(lyst,lystCopy,left,middle,right)

def splitMergSort(lyst):
	lystCopy=[]
	for i in range(0,len(lyst)):
		lystCopy.append(0)
	left=0
	right=len(lyst)-1
	splitMerg(lyst,lystCopy,left,right)

	print(len(lyst),lystCopy)

if __name__ == "__main__":
	lyst=[5,8,4.6,8.2,1.4,9.3,3.6,4.7]
	splitMergSort(lyst)
	print(lyst)
