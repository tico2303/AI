from __future__ import print_function

class Node:
	def __init__(self,state):
		self.state = state
		self.parent = None
		self.action = None
		self.solution_path = []
		#path_cost is g(n)
		self.path_cost = None
		#goal_distance is h(n) 
		self.goal_distance = None

		self.coordinates = {}
		self.__map_index()
			
	def print_node(self):
		for li in self.state:
			print(''.join([str(i) for i in li]))

	def __map_index(self):
		if self.state != None:
			for y, i in enumerate(self.state):
				for x, j in enumerate(i):
					self.coordinates[j] =(x,y)
		else:
			self.coordinates = None
				
	def update_coordinates(self):
		self.__map_index()


	def __lt__(self, other):
		#could also add goal_distance
		""" this is used to sort PriorityQue by (path_cost) or (path_cost + goal_distance)"""
		if self.goal_distance != None:
			return (self.path_cost + self.goal_distance) < (other.path_cost + other.goal_distance)
		return self.path_cost  < other.path_cost

	def __eq__(self, other):
		""" tests for equality of Nodes based on state"""
		if isinstance(other, Node):
			return self.state == other.state


	def __repr__(self):
		st = ''
		for li in self.state:
			st += ''.join([str(i) for i in li]) +"\n"
		return "%s state: \n%s\npath_cost: %r"%(self.__class__.__name__,st, self.path_cost)

