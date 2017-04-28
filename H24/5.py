import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.ylim(0, 30)
    plt.xlim(0, 30)
    plt.plot(x, y)
    plt.show()

def lsa(dl):
    xl, yl = zip(*dl)
    n = len(dl)
    d = n * sum(x ** 2 for x in xl) - sum(xl) ** 2      # Denominator
    a = float((n*sum(x * y for (x, y) in dl) - sum(xl) * sum(yl))) / d
    b = float(sum(x ** 2 for x in xl) * sum(yl) - sum(x * y for (x, y) in dl) * sum(xl)) / d

    return a, b


f = open("data1.txt", "r")
dList = []
for line in f:
    tmp = eval(line)
    dList.append(tmp)

# test
# dList = map(lambda x: (x[0], min(30, x[1]+3)), dList)

a, b = lsa(dList)
print a, b

plt.scatter(*zip(*dList))
graph("{a} * x + {b}".format(a=a, b=b), range(0, 30))
