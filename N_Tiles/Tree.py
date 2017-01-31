from Node import *
from copy import deepcopy

class Tree:

	def __init__(self, root):
		self.root = root

	def child_node(self, problem, parent_node, action):
		""" returns node from parent given a particular action that was taken"""
		child_node = Node(problem.result(parent_node, action))
		child_node.action = action
		child_node.parent = parent_node
		child_node.solution_path = deepcopy(parent_node.solution_path)
		child_node.solution_path.append(parent_node)

		child_node.path_cost = parent_node.path_cost + problem.step_cost(parent_node, action)
		return child_node

	def expand_node(self,problem, parent_node,actionsList):
		""" returns a list of all possible children of a node given a list of actions"""
		children_list = []
		for action in actionsList:
			children_list.append(self.child_node(problem, parent_node, action))
		return children_list
