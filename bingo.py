import random


def getTicket():
    tkt = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    l = []
    while 1 < 2:
            a = random.randint(1, 89)

            if a not in l:
                if d[int(a / 10)] < 3:
                    l.append(a)
                    d[int(a / 10)] += 1
                    if len(l) == 15:
                        break

    for x in l:
            x1 = int(x / 10)
            while 1 < 2:
                a = random.randint(0, 2)
                if tkt[a][x1] == 0:
                    tkt[a][x1] = x
                    break

    return tkt

t = getTicket();

print([5,5,5,5,8]//4)