from validator import Validator 
from preprocessing import Data
import numpy as np 

class Search(object):
	def __init__(self,data, validator):
		""" data is an instance of the Data class
		validator is an instance of the validator class initailize with a
		classifier"""
		
		self.Data = data
		self.validator = validator
	def search(self):
		raise NotImplemented


class ForwardSelection(Search):

	def search(self):
		feature_indices = []
		col_nums = self.Data.data.shape[1]
		explored = []
		curr_min_cost = 9999
		q = [1]
		while len(q) >0:
			curr_feature = q.pop()
			for feature in range(curr_feature, col_nums)
				self.validator.validate






