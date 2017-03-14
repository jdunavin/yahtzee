import numpy as np

class DiceRoll():

	NUM_DICE = 1
	MAX_PIPS = 1
	values = []
	
	""" The purpose of this class is to return a set that is a roll of k dice
	each with a value <= max."""
	# PARAMETERS:
	# k - number of dice in this roll
	# max - maximum # of pips on a die
	
	def __init__(self, k, max):
		values = [1 for _ in range(k)]
		self.NUM_DICE = k
		self.MAX_PIPS = max
		
	def roll(self, n=None):
		# Roll 'em
		# Warning: transforms values into an ndarray
		if (n != None):
			self.values = np.random.randint(1, self.MAX_PIPS, n)	
		else:
			self.values = np.random.randint(1, self.MAX_PIPS, self.NUM_DICE)
		return self.values
		
	def toString(self):
		# returns a string representation of the dice
		values = self.values
		return ''.join(str(v) for v in values)
		
	def parseRoll(self, roll):
		# Returns an integer representation of the dice		
		list = []
		if len(roll) != 5:
			return "Error in parseRoll!"
		else:
			for c in roll:
				list.append(int(c))
			return list
			
	def valueCounts(self, roll):
		# Returns a list of the counts of each die face
		values = [0,0,0,0,0,0]
		list = parseRoll(roll)
		for val in list:
			values[val-1] += 1
		return values
		
	def makeRollfromList(self, rollList):
		# Accepts an array of ints or chars and returns a string 
		# representation of the roll
		if len(rollList) != 5:
			return "Error in makeRollfromList!"
		else:
			rollStr = "".join(str(x) for x in rollList)
			return rollStr
			
	def setValues(self, roll):
		# Accepts a string representation of the dice values
		# and sets the dice to those values
		self.values = self.parseRoll(roll)
		