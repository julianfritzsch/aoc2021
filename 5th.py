import numpy as np
import re

fr = []
to = []

with open('input5th.txt') as f:
    for line in f:
        tmp = re.split(',| -> ', line.strip())
        fr.append([int(i) for i in tmp[:2]])
        to.append([int(i) for i in tmp[2:]])
fr = np.array(fr)
to = np.array(to)
dist = to - fr
xsize = np.max([fr[:, 0], fr[:, 1]]) + 1
ysize = np.max([fr[:, 1], to[:, 1]]) + 1
field = np.zeros((xsize, ysize))

# Part 1
for i, j in enumerate(dist):
    if j[0] == 0 or j[1] == 0:
        if j[0] > 0:
            for k in range(j[0] + 1):
                field[fr[i, 0] + k, fr[i, 1]] += 1
        elif j[0] < 0:
            for k in range(j[0], 1):
                field[fr[i, 0] + k, fr[i, 1]] += 1
        if j[1] > 0:
            for k in range(j[1] + 1):
                field[fr[i, 0], fr[i, 1] + k] += 1
        elif j[1] < 0:
            for k in range(j[1], 1):
                field[fr[i, 0], fr[i, 1] + k] += 1

print('Overlap: ', len(np.where(field > 1)[0]))

# Part 2
field = np.zeros((xsize, ysize))

for i, j in enumerate(dist):
    if j[0] == 0 or j[1] == 0:
        if j[0] > 0:
            for k in range(j[0] + 1):
                field[fr[i, 0] + k, fr[i, 1]] += 1
        elif j[0] < 0:
            for k in range(j[0], 1):
                field[fr[i, 0] + k, fr[i, 1]] += 1
        if j[1] > 0:
            for k in range(j[1] + 1):
                field[fr[i, 0], fr[i, 1] + k] += 1
        elif j[1] < 0:
            for k in range(j[1], 1):
                field[fr[i, 0], fr[i, 1] + k] += 1
    else:
        if j[0] > 0 and j[1] > 0:
            for k in range(j[0] + 1):
                field[fr[i, 0] + k, fr[i, 1] + k] += 1
        elif j[0] > 0 and j[1] < 0:
            for k in range(j[0] + 1):
                field[fr[i, 0] + k, fr[i, 1] - k] += 1
        elif j[0] < 0 and j[1] > 0:
            for k in range(j[0], 1):
                field[fr[i, 0] + k, fr[i, 1] - k] += 1
        elif j[0] < 0 and j[1] < 0:
            for k in range(j[0], 1):
                field[fr[i, 0] + k, fr[i, 1] + k] += 1

print('Overlap: ', len(np.where(field > 1)[0]))
