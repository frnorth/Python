
from abstractcollection import AbstractCollention

class AbstractStack(AbstractCollention):

	def __init__(self,sourcecollection=None):
		AbstractCollention.__init__(self,sourcecollection)

	def add(self,item):
		self.push(item)
