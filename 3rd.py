import numpy as np
# Part 1

with open('input3rd.txt') as f:
    inp = f.readlines()

for i in range(len(inp)):
    inp[i] = inp[i].rstrip()

gamma = ''
N = len(inp)
for i in range(len(inp[0])):
    sum = 0
    for j in range(N):
        sum += int(inp[j][i])
    gamma += str(sum // (N // 2))

eta = ''
for i in gamma:
    eta += str(1-int(i))

print('Power consumption: ', int(gamma, 2) * int(eta, 2))

# Part 2
ox = inp.copy()
ixo = 0
while len(ox) > 1:
    sum = 0
    for j in range(len(ox)):
        sum += int(ox[j][ixo])
    mco = str(sum // int(np.ceil(len(ox) / 2)))
    ixd = []
    for i in range(len(ox)):
        if ox[i][ixo] != mco:
            ixd.append(i)
    for i in sorted(ixd, reverse=True):
        ox.pop(i)
    ixo += 1

co = inp.copy()
ixc = 0
while len(co) > 1:
    sum = 0
    for j in range(len(co)):
        sum += int(co[j][ixc])
    if (sum == len(co) / 2):
        mco = str(0)
    else:
        mco = str(1-sum // int(np.ceil(len(co) / 2)))
    ixd = []
    for i in range(len(co)):
        if co[i][ixc] != mco:
            ixd.append(i)
    for i in sorted(ixd, reverse=True):
        co.pop(i)
    ixc += 1

print('Life support rating: ', int(ox[0], 2) * int(co[0], 2))
