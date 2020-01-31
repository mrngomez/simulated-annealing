
import random
import math

"""
The algorithm gets a problem, that must have the methon energyFunction and a range of possible inputs

tmax, tmin, and in the future cooling rate

"""

def simulatedAnnealing(problem, inMax, inMin, tmax, tmin=10):

	interval = inMax - inMin
	neightborhood = interval // 5

	currentState = random.randint( inMin, inMax ) #Initial state

	print("Begin simulatedAnnealing with tmax: {} tmin: {}".format(tmax, tmin))

	for t in range(tmax, tmin, -1):

		#print("cooling down: {}".format(t), end='\r', flush=True)

		currentEnergy = problem.energyFunction(currentState)
		
		nextState = random.randint( currentState - neightborhood, currentState + neightborhood )

		nextState = max(inMin, nextState) # Bound the nextState inside the available problem's interval
		nextState = min(inMax, nextState)

		nextEnergy = problem.energyFunction(nextState)

		deltaE = nextEnergy - currentEnergy

		if deltaE > 0:
			currentState = nextState
		elif (math.exp( - deltaE / t) > random.random()):
			currentState = nextState

	return currentState # This is X, not Y!