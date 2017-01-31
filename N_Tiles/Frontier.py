
class Frontier(object):
	def __init__(self):
		self.q = []
	def is_empty(self):
		pass
	def pop(self):
		pass
	def push(self):
		pass

class PriorityQue(Frontier):

	def is_empty(self):
		if self.q:
			return False
		else:
			return True
	def pop(self):
		return self.q.pop(0)

	def push(self, node):
		self.q.append(node)
		self.q.sort()

