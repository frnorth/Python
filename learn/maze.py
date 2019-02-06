
from grid import Grid
from arraystack import ArrayStack

f=open("data.txt",'r')
s=f.read()
f.close()

for i in range(len(s)):
	print(s[i],end="")
g1=Grid(15,15,0)

enterPointRow=2
enterPointCol=0
exitPointRow=14
exitPointCol=10
for i in range(15):
	for j in range(15):
		block=s[i*30+2*j]
		if block == '*':
			g1[i][j]=1
		if block == ' ':
			g1[i][j]=0

#for i in range(15):
#	print(g1[2][i])

for i in range(15):
	for j in range(15):
		print (g1[i][j],end=" ")
	print()

sRow=ArrayStack()
sCol=ArrayStack()
svalue=ArrayStack()

lastRow=enterPointRow
lastCol=enterPointCol

sRow.push(enterPointRow)
sCol.push(enterPointCol)
svalue.push(2)

sRow.push(enterPointRow)
sCol.push(enterPointCol+1)
svalue.push(2)

while sRow.peek()!=exitPointRow or sCol.peek()!=exitPointCol:
#for i in range(19):
	row=sRow.peek()
	col=sCol.peek()
	crosssite=0
	#print(g1[row][col-1])
	#print(g1[row+1][col])
	#print(g1[row][col+1])
	#print(g1[row-1][col])
	if g1[row][col-1]==0:
		if row!=lastRow or (col-1)!=lastCol:
			sRow.push(row)
			sCol.push(col-1)
			crosssite+=1
	if g1[row+1][col]==0:
		if (row+1)!=lastRow or col!=lastCol:
			sRow.push(row+1)
			sCol.push(col)
			crosssite+=1
	if g1[row][col+1]==0:
		if row!=lastRow or (col+1)!=lastCol:
			sRow.push(row)
			sCol.push(col+1)
			crosssite+=1
	if g1[row-1][col]==0:
		if (row-1)!=lastRow or col!=lastCol:
			sRow.push(row-1)
			sCol.push(col)
			crosssite+=1

	print(len(svalue))
	print(crosssite)

	if crosssite>1:
		for i in range(crosssite):
			svalue.push(3)
		lastRow=row
		lastCol=col

	elif crosssite==1:
		svalue.push(2)
		lastRow=row
		lastCol=col

	elif crosssite==0:
		while svalue.peek()!=3:
			svalue.pop()
			sRow.pop()
			sCol.pop()
		svalue.pop()
		sRow.pop()
		sCol.pop()
		xTmp=list()
		yTmp=list()
		while svalue.peek()!=2:
			xTmp.append(sRow.pop())
			yTmp.append(sCol.pop())
			svalue.pop()
		lastRow=sRow.peek()
		lastCol=sCol.peek()
		for i in range(len(xTmp)):
			sRow.push(xTmp[i])
			sCol.push(yTmp[i])
			svalue.push(3)

while svalue.pop():
	g1[sRow.pop()][sCol.pop()]=2

print(g1)

