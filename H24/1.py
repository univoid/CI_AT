f = open("data1.txt", "r")
dList = []
for line in f:
    tmp = eval(line)
    dList.append(tmp)

print max(dList, key=lambda x: x[1])
