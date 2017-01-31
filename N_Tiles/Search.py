from Node import Node
from Frontier import *
from Tree import Tree 
from copy import deepcopy

class Search(object):
	def __init__(self, problem):
		pass

	def run(self):
		pass

def SolutionPath(solnode):
	#for node in solnode.solution_path:
		#print node
	print("number of solution: ", len(solnode.solution_path))

	for i in range(0,len(solnode.solution_path)):
		print solnode.solution_path[i]
		print solnode.solution_path[i].action
		print("\n\n\n")

		
	print(solnode)
	print(solnode.action)
	print("\n\n\n")




def UniformCostSearch(problem):
		node = Node(problem.inital_state)
		node.path_cost = 0
		que = PriorityQue()
		que.push(node)
		explored = []

		while True:
			if que.is_empty():
				return "Failed"
			node = que.pop()
			print("parent:", node)
			if problem.is_goal(node.state):
				return node
			explored.append(node)
			tree = Tree(node)
			for action in problem.actions(node):
				child = tree.child_node(problem,node, action)
				print("child: ", child)
				if child not in explored:
					que.push(child)
				#elif child in and que < 


def ManhattanDistance(node, goal):
	distance = 0
	for y, _ in enumerate(node.state):
		for x, tile in enumerate(node.state[y]):
			if tile != "*":
				distance += abs(node.coordinates[tile][0] -goal.coordinates[tile][0])
				distance += abs(node.coordinates[tile][1] - goal.coordinates[tile][1])
	return distance



def AstarManhattan(problem):
	pass



def AstarMisplacedTile(problem):
	pass