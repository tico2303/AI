from Problem import *
from Node import *
from Search import *
import time
from Frontier import *

"""
inital_state = [[2, 4, 6],
				[1,'*',5],
				[3, 7, 8]]

inital_state = [
				[1,2,3],
				[4,8,"*"],
				[7, 6,5]
				]
"""
inital_state = [
				["*", 4, 8],
				[6, 3, 1],
				[7, 5, 2]
				]
test_state1 = [
				[4,2,3],
				[1,5,6],
				[7,8,"*"]
				]

test_state2 = [
				[1,2,3],
				[4,5,6],
				[7,"*",8]
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

	search = UniformCostSearch(prob)
	final_node = search.run()
	print("*"*15, "Found soution!")
	search.solution_path()
	print("time: ", time.time()-start, " \'s")


def TestFrontier():
	n1 = Node(inital_state)
	n1a = Node(inital_state)
	n1.path_cost = 1
	n1a.path_cost = 1
	n1a.goal_distance = 3

	n2 = Node(GOAL_STATE)
	n2.path_cost = 2
	n2a = Node([['testnode 2a']])
	n2a.path_cost = 2
	n2a.goal_distance = 0

	n3 = Node([["testnode3"]])
	que = PriorityQue()
	que.push(n1)
	que.push(n1a)
	que.push(n2)
	que.push(n3)

	print("*"*10, "Testing QUE")

	#if n1 in que:
		#print("Passed if el in que  Test")

	n_index = que.index(n1)
	print("testing index and its: ", n_index)
	print("geting node at index")
	#print(que[n_index])
	print("index test done")
	que[n_index] = n3
	print(que[n_index])

	## __iter__ is working
	"""
	for node in que:
		print(node)
	"""
	"""
	print("*"*10, "Testing Node")

	if n2 == n2:
		print("Passed equailty")
	else:
		print("failed equailty")	
	if n1a < n2:
		print("passed overloaded __lt__ path_cost + goal_distance")
	else:
		print("failed overloaded")	
	if n1a > n2:
		print("failed __gt__")
	else:
		print("passed __gt__")

	"""
def TestNodeNotInExplored():
	n1 = Node(inital_state)
	n2 = Node(test_state1)
	n3 = Node(test_state2)
	n4 = Node("fake")
	n = "nothing"
	que = PriorityQue()
	que.push(n1)
	que.push(n2)
	que.push(n3)
	
	assert len(que) == 3
	print("len(que): passed!")

	if n in que:
		print("n in que: Failed!")

	if n1 in que:
		print("n1 in que: passed!")

	if n4 not in que:
		print("n4 not in que: passed!")

	print("*"*10, "Testing node behavior in explored list")

	explored = []
	explored.append(n1)
	if n1 in explored:
		print("n1 in explored: passed!")

	if n1 not in explored:
		print("n1 not in explored: Failed!")


def TestAstarManhattan():
	n = Node(inital_state)
	goal = Node(GOAL_STATE)
	prob = EightTilesProblem(n, goal)
	start = time.time()

	search = AstarManhattan(prob)
	final_node = search.run()
	print("*"*15, "Found soution!")
	search.solution_path()
	print("time: ", time.time()-start, " \'s")







#TestNode()
#TestManDist()
#TestProblem()
#TestTree()
#TestProblemResult()
#TestUniformSearch()
#TestFrontier()
#TestNodeNotInExplored()
TestAstarManhattan()