import numpy as np


def haswon(b):
    for row in b:
        if np.alltrue(row):
            return True
    for row in b.T:
        if np.alltrue(row):
            return True
    return False


boards = []
with open('input4th.txt') as f:
    for i, line in enumerate(f):
        if i == 0:
            drawnnumbers = line.strip().split(',')
        elif i == 1:
            continue
        elif (i-2) % 6 == 0:
            board = []
            board.append(line.strip().split())
        elif (i-2) % 6 < 5:
            board.append(line.strip().split())
        elif (i-2) % 6 == 5:
            board.append(line.strip().split())
            boards.append(board)

# Part 1
check = np.zeros((len(boards), 5, 5), dtype=bool)

for num in drawnnumbers:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, el in enumerate(row):
                if el == num:
                    check[i, j, k] = True
    for i in range(len(boards)):
        if haswon(check[i]):
            winner = i
            print('Winner: ', i)
            break
    else:
        continue
    break

unmarkedsum = 0
for i, row in enumerate(check[winner]):
    for j, el in enumerate(row):
        if not el:
            unmarkedsum += int(boards[winner][i][j])
print('Score: ', unmarkedsum * int(num))

# Part 2
check = np.zeros((len(boards), 5, 5), dtype=bool)
alreadywon = set()

for num in drawnnumbers:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, el in enumerate(row):
                if el == num:
                    check[i, j, k] = True
    for i in range(len(boards)):
        if haswon(check[i]):
            if len(alreadywon) == len(boards) - 1 and i not in alreadywon:
                winner = i
                print('Winner: ', i)
                break
            else:
                alreadywon.add(i)
    else:
        continue
    break

unmarkedsum = 0
for i, row in enumerate(check[winner]):
    for j, el in enumerate(row):
        if not el:
            unmarkedsum += int(boards[winner][i][j])
print('Score: ', unmarkedsum * int(num))
