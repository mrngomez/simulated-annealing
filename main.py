import mountainRange      as mr
import Parabolic          as pa
import simulatedAnnealing as sa
import matplotlib.pyplot  as plt

def main():

	#m = mr.Mountain(width = 25)
	m = pa.Parabolic()

	print("inMin {} inMax {}".format(m.inMin, m.inMax))

	sol, energy, states, temps = sa.simulatedAnnealing(m, m.inMax - 1, m.inMin, 50000) #problem, inMax, inMin, steps

	index = m.range.index(max(m.range))
	value = max(m.range)

	print("sol {} realSol {}".format(m.range[sol], value))

	if m.range[sol] == value:
		print("ha funcionao")

	plt.figure()
	plt.subplot(221) #Nrows, ncols, index
	plt.plot(m.range, label='Mountain range')
	plt.plot(sol, m.range[sol], label='simulatedAnnealing', marker='o', markersize=10, color="red")
	plt.plot(index, value, label='realSol', marker='o', markersize=10, color="purple")
	plt.title("problem range")
	plt.subplot(222)
	plt.plot(energy, label='energy', color="orange")
	plt.title("energy")
	plt.subplot(223)
	plt.plot(states, label='states', color="green")
	plt.title("states")
	plt.subplot(224)
	plt.plot(temps, label='temps', color="red")
	#plt.xscale("log")
	plt.title("temps")
	plt.show()
	

if __name__ == "__main__":
    main()