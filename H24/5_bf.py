import numpy as np
import matplotlib.pyplot as plt
import sys


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.ylim(0, 30)
    plt.xlim(0, 30)
    plt.plot(x, y)


def cale(a, b, dl):
    return sum((y - (a*x+b)) ** 2 for (x, y) in dl)


def lsa(dl):
    xl, yl = zip(*dl)
    n = len(dl)
    d = n * sum(x ** 2 for x in xl) - sum(xl) ** 2      # Denominator
    a = float((n*sum(x * y for (x, y) in dl) - sum(xl) * sum(yl))) / d
    b = float(sum(x ** 2 for x in xl) * sum(yl) - sum(x * y for (x, y) in dl) * sum(xl)) / d
    e = cale(a, b, dl)
    return a, b, e


def binse(l, r, dl, x0, y0):
    if abs(l-r) < 0.1:
        return l

    mid = (l + r) / 2
    a = (l + mid)/2
    b = y0 - a * x0
    e1 = cale(a, b, dl)
    a = (r+mid)/2
    b = y0 - a * x0
    e2 = cale(a, b, dl)
    if e1 < e2:
        return binse(l, mid, dl, x0, y0)
    else:
        return binse(mid, r, dl, x0, y0)


f = open("data2.txt", "r")
dList = []
for line in f:
    tmp = eval(line)
    dList.append(tmp)

e = sys.maxint
ea1 = 0
eb1 = 0
ea2 = 0
eb2 = 0
ex = 0
ey = 0
for k in range(2, len(dList)-1):
    a1, b1, e1 = lsa(dList[:k])
    for xm in range(dList[k-1][0], dList[k][0]):
        ym = int(a1 * xm + b1)
        a2 = binse(0.0, 30.0, dList[k:], xm, ym)
        b2 = ym - a2 * xm
        e2 = cale(a2, b2, dList[k:])
        print k,a2, e2
        if e > e1 + e2:
            ea1 = a1
            eb1 = b1
            ea2 = a2
            eb2 = b2
            ex = xm
            ey = ym
            e = e1 + e2


plt.scatter(*zip(*dList))
print "({}, {})".format(ex, ey)
graph("{a} * x + {b}".format(a=ea1, b=eb1), range(0, 30))
graph("{a} * x + {b}".format(a=ea2, b=eb2), range(0, 30))
plt.show()