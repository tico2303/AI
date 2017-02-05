from Node import Node
from Frontier import *
from Tree import Tree 
from copy import deepcopy
from sets import Set

DEBUG = False

class Search(object):
	def __init__(self, problem):
		self.problem = problem
		self.solnode = None
	def solutionPath(self):
		raise NotImplementedError

	def run(self):
		raise NotImplementedError

	"""
	def solution_path(self):
		print("number of solution: ", len(self.solnode.solution_path))
		actionList = []
		if self.solnode:
			for i in range(0,len(self.solnode.solution_path)):
				print self.solnode.solution_path[i]
				print self.solnode.solution_path[i].action
				print("\n\n\n")
				if self.solnode.solution_path[i].action != None:
					actionList.append(self.solnode.solution_path[i].action)
			print(self.solnode)
			print(self.solnode.action)
			actionList.append(self.solnode.action)
			print("\n\n\n")
		print(actionList)
	"""
	def solution_path(self):
		print("Started from: ", self.problem.inital_node)
		node = self.solnode
		if node.parent == None:
			print("solnode is goal: ", node)
			return None
		else:
			actionList = []
			nodeList = []
			while node.parent != None:
				actionList.append(node.action)
				nodeList.append(node)
				node = node.parent	
			actionList.reverse()
			nodeList.reverse()

			for node in nodeList:
				print(node)
			print("\nActions taken to get to solution:")	
			for action in actionList:
				print(action)

		print("!DONE")


class UniformCostSearch(Search):
	def run(self):
		node = Node(self.problem.inital_state)
		node.path_cost = 0
		que = PriorityQue()
		que.push(node)
		explored = []

		while True:
			if que.is_empty():
				self.solnode = None
				return "Failed"
			node = que.pop()
			print("parent:", node)
			if self.problem.is_goal(node.state):
				self.solnode = node
				return node
			if node not in explored:
				explored.append(node)
				print("pushing onto explored node: ", node.state)
			print("len(explored): ", len(explored))
			print("len(que): ", len(que.q))
			tree = Tree(node)
			for action in self.problem.actions(node):
				child = tree.child_node(self.problem,node, action)
				print("child: ", child)
				#raw_input()
				if (child not in explored) and (child not in que):
					print("Child not in explored or not in que. pushing: ", child.state)
					que.push(child)
				elif child in que:
					q_index = que.index(child)
					#print("child in que index in q_index: ", q_index)
					print("que[",q_index,"].path_cost: ", que[q_index].path_cost)
					print("child.path_cost: ", child.path_cost)
					if child.path_cost < que[q_index].path_cost:
						print("*"*10, "child is > que[q_index]")
						que[q_index] = child
				print("\n\n")





class AstarManhattan(Search):

	def ManhattanDistance(self, node, goal):
		distance = 0
		for y, _ in enumerate(node.state):
			for x, tile in enumerate(node.state[y]):
				if tile != "*":
					distance += abs(node.coordinates[tile][0] -goal.coordinates[tile][0])
					distance += abs(node.coordinates[tile][1] - goal.coordinates[tile][1])
		return distance

	def run(self):
		node = Node(self.problem.inital_state)
		goal_node = Node(self.problem.goal_state)
		node.path_cost = 0
		self.problem.inital_node.path_cost =0
		node.goal_distance = self.ManhattanDistance(node, goal_node)
		self.problem.inital_node.goal_distance = node.goal_distance
		que = PriorityQue()
		que.push(node)
		explored = []

		while True:
			#print("len(que)", len(que))
			#print("len(explored)", len(explored))
			if que.is_empty():
				self.solnode = None
				return "Failed"
			node = que.pop()
			if DEBUG:
				print("parent:", node)
			if self.problem.is_goal(node.state):
				self.solnode = node
				return node
			if node not in explored:
				explored.append(node)
				if DEBUG:
					print("pushing onto explored node: ", node.state)
			if DEBUG:
				print("len(explored): ", len(explored))
				print("len(que): ", len(que.q))
			tree = Tree(node)
			for action in self.problem.actions(node):
				child = tree.child_node(self.problem,node, action)
				child.goal_distance = self.ManhattanDistance(child, goal_node)
				if DEBUG:
					print("child: ", child)
					raw_input()
				if (child not in explored) and (child not in que):
					if DEBUG:
						print("Child not in explored or not in que. pushing: ", child.state)
					que.push(child)
				elif child in que:
					q_index = que.index(child)
					#print("child in que index in q_index: ", q_index)
					if DEBUG:
						print("que[",q_index,"].path_cost: ", que[q_index].path_cost)
						print("child.path_cost: ", child.path_cost)

					if child < que[q_index]:
						if DEBUG:
							print("*"*10, "child is > que[q_index]")
						que[q_index] = child
				if DEBUG:
					print("\n\n")



class AstarMisplacedTile(Search):

	def MisplacedTileHeuristic(self,node, goal_node):
		distance = 0
		for num, coords in node.coordinates.items():
			#print("Comparing:", goal_node.coordinates[num], " to ", )
			if goal_node.coordinates[num] != node.coordinates[num]:
				distance +=1
		print distance
		return distance

	def run(self):
		node = Node(self.problem.inital_state)
		goal_node = Node(self.problem.goal_state)
		node.path_cost = 0
		self.problem.inital_node.path_cost =0
		node.goal_distance = self.MisplacedTileHeuristic(node, goal_node)
		self.problem.inital_node.goal_distance = node.goal_distance
		que = PriorityQue()
		que.push(node)
		explored = []

		while True:
			print("len(que)", len(que))
			print("len(explored)", len(explored))
			if que.is_empty():
				self.solnode = None
				return "Failed"
			node = que.pop()
			if DEBUG:
				print("parent:", node)
			if self.problem.is_goal(node.state):
				self.solnode = node
				return node
			if node not in explored:
				explored.append(node)
				if DEBUG:
					print("pushing onto explored node: ", node.state)
			if DEBUG:
				print("len(explored): ", len(explored))
				print("len(que): ", len(que.q))
			tree = Tree(node)
			for action in self.problem.actions(node):
				child = tree.child_node(self.problem,node, action)
				child.goal_distance = self.MisplacedTileHeuristic(child, goal_node)
				if DEBUG:
					print("child: ", child)
					raw_input()
				if (child not in explored) and (child not in que):
					if DEBUG:
						print("Child not in explored or not in que. pushing: ", child.state)
					que.push(child)
				elif child in que:
					q_index = que.index(child)
					#print("child in que index in q_index: ", q_index)
					if DEBUG:
						print("que[",q_index,"].path_cost: ", que[q_index].path_cost)
						print("child.path_cost: ", child.path_cost)

					if child < que[q_index]:
						if DEBUG:
							print("*"*10, "child is > que[q_index]")
						que[q_index] = child
				if DEBUG:
					print("\n\n")

