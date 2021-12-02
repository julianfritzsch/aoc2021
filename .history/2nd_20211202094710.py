with open('input2nd.txt') as f:
    inp = f.readlines()

depth = 0

for line in inp:
    direction, distance = line
