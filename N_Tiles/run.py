from Problem import *
from Node import *
from Search import *
import time
from Frontier import *
import random
from os import system

GOAL_STATE = [[1,2,3],
			  [4,5,6],
			  [7,8,'*']]

default_puzzle = [
			  [1,2,3],
			  [4,"*",6],
			  [7,5,8]
				]

def findZero(row):
	for index, num in enumerate(row):
		if num == 0:
			row[index] = "*"
			return row
	return row

def menu():
	print("Robert's 8-Tile Puzzle solver!")

def mainMenu():
	menu()
	print("Type \"1\" to use a default puzzle or \"2\" to enter your own puzzle.")
	choice = int(raw_input())
	print("\n")
	return choice

def enterPuzzleMenu():
	print("Enter your puzzle, use a zero to represent the blank")
	row1 = raw_input("Enter first row, use spaces between numbers     ")
	row2 = raw_input("Enter second row, use spaces between numbers    ")
	row3 = raw_input("Enter third row, use spaces between numbers     ")	

	row1 = [int(num) for num in row1.split(" ")]
	row2 = [int(num) for num in row2.split(" ")]
	row3 = [int(num) for num in row3.split(" ")]

	row1 = findZero(row1)
	row2 = findZero(row2)
	row3 = findZero(row3)

	puzzle =[]
	puzzle.append(row1) 
	puzzle.append(row2) 
	puzzle.append(row3) 
	print("\n")
	return puzzle

def algorithmMenu():
	print("Enter your choice of algorithm")
	print("1. Uniform Cost Search")
	print("2. A* with MisPlaced Tile heuristic")
	print("3. A* with the Manhattan distance heuristic")
	choice = int(raw_input())
	print("\n")
	return choice	

def main():
	choice = mainMenu()
	if choice == 1:
		inital_state = default_puzzle
		algorithm = algorithmMenu()
	elif choice == 2:
		inital_state = enterPuzzleMenu()
		algorithm = algorithmMenu()

	start = Node(inital_state)
	goal = Node(GOAL_STATE)
	problem = EightTilesProblem(start, goal)

	#Uniform Cost Search
	if algorithm == 1:
		search = UniformCostSearch(problem)
	#A* MisPlaced Tile
	elif algorithm == 2:
		search = AstarMisplacedTile(problem)
	#A* Manhattan
	elif algorithm == 3:
		search = AstarManhattan(problem)

	start = time.time()
	final_node, nodes_explore, max_que_size= search.run()
	print "*"*7, "Found soution!" + "*"*6
	depth = search.solution_path()
	print "Nodes explored: ", nodes_explore
	print "Max que size: ", max_que_size
	print "Depth: ", depth
	print "time: ", round(time.time()-start, 6), "seconds"


main()
#enterPuzzleMenu()

