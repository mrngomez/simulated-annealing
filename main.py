import mountainRange as mr
import simulatedAnnealing as sa
import matplotlib.pyplot as plt

def main():

	m = mr.Mountain()
	sol = sa.simulatedAnnealing(m, 1000, 0, 1000, 0)
	print("sol {} realSol {}".format(sol, m.top))
	if m.range[sol] == m.top:
		print("ha funcionao")

	plt.plot(m.range, label='Mountain range')
	plt.plot(sol,     label='simulatedAnnealing')
	plt.plot(m.top,   label='realSol')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()
	

if __name__ == "__main__":
    main()