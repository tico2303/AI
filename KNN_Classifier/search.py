from validator import Validator 
from preprocessing import Data
import numpy as np 
from copy import deepcopy

class Search(object):
	def __init__(self,data, validator):
		""" data is an instance of the Data class
		validator is an instance of the validator class initailize with a
		classifier"""

		self.data = data
		self.validator = validator


	def search(self):
		raise NotImplemented


class ForwardSelection(Search):

	def get_features(self,node):
		results = []
		col_nums = self.data.data.shape[1]
		for i in range(1,col_nums):
			new_node = []
			new_node = [x for x in node]
			for j in range(len(node) +1):
				if 	i not in new_node:
					new_node.append(i)
					new_node.sort()
					if new_node not in results:
						results.append(new_node)
		return results

	def set_best_accuracy(self, best,accuracy,state):
		if best[0]<= accuracy:
			best[0] = accuracy
			best[1] = state
		return best

	def search(self):
		q = [[]]
		best_accuracy = [0,None]
		col_nums = self.data.data.shape[1]
		print "Beginning search:"
		while q:
			node = q.pop(0)
			if node == None:
				print "Best feature subset was ", best_accuracy[1], " with a accuracy of ", best_accuracy[0]
				break

			local_best = [0, None]
			for state in self.get_features(node):
				self.validator.data = self.data.selectFeature(self.data.data, state)
				accuracy = self.validator.validate()
				if 0 in state:
					state.remove(0)
				print "Using feature(s) ", state, " accuracy is ", accuracy*100
				local_best = self.set_best_accuracy(local_best, accuracy, state)
				best_accuracy = self.set_best_accuracy(best_accuracy, accuracy, state)

			if local_best[1] != None:
				print "Feature set ", local_best[1], " was best, accuracy is ", local_best[0]*100, "\n\n"

			q.append(local_best[1])	

		print "Finished!\n"


class BackwardsElimination(Search):
	def get_features(self, node):
		results = []
		col_nums = self.data.data.shape[1]

		for i in range(len(node)):

			new_node = []
			new_node = [x for x in node]
			new_node.pop(i)
			results.append(new_node)
		"""		
		print "results: "	
		for r in results:
			print r
		print "\n\n"
		"""
		return results
		
	def set_best_accuracy(self, best,accuracy,state):

		if best[0]<= accuracy:
			best[0] = accuracy
			best[1] = state
		return best

	def search(self):
		best_accuracy = [0,None]
		col_nums = self.data.data.shape[1]

		#start with full q
		q = [[x for x in range(1,col_nums)]]

		while q:
			node = q.pop(0)

			if node == None:
				print "Best feature subset was ", best_accuracy[1], " with a accuracy of ", best_accuracy[0]*100
				return best_accuracy

			local_best = [0,None]
			for state in self.get_features(node):
				if state:
					self.validator.data = self.data.selectFeature(self.data.data, state)
					accuracy = self.validator.validate()
					if 0 in state:
						state.remove(0)
						
					print "Using feature(s) ", state, " accuracy is ", accuracy*100
					local_best = self.set_best_accuracy(local_best, accuracy, state)
					best_accuracy = self.set_best_accuracy(best_accuracy, accuracy, state)

			if local_best[1] != None and local_best[0] !=0:
				print "Feature set ", local_best[1], " was best, accuracy is ", local_best[0]*100, "\n\n"

			q.append(local_best[1])























