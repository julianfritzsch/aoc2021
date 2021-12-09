import re


def decode(a, b):
    zer = set(['a', 'b', 'c', 'e', 'f', 'g'])
    # one = set(['c', 'f'])
    two = set(['a', 'c', 'd', 'e', 'g'])
    thr = set(['a', 'c', 'd', 'f', 'g'])
    # fou = set(['b', 'c', 'd', 'f'])
    fiv = set(['a', 'b', 'd', 'f', 'g'])
    six = set(['a', 'b', 'd', 'e', 'f', 'g'])
    # sev = set(['a', 'c', 'f'])
    # eig = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    nin = set(['a', 'b', 'c', 'd', 'f', 'g'])

    for entry in a + b:
        if len(entry) == 2:
            tempone = [i for i in entry]
        elif len(entry) == 3:
            tempsev = [i for i in entry]
        elif len(entry) == 4:
            tempfou = [i for i in entry]
        elif len(entry) == 7:
            tempeig = [i for i in entry]

    midlef = list(set(tempfou) - set(tempone))
    botlef = list(set(tempeig) - set(tempsev) - set(tempfou))
    test = {}
    test['a'] = list(set(tempsev) - set(tempone))[0]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                test['c'] = tempone[i]
                test['f'] = tempone[1-i]
                test['b'] = midlef[j]
                test['d'] = midlef[1-j]
                test['e'] = botlef[k]
                test['g'] = botlef[1-k]
                tempzer = set(test[i] for i in zer)
                temptwo = set(test[i] for i in two)
                tempthr = set(test[i] for i in thr)
                tempfiv = set(test[i] for i in fiv)
                tempsix = set(test[i] for i in six)
                tempnin = set(test[i] for i in nin)
                for entry in a + b:
                    if len(entry) == 5:
                        temp = set([i for i in entry])
                        if not(len(temptwo - temp) == 0 or len(tempthr - temp) == 0 or len(tempfiv - temp) == 0):
                            break
                    elif len(entry) == 6:
                        temp = set([i for i in entry])
                        if not(len(tempzer - temp) == 0 or len(tempsix - temp) == 0 or len(tempnin - temp) == 0):
                            break
                else:
                    ret = 0
                    for i, entry in enumerate(b):
                        if len(entry) == 2:
                            ret += 1 * 10**(3-i)
                        elif len(entry) == 3:
                            ret += 7 * 10**(3-i)
                        elif len(entry) == 4:
                            ret += 4 * 10**(3-i)
                        elif len(entry) == 5:
                            temp = set([i for i in entry])
                            if len(temptwo - temp) == 0:
                                ret += 2 * 10**(3-i)
                            elif len(tempthr - temp) == 0:
                                ret += 3 * 10**(3-i)
                            else:
                                ret += 5 * 10**(3-i)
                        elif len(entry) == 6:
                            temp = set([i for i in entry])
                            if len(tempzer - temp) == 0:
                                ret += 0 * 10**(3-i)
                            elif len(tempsix - temp) == 0:
                                ret += 6 * 10**(3-i)
                            else:
                                ret += 9 * 10**(3-i)
                        elif len(entry) == 7:
                            ret += 8 * 10**(3-i)
                    return ret


inp = []
out = []
with open('input8th.txt') as f:
    for line in f:
        temp = re.split(' \| ', line.strip())
        inp.append(temp[0].split())
        out.append(temp[1].split())

# Part 1
sol = 0
for line in out:
    for entry in line:
        if len(entry) == 2 or len(entry) == 3 or len(entry) == 7 or len(entry) == 4:
            sol += 1
print('Number of easy to guess output values: ', sol)

# Part 2
sol2 = 0
for a, b in zip(inp, out):
    sol2 += decode(a, b)
print('Sum of output values: ', sol2)
