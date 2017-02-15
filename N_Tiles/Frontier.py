import bisect
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

	def __iter__(self):
		for el in self.q:
			yield el

	def find_element(self, el):
		for i in self.q:
			if i == el:
				return i
			else:
				return None

	def index(self, el):
		return self.q.index(el)

	def __getitem__(self, index):
		return self.q[index]

	def __setitem__(self, index, value):
		self.q[index] = value

	def __len__(self):
		return len(self.q)

	def __contains__(self, key):
		return key in self.q

	def is_empty(self):
		if self.q:
			return False
		else:
			return True
	def pop(self):
		return self.q.pop(0)

	def push(self, node):
		#places node in shorted order
		# reduces time complexity to O(logn) in
		# average case
		
		bisect.insort(self.q, node)
	def front(self):
		"""just peek at front"""
		return self.q[0]


