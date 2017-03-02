import re
import numpy as np 

class Data(object):
	def __init__(self, filename):
		self.filename = filename
		self.data = self.preprocess()
	def preprocess(self):
		featureList = []
		DataSet = []
		features = 3
		instances = 4

		with open(self.filename, 'r') as f:
			for line in f.readlines():
				instance = line.strip("\n\r  ").strip("").split(" ")
				instance = np.array([format(float(feature),'8f') for feature in instance if feature], dtype=np.float64)
				DataSet.append(instance[0])
				featureList.append(instance[1:])
			featureList = self.normalize(featureList)
			DataSet = np.array(DataSet)
			Data = np.insert(featureList, 0, values=DataSet, axis=1)
			f.close()
			return Data


	def normalize(self,X):
		max_val = np.amax(X)
		min_val = np.amin(X)
		max_val = np.amax(X)
		min_val = np.amin(X)
		X -= max_val
		X /= (max_val - min_val)
		X = np.abs(X)
		return X


	def selectFeature(self,X, featureIndexList):

		featureIndexList.sort()
		if 0 not in featureIndexList:
			featureIndexList.insert(0,0)
		max_index = max(featureIndexList)
		if max_index > X.shape[1]:
			raise IndexError("FeatureIndex is out of range"+
							 "must be within %r but is %r"%(X.shape[1], max_index))

		# returning only the columns/features specified
		return X[:,featureIndexList]	

	def classFeatureSplit(self,X):

		classifications = X[:,0]
		feature_nums = [x for x in range(1,X.shape[1])]
		features = np.array(X[:,feature_nums])
		return classifications, features


	def testTrainSplit(self,data, test=0.2):
		if test > 1:
			print "Test is a precentage of total data to test on: eg. 0.2"
			exit()
		else:		
			num_samples = data.shape[0]
			test_data = data[(num_samples*(1-test)):,]
			train_data = data[(num_samples*test):,]

			return test_data, train_data




if __name__ == '__main__':
	data = Data("cs_170_small80.txt")

	Data = data.preprocess()
	data_len = len(Data.data)
	feature_indices = []
	testTrainSplit(Data)
	#classFeatureSplit(Data)
