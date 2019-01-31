
from abstractcollection import AbstractCollention

class AbstractStack(AbstractCollention):

	def __init__(self,sourcecollection):
		AbstractCollention.__init__(self,sourcecollection)

	def add(self,item):
		self.push(item)
