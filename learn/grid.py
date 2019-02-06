
from arrays import Array

class Grid(object):

	def __init__(self,rows,columns,fillValue=None):
		self._data=Array(rows)
		for row in range(rows):
			self._data[row]=Array(columns,fillValue)

	def getHeight(self):
		return len(self._data)

	def getWidth(self):
		return len(self._data[0])

	def __getitem__(self,indexRow):
		return self._data[indexRow]

	def __str__(self):
		result=""
		for row in range(self.getHeight()):
			for col in range(self.getWidth()):
				result+=str(self._data[row][col])+" "
			result+="\n"
		return result

if __name__=="__main__":
	g1=Grid(5,9,0)
	print(g1)
	print(g1[4][7])
