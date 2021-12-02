with open('input2nd.txt') as f:
    inp = f.readlines()

depth = 0
horizontal = 0
for line in inp:
    # print(line)
    direction, distance = line.split(" ")
    # if direction == "up":
    #     depth -= int(distance)
    # elif direction == "down":
    #     depth += int(distance)
    # elif direction == "forward":
    #     horizontal += int(distance)
    # elif direction == "backward":
    #     horizontal -= int(distance)

print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Combined: ", depth * horizontal)
