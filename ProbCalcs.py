from itertools import product
from pandas import DataFrame
from numpy import sort

class ProbTable():

	"""The purpose of this class is to calculate and return the probability of any Yahtzee roll,
	given any prior roll (or none at all). """
	
	NUM_DICE = 1
	MAX_PIPS = 1
	ROLLTABLE = []
	cols = []
	
	# PARAMETERS:
	# k - number of dice in this roll
	# max - maximum # of pips on a die
	
	def __init__(self, k, max):
	
		""" Sets up the table from which the roll probabilities will be calculated """
		
		self.NUM_DICE = k
		self.MAX_PIPS = max
		
		cols = ['die' + str(x) for x in xrange(1,NUM_DICE+1)]
		rolls = lambda x: list(product(x, repeat=NUM_DICE)
		ROLLTABLE = DataFrame(rolls(xrange(1,MAX_PIPS+1)), columns=cols)
		ROLLTABLE['key'] = ROLLTABLE.iloc[:,0:NUM_DICE].apply(lambda x: ''.join(x.map(str)), axis=1)
		ROLLTABLE['prob'] = 1 / len(ROLLTABLE)
		
		# I might want to add a value counts field, as that would make it considerably easier to find certain rolls
		
	def calcProb(roll, given):
	
		""" This function needs to accept a roll value in either numeric or string
		format, and calculate the probability of a roll, using the given as a prior if provided."""
		
		# If the roll or prior was given as a numeric, convert it
		