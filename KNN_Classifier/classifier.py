from preprocessing import *
import math
import numpy as np 


class Classifer(object):
	def fit(x,y):
		raise NotImplemented
	def predict(x,y):
		raise NotImplemented

class KnearestNeighbor(Classifer):
	def __init__(self, data=None):
		if data!=None:
			self.data = data
		self.neighbors = []

	def distance(self, d1, d2):
		"""
		distance = []
		print d1.shape
		feature_indices = [x for x in range(1,d1.shape[1])]
		training_data = d1[:, feature_indices]		
		for instance in training_data:
			dist = 0
			for i,feature in enumerate(instance):
				dist += abs((d2[i] - feature)**2)
			dist = math.sqrt(dist)
			distance.append([instance,dist])
		print "distance from ", d2, " to ", instance, " is: ",dist
		return distance
		"""
		# creates a distance matrix
		return np.sqrt(((d1-d2)**2).sum(axis=1))

	def getNeighbor(self,training_data, test_instance, k=1):
		distances = []
		dist = 0
		distance = self.distance(training_data,test_instance)
		print "distance: ", distance
		#sort by distance
		
		print "distance.shape: ", distance.shape
		neighbors = []
		for i in range(k):
			indices = np.where(distance == distance.min())
			print "indices: ", indices
			row = zip(indices[0])
			neighbor = (training_data[row[0],0],distance[row[0]])
			print "neighbor: ", neighbor	
			neighbors.append(neighbors)
		self.neighbors = neighbors
		return neighbors



	def fit(self,x,y):
		""" x is the training data and y is 
		the classification """
		for feature in x:
			pass

	def predict(self,x,y):
		""" x is the training data and y is 
		the classification """



if __name__ == '__main__':
	data = preprocess("cs_170_small80.txt")	
	#classification, features = data.classFeatureSplit(data)
	training_data, test_instance = testTrainSplit(data)
	knn = KnearestNeighbor()
	#knn.distance(training_data, test_instance[0])
	
	neighbors = knn.getNeighbor(training_data,test_instance[0])
	#print neighbors






