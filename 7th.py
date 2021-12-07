import numpy as np

inp = np.loadtxt('input7th.txt', delimiter=',', dtype=int)
xmin = np.min(inp)
xmax = np.max(inp)
positions = range(xmin, xmax + 1)

# Part 1
fuel = np.zeros(xmax - xmin + 1, dtype=int)
for i, pos in enumerate(positions):
    fuel[i] = np.sum(np.abs(inp-pos))
print('Fuel consumption:', np.min(fuel))

# Part 2
fuel = np.zeros(xmax - xmin + 1, dtype=int)
fuelmin = np.inf
for i, pos in enumerate(positions):
    print(i, end='\r')
    steps = np.abs(inp-pos)
    for crab in steps:
        for step in range(crab):
            fuel[i] += 1 + step
        if fuel[i] > fuelmin:
            break
    if fuel[i] < fuelmin:
        fuelmin = fuel[i]
print('Fuel consumption:', fuelmin)
