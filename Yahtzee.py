import random
import pandas as pd
from operator import itemgetter

class Dice():

	""" This class simulates a die being thrown that can take values 1-6.
	The player has the option to freeze dice at the end of each roll depending
	on his or her desired strategy. """

    frozen = False
    value = 0

    def __init__(self, fr):
        self.frozen = fr
        self.value = 0

    def roll(self):
	# Returns the previous value if frozen, returns a new generated value if not.
    if self.frozen:
            return self.value
        else:
            self.value = random.randint(1,6) 
            return self.value
    
    def freeze(self):
		# Freeze the die and prevent it from being rerolled
		self.frozen = True
        
    def getStatus(self):
        # Return the frozen state of the die.
		return self.frozen
		
# End Dice class

class ScoreSheet():
    
	""" This class implements a Yahtzee scoresheet as a Pandas dataframe.
	This is probably swatting flies with a sledge hammer but it works. They're small
	so an array of them could probably be used later to accommodate multiple computer players. """
	
	# These two separate the scoresheet into the customary parts
    upperblanks = ['Ones','Twos','Threes','Fours','Fives','Sixes']
    lowerblanks = ['3ofAKind','4ofAKind', 'FullHouse', 'SmStraight','LgStraight','Yahtzee','YahtzeeBonus','Chance']
	
	# Allows me to alternately treat the scoresheet as a whole
    blanks = upperblanks + lowerblanks
	
	# Assign the dataframe and initialize it
    scores = pd.DataFrame(columns=['score','filled'], index=blanks)
    scores['score'] = 0
    scores['filled'] = False
    
	# Takes a score and a label and fills the labeled row in the scoresheet with the score,
	# and marking the blank as filled
    def fillScore(self, x, s):
        self.scores.loc[s, 'score'] = x
        self.scores.loc[s, 'filled'] = True

    # Takes a score label and returns the associated score    
    def getScore(self, s):
        return self.scores.loc[s,'score']
    
	# Reset a scoresheet to its initial state
    def clearScores(self):
        self.scores['score'] = 0
        self.scores['filled'] = False
     
	# Takes a label and resets the single line so labelled on the scoresheet to its initial state 
    def clearScore(self, s):
        self.scores.loc[s, 'score'] = 0
        self.scores.loc[s, 'filled'] = False
    
	# Takes a label and returns the so-labelled row's filled state
    def scoreFilled(self, s):
        return self.scores.loc[s, 'filled']
    
	# Returns the total score of the upper half of the score sheet, with applicable bonuses
    def upperHalf(self):
        s = sum(self.scores.loc[self.upperblanks, 'score'])
        if (s >= 63):
            return s + 35
        else: 
            return s
    
	# Returns the total score of the lower half of the score sheet
    def lowerHalf(self):
        s = sum(self.scores.loc[self.lowerblanks, 'score'])
        return s

# End ScoreSheet class

# BEGIN NEEDED FUNCTIONS
def checkFullHouse(values):
	
	""" Takes a set of 2-tuples representing dice counts, and checks to see if it 
	results in a Full House == 3 of a kind + a pair """
	
	ok3 = False # Did you get 3 of a kind?
	ok2 = False # Did you get a pair?
	
	for d,v in values:
		if v = 3:
			ok3 = True
		elif v = 2:
			ok2 = True
		if ok3 && ok2:  # Stop, we got it
			break
	
	return ok3 && ok2  # Only returns true if we found three of one value and two of another

	
# --- NOW THE FUN BEGINS --- 

""" This is where the game starts to be implemented. My eventual goal is to functionalize strategies and pit
them against each other in a simulation, to attempt to divine what (if any) strategies result in a
win percentage greater (or maybe less) than random. """

# Create five unfrozen dice
dice = [Dice(False) for _ in xrange(5)]

# Create a scoresheet for this player
scoresheet = ScoreSheet()

# roll the dice and store the results in an array
currValues = []

for d in dice:
	currValues.extend([d.roll()])
	rollTest = rollTest + " " + str(d.value)

# Test lines, remove later or pretty up	
print rollTest
print currValues

# Count the values - # of 1s, # of 2s, etc - store them as an array of 2-tuples
valueCounts = [0 for x in xrange(1,7)]
valueKeys = [1,2,3,4,5,6]
	
for j in valueKeys:
    valueCounts[j-1] = currValues.count(j)

thisrollValues = zip(valueKeys, valueCounts)

# Sort the die values by count
sortedValues = sorted(thisrollValues, key=itemgetter(1), reverse=True)

# Strategy point 1: Greedily check for a scoring play in the lower half
