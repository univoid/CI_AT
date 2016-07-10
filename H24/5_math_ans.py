import sys
from math import ceil
from draw import initial_canvas, draw_point, draw_canvas

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


def get_a(dl, x0, y0):
    return float(sum((y-y0)*(x-x0) for (x, y) in dl))/((sum((x-x0)**2 for (x, y) in dl)))


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
        # some math trick
        a2 = get_a(dList[k:], xm, ym)
        b2 = ym - a2 * xm
        e2 = cale(a2, b2, dList[k:])
        # print k, a2, e2
        if e > e1 + e2:
            ea1 = a1
            eb1 = b1
            ea2 = a2
            eb2 = b2
            ex = xm
            ey = ym
            e = e1 + e2

# draw scatter
canvas = [[" " for x in range(64)] for y in range(32)]
initial_canvas(canvas)
for (x,y) in dList:
    draw_point(x, y, canvas, mark='*')

print "turn point: ({}, {})".format(ex, ey)
# draw fit
for x in range(0, ex, int(ceil(1/ea1))):
    if ea1 * x + eb1 < 0:
        continue
    draw_point(x, ea1*x+eb1, canvas, mark='o')

for x in range(ex, 30, int(ceil(1/ea2))):
    if ea2 * x + eb2 > 30:
        break
    draw_point(x, ea2*x+eb2, canvas, mark='o')

draw_canvas(canvas)
