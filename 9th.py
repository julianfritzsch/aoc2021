inp = []
with open('input9th.txt') as f:
    for line in f:
        inp.append(line.strip())
N1 = len(inp)
N2 = len(inp[0])
sol = 0
minima = []
for i in range(N1):
    for j in range(N2):
        top = 10
        bot = 10
        rig = 10
        lef = 10
        if i > 0:
            top = int(inp[i-1][j])
        if i < N1-1:
            bot = int(inp[i+1][j])
        if j > 0:
            lef = int(inp[i][j-1])
        if j < N2 - 1:
            rig = int(inp[i][j+1])
        cur = int(inp[i][j])
        if cur < top and cur < bot and cur < rig and cur < lef:
            minima.append((i, j))
            sol += 1 + cur
print('Number of minima: ', sol)

basins = [[] for i in minima]
for i, minimum in enumerate(minima):
    # print(i)
    basins[i].append(minimum)
    change = True
    while change:
        # print(basins[i])
        change = False
        newnodes = []
        for node in basins[i]:
            _i = node[0]
            _j = node[1]
            if _i > 0:
                if int(inp[_i - 1][_j]) > int(inp[_i][_j]) and (_i-1, _j) not in basins[i] and int(inp[_i - 1][_j]) != 9:
                    newnodes.append((_i-1, _j))
                    change = True
            if _i < N1-1:
                if int(inp[_i + 1][_j]) > int(inp[_i][_j]) and (_i+1, _j) not in basins[i] and int(inp[_i + 1][_j]) != 9:
                    newnodes.append((_i+1, _j))
                    change = True
            if _j > 0:
                if int(inp[_i][_j-1]) > int(inp[_i][_j]) and (_i, _j-1) not in basins[i] and int(inp[_i][_j-1]) != 9:
                    newnodes.append((_i, _j-1))
                    change = True
            if _j < N2-1:
                if int(inp[_i][_j + 1]) > int(inp[_i][_j]) and (_i, _j + 1) not in basins[i] and int(inp[_i][_j + 1]) != 9:
                    newnodes.append((_i, _j+1))
                    change = True
        for node in set(newnodes):
            basins[i].append(node)

basindepths = [len(basin) for basin in basins]
basindepths = sorted(basindepths, reverse=True)
print('Three largest basins: ',
      basindepths[0] * basindepths[1] * basindepths[2])
