from classifier import KnearestNeighbor
import numpy as np

class Validator(object):
	def validate(self):
		raise NotImplemented

class LeaveOneOutValidator(Validator):
	def __init__(self, data, Classifier):
		self.classifier = Classifier()
		self.data = data
	def leaveOneOut(self, data, row):
		num_rows = data.shape[0]
		test_data = data[row,:]
		train_data = np.delete(data,row,0)

		return test_data, train_data

	def validate(self):
		correct_predictions = 0
		total_instances = len(self.data)
		for i in range(len(self.data)):
			test, train = self.leaveOneOut(self.data,i)
			classification = self.classifier.predict(train, test)
			if classification == test[0]:
				correct_predictions +=1
		accuracy_score = (float(correct_predictions)/float(total_instances))
		print "*"*30
		print "precentage correct: ",accuracy_score
		print "*"*30
		print "\n\n"
		return accuracy_score
