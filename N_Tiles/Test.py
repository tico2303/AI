from Problem import *
from Node import *
from Search import *
import time

"""
inital_state = [[2, 4, 6],
				[1,'*',5],
				[3, 7, 8]]

"""

inital_state = [
				[1,2,3],
				[4,8,"*"],
				[7, 6,5]
				]

GOAL_STATE = [[1,2,3],
			  [4,5,6],
			  [7,8,'*']]

def TestNode():
	n = Node(inital_state)
	goal = Node(GOAL_STATE)
	n.print_node()
	print(n.state )
	print("testing Node representation: ")
	print(n)

def TestManDist():
	n = Node(inital_state)
	goal = Node(GOAL_STATE)
	print("Finding Manhaton Distance")
	print("distance is: ", ManhattanDistance(n, goal))

def TestProblem():
	n = Node(inital_state)
	goal = Node(GOAL_STATE)
	n.print_node()
	prob = EightTilesProblem(n, goal)
	print("***Problem Actions***")
	print(prob.actions(n))		
	print("\n")
	print("\n")
	print("***Problem result***")
	print("inital_state: ")
	n.print_node()
	print("\n")


######### UP	

	#checking out of bounds UP
	print("up2")
	prob.result(n, 'up')
	print(n)
	print("\n")

######### DOWN	
	print("down1")
	prob.result(n, 'down')
	print(n)
	print("\n")



######### LEFT	
	
	#checking out of bounds LEFT	
	print("left2")
	prob.result(n, 'left')
	print("passed\n")
	print(n)
	print("\n")

######### RIGHT	
	print("right1")
	prob.result(n, 'right')
	print(n)
	print("\n")

######### is_goal Test
	print("\n")
	print("\n")
	print("**is_goal State Test**")
	print(prob.is_goal(n.state))
	print(prob.is_goal(GOAL_STATE))

def TestProblemResult():
	n = Node(inital_state)
	n.path_cost=0
	print("inital_state:")
	print(n)
	print("\n")
	print("\n")
	print("\n")
	goal = Node(GOAL_STATE)
	goal.path_cost=0
	prob = EightTilesProblem(n, goal)
	print(prob.result(n,'up'))
	print(prob.result(n,'down'))
	print(prob.result(n,'down'))


def TestTree():
	n = Node(inital_state)
	n.path_cost=0
	print(n)
	goal = Node(GOAL_STATE)
	goal.path_cost=0
	prob = EightTilesProblem(n, goal)
	print("actions: ", prob.actions(n))
	actionsList = prob.actions(n)
	tree = Tree(n)
	testList = []
	testList.append(tree.child_node(prob, n, 'up'))
	if tree.child_node(prob, n, 'up') in testList:
		print("PASSED!!!!!!!!!!")
	else:
		print("Failed!!!!!")

	print("tree.child_node: ", tree.child_node(prob, n, 'up'))
	print("tree.expand: ", tree.expand_node(prob, n,actionsList ))	

def TestUniformSearch():
	n = Node(inital_state)
	goal = Node(GOAL_STATE)
	prob = EightTilesProblem(n, goal)
	
	start = time.time()
	final_node = UniformCostSearch(prob)
	print("********FOUND GOAL NODE********\n",final_node)
	SolutionPath(final_node)
	print("time: ", time.time()-start, " \'s")

#TestNode()
#TestManDist()
#TestProblem()
#TestTree()
#TestProblemResult()
TestUniformSearch()


