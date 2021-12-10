inp = []
with open('input10th.txt') as f:
    for line in f:
        inp.append(line.strip())
openchars = ['(', '[', '<', '{']
expectedclose = {'(': ')', '[': ']', '{': '}', '<': '>'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
sol = 0
illegallines = []

# Part 1
for ix, line in enumerate(inp):
    opens = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            opens.append(char)
        else:
            opened = opens.pop()
            if char != expectedclose[opened]:
                # print(
                #     f'Expected {expectedclose[opened]}, but found {char} instead.')
                sol += score[char]
                illegallines.append(ix)
                break
print('Total syntax error score: ', sol)

# Part 2
for ix in illegallines[::-1]:
    inp.pop(ix)
completing = []
for ix, line in enumerate(inp):
    opens = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            opens.append(char)
        else:
            opens.pop()
    completing.append([])
    for incomp in opens[::-1]:
        completing[ix].append(expectedclose[incomp])

score2 = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in completing:
    sol = 0
    for entry in line:
        sol *= 5
        sol += score2[entry]
    scores.append(sol)
print('Middle score: ', sorted(scores)[len(scores) // 2])
