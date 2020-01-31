import mountainRange as mr
import simulatedAnnealing as sa
import matplotlib.pyplot as plt

def main():

	m = mr.Mountain()

	sol = sa.simulatedAnnealing(m, 1000, 0, 900000)

	index = m.range.index(max(m.range))
	value = max(m.range)

	print("sol {} realSol {}".format(m.range[sol], value))

	if m.range[sol] == value:
		print("ha funcionao")

	plt.plot(m.range, label='Mountain range')
	plt.plot(sol, m.range[sol], label='simulatedAnnealing', marker='o', markersize=10, color="red")
	plt.plot(index, value, label='realSol', marker='o', markersize=10, color="purple")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()
	

if __name__ == "__main__":
    main()