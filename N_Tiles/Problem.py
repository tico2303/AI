from __future__ import print_function
from copy import deepcopy
import operator

class Problem(object):
	def __init__(self, init_node, goal_node):
		self.inital_state = init_node.state
		self.goal_state = goal_node.state

	def actions(self, node):
		""" list of actions that are possible at that nodes state"""
		raise NotImplementedError

	def is_goal(self, nodes_state):
		""" returns solution or not found"""
		raise NotImplementedError

	def result(self, state, action):
		""" returns the state after the action has been taken"""
		raise NotImplementedError

	def step_cost(self, node_state, action):
		"""the cost of taking the action from the node state """
		raise NotImplementedError

class EightTilesProblem(Problem):

	def actions(self, node):
		"""possible actions for EightTilesProblem ['up', 'down', 'left', 'right']"""
		actionsList = []
		#up
		if self.__is_valid(node, "up"):
			actionsList.append('up')

		#down
		if self.__is_valid(node, "down"):
			actionsList.append('down')

		#left
		if self.__is_valid(node, "left"):
			actionsList.append('left')

		#right
		if self.__is_valid(node, "right"):
			actionsList.append('right')

		return actionsList

	def __swap(self, node, from_coords, to_coords):
		""" returns the state after swap coords are tuples (x,y)"""
		# indexing for coordinates is (x,y) but for state[y][x]
		temp_node = deepcopy(node)
		temp = temp_node.state[from_coords[1]][from_coords[0]] 
		temp_node.state[from_coords[1]][from_coords[0]] = temp_node.state[to_coords[1]][to_coords[0]]
		temp_node.state[to_coords[1]][to_coords[0]] = temp
		temp_node.update_coordinates()

		return temp_node.state

	def __is_valid(self, node, action):
		""" tests for valid actions"""
		x = 0
		y = 1
		star_coords = node.coordinates["*"]
		maxleny = len(node.state)-1
		maxlenx = len(node.state[0])-1
		#test up
		if action.lower() == "up":
			if star_coords[y]-1 >= 0:
				return True
			else:
				return False

		#test down
		elif action.lower() == "down":
			if star_coords[y] +1 <= maxleny:
				return True
			else:
				return False

		# test left
		elif action.lower() == "left":
			if star_coords[x] -1 >= 0:
				return True
			else:
				return False

		#test right
		elif action.lower() == "right":
			if star_coords[x] +1 <= maxlenx:
				return True
			else:
				return False

	def is_goal(self, node_state):
		""" tests if the nodes state is the goal state"""
		for x, li in enumerate(node_state):
			for y,_ in enumerate(li):
				if node_state[x][y] != self.goal_state[x][y]:
					return False
		return True
	
	def result(self, node, action):
		""" returns a state after any valid action [up, down, left, right ] have been taken"""
		if action.lower() == 'up' and self.__is_valid(node, 'up'):
			return self.__swap(node, node.coordinates["*"], (node.coordinates["*"][0], node.coordinates["*"][1]-1))
			
		elif action.lower() == 'down' and self.__is_valid(node, 'down'):
			return self.__swap(node, node.coordinates["*"], (node.coordinates["*"][0], node.coordinates["*"][1]+1))

		elif action.lower() == 'left' and self.__is_valid(node, 'left'):
			return self.__swap(node, node.coordinates["*"], (node.coordinates["*"][0]-1, node.coordinates["*"][1]))

		elif action.lower() == 'right' and self.__is_valid(node, 'right'):
			return self.__swap(node, node.coordinates["*"], (node.coordinates["*"][0]+1, node.coordinates["*"][1]))
		else:
			return None

	def step_cost(self, node, action):
		return 1

