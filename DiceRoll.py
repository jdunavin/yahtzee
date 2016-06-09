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
		values = [1 for _ in xrange(k)]
		self.NUM_DICE = k
		self.MAX_PIPS = max
		
	def roll(self):
		# Roll 'em
		# Warning: transforms values into an ndarray
		self.values = np.random.randint(1, self.MAX_PIPS, self.NUM_DICE)
		
	def toString(self):
		# returns a string representation of the dice, sorted in increasing order
		values = sorted(self.values)
		return '[' + ''.join(str(v) for v in values) + ']'
		
	def countDice(self, n)
		# return the number of dice showing the given number n
		return np.sum(values==n)