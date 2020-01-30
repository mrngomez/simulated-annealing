
import sys
import random
import math

"""
The algorithm gets a problem, that must have the methon energyFunction and a range of possible inputs

tmax, tmin, and in the future cooling rate

"""

def simulatedAnnealing(problem, inMax, inMin, tmax, tmin):

	currentState = random.randint( inMin, inMax ) #Initial state

	for t in range(tmax, tmin):

		currentEnergy = problem.energyFunction(currentState)
		
		nextState = random.randint( inMin, inMax )

		nextEnergy = problem.energyFunction(nextState)

		deltaE = nextEnergy - currentEnergy

		if deltaE > 0:
			currentState = nextState
		elif (math.exp(deltaE / t) > random.uniform(0, 1)):
			currentState = nextState

	return currentState # This is X, not Y!