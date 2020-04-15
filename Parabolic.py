
class Parabolic:

	def __init__(self, width=500):

		self.width  = width
		self.inMin = -self.width
		self.inMax =  self.width
		self.range = []

		for x in range(self.inMin, self.inMax, 1): # Generating the mountain range randomly...
			
			self.range.append( (- ( x ** 2 )) + 10000)


	def energyFunction(self, x):
		return - self.range[x]