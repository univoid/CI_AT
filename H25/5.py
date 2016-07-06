class Sentence(object):
    def __init__(self, action, a, b):
        self.action = action
        self.a = a
        self.b = b

f = open("prog1.txt", "r")
proList = []

for line in f:
    tmp = line.strip().split(" ")
    stn = Sentence(tmp[0], tmp[1], tmp[2])
    proList.append(stn)

point = 0
recPos = 0
memo = {}
while point != len(proList):
    c = proList[point]
    action = c.action
    a = c.a
    b = c.b
    if action == "SET":
        memo[a] = memo[b] if (b in memo) else int(b)
        point += 1

    elif action == "ADD":
        if a in memo:
            memo[b] += memo[a]
        else:
            memo[b] += int(a)

        point += 1

    elif action == "PRN":
        print memo[a], memo[b]
        break

    elif action == "CMP":
        point += 1
        cmpA = memo[a] if (a in memo) else int(a)
        cmpB = memo[b] if (b in memo) else int(b)
        if cmpA == cmpB:
            point += 1

    elif action == "JMP":
        point += int(a)

    elif action == "SUB":
        recPos = point
        point += int(a)

    elif action == "BAK":
        point = recPos

    elif action == "CAL":
        pass

    elif action == "RET":
        pass






