from classifier import KnearestNeighbor
from validator import LeaveOneOutValidator
from preprocessing import Data


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
	d = data.selectFeature(data.data, [5,3,7])
	validator = LeaveOneOutValidator(d, KnearestNeighbor)
	print validator.validate()

#TestValidatorFlow()
#TestDistance()
#TestFeatureSelection()
TestClassifier()








