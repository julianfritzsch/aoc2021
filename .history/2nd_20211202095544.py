with open('input2nd.txt') as f:
    inp = f.readlines()

# Part 1
depth = 0
horizontal = 0
for line in inp:
    direction, distance = line.split(" ")
    if direction == "up":
        depth -= int(distance)
    elif direction == "down":
        depth += int(distance)
    elif direction == "forward":
        horizontal += int(distance)

print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Combined: ", depth * horizontal)


# Part 2
depth = 0
horizontal = 0
aim = 0
for line in inp:
    direction, distance = line.split(" ")
    if direction == "up":
        aim -= int(distance)
    elif direction == "down":
        aim += int(distance)
    elif direction == "forward":
        horizontal += int(distance)
        depth += int(distance) * aim

print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Combined: ", depth * horizontal)
