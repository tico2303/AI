import re
import numpy as np 
#from sklearn.preprocessing import normalize


PATTERN ='([0-9])\.([0-9]{7})e([\+\-])([0-9]{3})' 
def preprocess(filename):
	featureList = []
	DataSet = []
	features = 3
	instances = 4

	#arr = np.arange(features*instances).reshape(instances, features)
	with open(filename, 'r') as f:
		for line in f.readlines():
			instance = line.strip("\n\r  ").strip("").split(" ")
			instance = np.array([format(float(feature),'8f') for feature in instance if feature], dtype=np.float64)

			DataSet.append(instance[0])
			featureList.append(instance[1:])
		#featureList = normalize(featureList, axis=0, norm='max')
		featureList = normalize(featureList)
		DataSet = np.array(DataSet)
		print featureList.shape
		print DataSet.shape
		Data = np.insert(featureList, 0, values=DataSet, axis=1)
		print Data
		print Data.shape
		f.close()
		return Data


def normalize(X):
	max_val = np.amax(X)
	min_val = np.amin(X)
	max_val = np.amax(X)
	min_val = np.amin(X)
	X -= max_val
	X /= (max_val - min_val)
	X = np.abs(X)
	return X


def selectFeature(X, featureIndexList):

	featureIndexList.sort()
	if 0 not in featureIndexList:
		featureIndexList.insert(0,0)
	max_index = max(featureIndexList)
	if max_index > X.shape[1]:
		raise IndexError("FeatureIndex is out of range"+
						 "must be within %r but is %r"%(X.shape[1], max_index))

	# returning only the columns/features specified
	return X[:,featureIndexList]	

def classFeatureSplit(X):

	classifications = X[:,0]
	feature_nums = [x for x in range(1,X.shape[1])]
	features = np.array(X[:,feature_nums])
	return classifications, features

def testTrainSplit(data, test=0.2):
	if test > 1:
		print "Test is a precentage of total data to test on: eg. 0.2"
		exit()
	else:		
		num_samples = data.shape[0]
		test_data = data[(num_samples*(1-test)):,]
		train_data = data[(num_samples*test):,]
		print type(test_data)
		print type(train_data)
		print test_data.shape
		print train_data.shape
		print "*****"

		return test_data, train_data




if __name__ == '__main__':
	Data = preprocess("cs_170_small80.txt")
	#Data = preprocess("cs_170_large80.txt")

	#Data = preprocess("testData.txt")
	#print selectFeature(Data, [1,2])
	#print selectFeature(Data, [2])
	testTrainSplit(Data)
	#classFeatureSplit(Data)
