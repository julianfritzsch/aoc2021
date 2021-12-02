with open('input2nd.txt') as f:
    inp = f.readlines()

depth = 0
horizontal = 0
for line in inp:
    direction, distance = line
    if direction == "up":
        depth -= distance
    elif direction == "down":
        depth += distance
    elif direction == "forward":
        horizontal += distance
    elif direction == "backward":
        horizontal -= distance

print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Combined: ", depth * horizontal)
