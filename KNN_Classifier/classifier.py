from preprocessing import *
import math
import numpy as np 


class Classifer(object):
	def distance(self, d1,d2):
		raise NotImplemented

	def predict(x,y):
		raise NotImplemented

class KnearestNeighbor(Classifer):
	def __init__(self):
		self.neighbors = []

	def distance(self, train, test):
		# creates a distance matrix
		#featureMatrix1 will be the test vector
		featureMatrix1 = test[1:test.shape[0]]
		featureMatrix2 = train[:,1:train.shape[1]]
		return np.sqrt(((featureMatrix1-featureMatrix2)**2).sum(axis=1))
		#return np.sqrt(((d1-d2)**2).sum(axis=1))[1:]

	def NearestNeighbor(self,training_data, test_instance, k=1):
		distances = []
		dist = 0
		distance = self.distance(training_data,test_instance)
		neighbors = []
		for i in range(k):
			indices = np.where(distance == distance.min())
			row = zip(indices[0])
			neighbor = (training_data[row[0][0],0],distance[row[0]])
			neighbors.append(neighbor)
		self.neighbors = neighbors
		return neighbors

	def predict(self,train_data,test_data):
		""" x is the training data and y is 
		the classification """
		nearst_neighbor = self.NearestNeighbor(train_data, test_data)

		#returns (classification)
		return nearst_neighbor[0][0]


if __name__ == '__main__':
	from validator import LeaveOneOutValidator
	val = LeaveOneOutValidator()
	d = Data("testData.txt")
	data = d.preprocess()	
	training_data, test_instance = d.testTrainSplit(data)
	knn = KnearestNeighbor()
	dist = knn.distance(training_data, test_instance[0])
	print "distance: ", dist	






