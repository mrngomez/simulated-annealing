import mountainRange      as mr
import Parabolic          as pa
import simulatedAnnealing as sa
import matplotlib.pyplot  as plt

def main():

	#m = mr.Mountain()
	p = pa.Parabolic()

	sol, energy, states, temps = sa.simulatedAnnealing(p, 200 - 1, 	0)

	index = p.range.index(max(p.range))
	value = max(p.range)

	print("sol {} realSol {}".format(p.range[sol], value))

	if p.range[sol] == value:
		print("ha funcionao")

	plt.figure()
	plt.subplot(221) #Nrows, ncols, index
	plt.plot(p.range, label='Mountain range')
	plt.plot(sol, p.range[sol], label='simulatedAnnealing', marker='o', markersize=10, color="red")
	plt.plot(index, value, label='realSol', marker='o', markersize=10, color="purple")
	plt.legend()
	plt.subplot(222)
	plt.plot(energy, label='energy', color="orange")
	plt.legend()
	plt.subplot(223)
	plt.plot(states, label='states', color="green")
	plt.legend()
	plt.subplot(224)
	plt.plot(temps, label='temps', color="red")
	plt.xscale("log")
	plt.legend()
	plt.show()
	

if __name__ == "__main__":
    main()