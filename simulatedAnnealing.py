
import numpy.random as rn
import math
import numpy as np

"""
The algorithm gets a problem, that must have the methon energyFunction and a range of possible inputs

"""

def simulatedAnnealing(problem, inMax, inMin, tmin=0):

	interval = inMax - inMin
	neightborhood = interval // 4
	energy = []
	states = []
	temps  = []
	i = np.nextafter(0, math.inf)
	cooldown = False

	currentState = rn.randint( inMin, inMax ) #Initial state

	while not cooldown:

		#print("cooling down: {}".format(t), end='\r', flush=True)
		i += np.nextafter(i, math.inf)
		t = 1 / i #exponential cooldown

		temps.append(t)

		currentEnergy = problem.energyFunction(currentState)
		
		nextState = rn.randint( currentState - neightborhood, currentState + neightborhood )

		nextState = max(inMin, nextState) # Bound the nextState inside the available problem's interval
		nextState = min(inMax, nextState)

		nextEnergy = problem.energyFunction(nextState)


		deltaE = nextEnergy - currentEnergy

		if deltaE > 0:
			currentState = nextState
		elif (np.exp( - deltaE / t) > rn.uniform(0,1)):
			currentState = nextState

		energy.append(problem.energyFunction(currentState))
		states.append(currentState)

		if t <= tmin: cooldown = True

	return currentState, energy, states, temps