
from random import random

def merge(lyst,lystCopy,left,middle,right):
	i=left
	il=left
	ir=middle+1
	while i<right+1:
		if il>middle:
			lystCopy[i]=lyst[ir]
			ir+=1
		elif ir>right:
			lystCopy[i]=lyst[il]
			il+=1
		elif lyst[il]<=lyst[ir]:
			lystCopy[i]=lyst[il]
			il+=1
		elif lyst[il]>=lyst[ir]:
			lystCopy[i]=lyst[ir]
			ir+=1
		i+=1
	for j in range(left,right+1):
		lyst[j]=lystCopy[j]
	#print(left,"\t",lyst[left:(right+1)],"\n")

def splitMerg(lyst,lystCopy,left,right):
	middle=(left+right)//2
	if right-left>1:
		splitMerg(lyst,lystCopy,left,middle)
		splitMerg(lyst,lystCopy,middle+1,right)
	merge(lyst,lystCopy,left,middle,right)

def splitMergSort(lyst):
	lystCopy=[]
	for i in range(0,len(lyst)):
		lystCopy.append(0)
	left=0
	right=len(lyst)-1
	splitMerg(lyst,lystCopy,left,right)


if __name__ == "__main__":
	lyst=[]
	for i in range(0,200):
		lyst.append(float("%.1f"%(random()*100)))
	print(lyst,"\n")
	splitMergSort(lyst)
	print(lyst,"\n")
	for i in range(1,len(lyst)):
		cc=lyst[i]-lyst[i-1]
		print("%.1f"%cc,end="")
