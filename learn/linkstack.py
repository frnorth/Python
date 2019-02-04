
from node import Node
from abstractstack import AbstractStack

class LinkStack(AbstractStack):

	def __init__(self,sourceCollection=None):
		self._items=None
		AbstractStack.__init__(self,sourceCollection)

	def __iter__(self):
		def visitNode(node):
			if not node is None:
				visitNode(node._after)
				tmpList.append(node._data)
		tmpList=list()
		visitNode(self._items)
		return iter(tmpList)

	
