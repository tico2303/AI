from validator import Validator 
from preprocessing import Data
import numpy as np 

class Search(object):
	def __init__(self,data, validator):
		""" data is an instance of the Data class
		validator is an instance of the validator class initailize with a
		classifier"""

		self.Data = data
		self.validator = Validator(data)
	def search(self):
		raise NotImplemented


class ForwardSelection(Search):

	def get_features(self,node):
		results = []
		col_nums = self.data.shape[1]
		for i in range(col_nums):
			new_node = []
			new_node = [x for x in node]
			for j in range(len(node) +1):
				if 	i not in new_node:
					new_node.append(i)
					results.append(new_node)
		print "results: ", results
		#print "\n"
		return results


	def search(self):
		q = [[]]
		best_accuracy = (0,None)
		while q:
			node = q.pop()
			if len(node) == col_nums:
				break
			x = 0
			for state in get_states(node):
				accuracy = self.validator.validate()
				if best_accuracy[0] <accuracy:
					best_accuracy[0] = accuracy
					best_accuracy[1] = state
				#print state
			q.append(best_accuracy[1])	







