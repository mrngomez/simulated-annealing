
import random

class Mountain:

	def __init__(self, heigth=500,width=1000):

		self.heigth = heigth #Dimensions of the mountain range
		self.width  = width
		self.range = []

		self.range.append(random.uniform(0, self.heigth)) #First point at random heigth

		for _ in range(self.width): # Generating the mountain range randomly...
			
			step = random.uniform(0.5, 0.01) #TODO: made this variable

			# Get last value from range list and choose the next point in the vecinity
			next = random.choice( [self.range[-1] + step, self.range[-1] - step] )
			self.range.append( next )


	def energyFunction(self, x): #We're searching for the top of the range, maximize this
		return self.range[x]