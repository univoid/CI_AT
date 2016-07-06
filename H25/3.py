class Sentence(object):
    def __init__(self, action, a, b):
        self.action = action
        self.a = a
        self.b = b

f = open("prog2.txt", "r")
proList = []

for line in f:
    tmp = line.strip().split(" ")
    stn = Sentence(tmp[0], tmp[1], tmp[2])
    proList.append(stn)

point = 0
memo = {}
while point != len(proList):
    c = proList[point]
    action = c.action
    a = c.a
    b = c.b
    if action == "SET":
        memo[a] = memo[b] if (b in memo) else int(b)

    elif action == "ADD":
        if a in memo:
            memo[b] += memo[a]
        else:
            memo[b] += int(a)

    elif action == "PRN":
        print memo[a], memo[b]
        break

    point += 1



