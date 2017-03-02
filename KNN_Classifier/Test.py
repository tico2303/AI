from classifier import KnearestNeighbor
from validator import LeaveOneOutValidator
from search import ForwardSelection
from search import BackwardsElimination
from preprocessing import Data
import time

def TestValidatorFlow():
	data = Data("cs_170_small80.txt")
	validator = LeaveOneOutValidator(data.data, KnearestNeighbor)
	precentage_correct = validator.validate()
def TestDistance():
	data = Data("testData.txt")
	validator = LeaveOneOutValidator(data.data, KnearestNeighbor)
	d = data.preprocess()
	test, train = validator.leaveOneOut(d, 0)
	knn = KnearestNeighbor()
	print "test: ", test
	print "train: \n", train

	print "distance: ",  knn.distance(train, test)
	print "\n\n"

def TestFeatureSelection():
	data = Data("cs_170_small80.txt")
	dat = data.preprocess()
	print dat.shape
	print "dat type: ", type(dat)
	col_nums = dat.shape[1]
	feature_indices = []
	for d in range(col_nums):
		feature_indices.append(d)
		print data.selectFeature(dat,feature_indices )

def TestClassifier():
	data = Data("cs_170_small80.txt")
	start = time.time()
	d = data.selectFeature(data.data, [0,5,3,7])
	validator = LeaveOneOutValidator(d, KnearestNeighbor)
	print validator.validate()
	print "time: ", time.time() -start

def TestForwardSearch():
	data = Data("cs_170_small80.txt")
	start = time.time()
	validator = LeaveOneOutValidator(data.data, KnearestNeighbor)
	fwdSlct = ForwardSelection(data, validator)	
	fwdSlct.search()
	print "time: ", time.time() - start

def TestBackwardsSearch():
	data = Data("cs_170_small80.txt")
	start = time.time()
	validator = LeaveOneOutValidator(data.data, KnearestNeighbor)
	backEl = BackwardsElimination(data, validator)	
	backEl.search()
	print "time: ", time.time() - start


def TestMenu():
	print "Welcome to Robert's Nearest Neigbhor Feature Search Algorithm"
	filename = raw_input("Enter filename to data: ")
	data = Data(filename)

	validator = LeaveOneOutValidator(data.data, KnearestNeighbor)
	print "Choose the Algorithm you'd like to run: (eg. 1)"
	print "1. Forward Selection"
	print "2. Backward Elimination"

	algorithm_choice = int(raw_input())

	if algorithm_choice == 1:
		algorithm = ForwardSelection(data, validator)
	elif algorithm_choice == 2:
		algorithm = BackwardsElimination(data, validator)

	print "This dataset has ", data.data.shape[1], " features and ", data.data.shape[0], " instances"
	algorithm.search()






#TestValidatorFlow()
#TestDistance()
#TestFeatureSelection()
#TestClassifier()
#TestForwardSearch()
#TestBackwardsSearch()
TestMenu()











