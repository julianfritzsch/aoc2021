import numpy as np


def step(x):
    Nx, Ny = x.shape
    x += 1
    ix = np.where(x == 10)
    changed = np.zeros(x.shape, dtype=bool)
    while len(ix[0]) > 0:
        for i, j in zip(ix[0], ix[1]):
            changed[i, j] = 1
            if i != 0:
                x[i-1, j] += 1
                if j != 0:
                    x[i-1, j-1] += 1
                if j != Ny - 1:
                    x[i - 1, j+1] += 1
            if i != Nx - 1:
                x[i+1, j] += 1
                if j != 0:
                    x[i + 1, j - 1] += 1
                if j != Ny - 1:
                    x[i + 1, j + 1] += 1
            if j != 0:
                x[i, j - 1] += 1
            if j != Ny - 1:
                x[i, j + 1] += 1
        ix = np.where(np.logical_and(x > 9, np.logical_not(changed)))
    N = changed.sum()
    x[x > 9] = 0
    return x, N


inp = []
with open('input11th.txt') as f:
    for line in f:
        inp.append(line.strip())
inp = np.array([[int(i) for i in j] for j in inp])
inp2 = inp.copy()
Nflash = 0
Noct = inp.size

for i in range(100):
    inp, flash = step(inp)
    Nflash += flash

print('Number of flashes: ', Nflash)

steps = 0
flash = 0
while flash != Noct:
    inp2, flash = step(inp2)
    steps += 1

print("All synchronized after step: ", steps)
