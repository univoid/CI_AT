class Sentence(object):
    def __init__(self, action, a, b):
        self.action = action
        self.a = a
        self.b = b

f = open("prog1.txt", "r")
proList = []

for line in f:
    tmp = line.split(" ")
    stn = Sentence(tmp[0], tmp[1], tmp[2])
    proList.append(stn)

for stn in proList:
    print stn.a



