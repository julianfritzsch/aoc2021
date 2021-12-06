with open('input6th.txt') as f:
    fish = list(map(int, f.readline().strip().split(',')))

timer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in fish:
    timer[i] += 1
timer2 = timer.copy()

for j in range(256):
    for i in range(1, 9):
        timer2[i-1] = timer[i]
    timer2[8] = timer[0]
    timer2[6] += timer[0]
    timer, timer2 = timer2, timer

print(sum(timer))
