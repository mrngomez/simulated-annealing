
import random
import matplotlib.pyplot as plt

class Mountain:

	def __init__(self, heigth=100,width=200):

		self.heigth = heigth #Dimensions of the mountain range
		self.width  = width
		self.range = []

		for _ in range(self.width): # Generating the mountain range randomly...
			self.range.append(random.uniform(0, self.heigth))


def main():

	m = Mountain()
	
	plt.plot(m.range, label='Mountain range')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()

if __name__ == "__main__":
    main()