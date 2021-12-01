import numpy as np

inp = np.loadtxt('input1st-1.txt')
inc = 0
for i in range(len(inp) - 1):
    if inp[i + 1] > inp[i]:
        inc += 1
print("1st puzzle solution: ", inc)

inc2 = 0
for i in range(len(inp) - 3):
    if sum(inp[i+1:i+4]) > sum(inp[i:i+3]):
        inc2 += 1
print("2nd puzzle solution: ", inc2)
