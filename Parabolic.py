
class Parabolic:

	def __init__(self, width=100):

		self.width  = width
		self.range = []

		for x in range(-self.width, self.width, 1): # Generating the mountain range randomly...
			
			self.range.append( (- ( x ** 2 )) + 10000)


	def energyFunction(self, x): #We're searching for the top of the range, maximize this
		return self.range[x]