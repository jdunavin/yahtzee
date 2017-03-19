class ScoreSheet():

	SCORE_SHEET = {'Ones':0, 'Twos':0, 'Threes:'0, 'Fours':0, 'Fives':0, 'Sixes':0, '3ofK':0, '4ofK':0, 'FH':0, 'SmStrt':0, 'LgStrt':0, 'Yahtzee':0, 'Bonus':0, 'Chance':0}
	
	def clearSheet(self):
		# Set all elements to 0, clearing the scoresheet
		for key in self.SCORE_SHEET.keys():
			self.SCORE_SHEET[key] = 0
	
	def setScore(self, key, score):
		# Set an individual blank on the scoresheet to a score
		# I'll add checking for valid scores later
		try:
			self.SCORE_SHEET[key] = score
		except:
			print("Error in ScoreSheet.setScore!")
			
	def upperScore(self):
		# Total the upper half of the scoresheet, and add the bonus points
		# if they are deserved
		upperSheet = [v for v in self.SCORE_SHEET.values()[0:6]}
		score = upperSheet.sum()
		if score >= 63:
			return score + 35
		else:
			return score
			
	def setScoreSheet(self, d):
		# Accepts a dict that for now we'll trust is in the same form as
		# the score sheet - I'm sure I'll change this later when I think better of items
		self.SCORE_SHEET = d
		
	def lowerScore(self, d):
		# Total the lower half of the scoresheet
		lowerSheet = [v for v in self.SCORE_SHEET.values()[6:]]
		score = lowerSheet.sum()
		return score
		