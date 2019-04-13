#! /usr/bin/python3
import math
from misc import listAvg

def weightAvB(a,b):
	if b == 0:
		b = 1
	c = a / b
	weight=1 / 9

	if c >= 10 / 17:
		weight = 1/7
	if c >= 2 / 3:
		weight = 1/5
	if c >= 5 / 6:
		weight=1 / 3
	if c >= 1:
		weight = 1
	if c >= 1.2:
		weight = 3
	if c >= 1.5:
		weight = 5
	if c >= 1.7:
		weight = 7
	if c >= 2:
		weight = 9
    
	return weight


class peerMatrix:
	def __init__(self, name, size=2):
		self.name = name
		self.size = size
		self.peerMatrix = []
		self.normalizedMatrix = []
		self.sum = []
		self.average = []

		for i in range(self.size):
			self.peerMatrix.append([None]*self.size)
			self.normalizedMatrix.append([None]*self.size)
			self.sum.append(0)
			self.average.append(0)

	def setPeerMatrixAt(self, x, y, value):
		self.peerMatrix[y][x] = value

	def calculateSumVector(self):
		for x in range(self.size):
			for y in range(self.size):
				self.sum[x] += self.peerMatrix[y][x]

	def calculateNormalizedMatrix(self):
		for i in range(self.size):
			for j in range(self.size):
				self.normalizedMatrix[i][j] = self.peerMatrix[i][j] / self.sum[i]
	
	def calculateAverageVector(self):
		for i in range(self.size):
			self.average[i] = listAvg(self.normalizedMatrix[i])

class avgMatrix:
	def __init__(self, vars_, avgArrays):
		self.vars_ = vars_
		self.avgs = avgArrays

	def dict(self):
		self.dict_ = {}

		for i in range(len(self.avgs)):
			self.dict_[self.vars_[i]] = self.avgs[i]

		return self.dict_

	def setWeights(self, weights):
		self.weights = []
		if type(weights) is type([]):
			for weight in weights:
				try:
					self.weights.append(float(weight))
				except Exception:
					self.weights.append(0)
			return self.weights
		return False


	def calculateYAvg(self):
		pass

	def calculateXAvg(self):
		self.xAvg = []
		avg = 0
		for i in range(len(self.avgs[0])):
			avg = 0
			for row in self.avgs:
				avg += self.weights[i] * row[i]
			self.xAvg.append(avg/len(self.avgs[i]))

	def xMatrix(self):
		self.xMatrix = []
		for i in range(len(self.avgs[0])):
			vector = []
			for row in self.avgs:
				vector.append(row[i])
			self.xMatrix.append(vector)

		return self.xMatrix


'''
def setAI():
	pm=peerMatrix("peer",2)

	x=0
	y=0
	for x in range(pm.size):
		for y in range(pm.size):
			pm.setPeerMatrixAt(x,y, weightAvB(x+1,y+1))

	pm.calculateSumVector()
	pm.calculateNormalizedMatrix()
	pm.calculateAverageVector()

	return pm
'''