
import numpy.random as rn
import math
import numpy as np

"""
The algorithm gets a problem, that must have the methon energyFunction and a range of possible inputs

"""

def simulatedAnnealing(problem, inMax, inMin, steps=50000):

	interval = inMax - inMin
	neightborhood = interval // 4
	energy = []
	states = []
	temps  = []
	tMax = 25000
	tMin = 2.5

	# precalcs...
	tFactor = - math.log(tMax/tMin)

	# Initial state
	t = tMax
	currentState = rn.randint(inMin, inMax) #Initial state

	for step in range(steps):

		currentEnergy = problem.energyFunction(currentState)
		
		nextState = rn.randint( currentState - neightborhood, currentState + neightborhood )

		nextState = max(inMin, nextState) # Bound the nextState inside the available problem's interval
		nextState = min(inMax, nextState)

		#print("currentState {} nextState {}".format(currentState, nextState))

		nextEnergy = problem.energyFunction(nextState)


		deltaE = nextEnergy - currentEnergy

		if deltaE > 0:
			currentState = nextState
		elif (np.exp( - deltaE / t) > rn.random()):
			currentState = nextState


		# Update the temp:
		t = tMax * math.exp(tFactor * step / steps)

		# Statistics for the algorithm
		temps.append(t)
		energy.append(problem.energyFunction(currentState))
		states.append(currentState)

	return currentState, energy, states, temps