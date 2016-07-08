import matplotlib.pyplot as plt


f = open("data1.txt", "r")
dList = []
for line in f:
    tmp = eval(line)
    dList.append(tmp)

plt.scatter(*zip(*dList))
plt.show()


