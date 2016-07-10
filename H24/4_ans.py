from math import ceil
from draw import initial_canvas, draw_point, draw_canvas

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
# draw scatter
canvas = [[" " for x in range(64)] for y in range(32)]
initial_canvas(canvas)
for (x,y) in dList:
    draw_point(x, y, canvas, mark='*')

#draw fit
a, b = lsa(dList)
print a, b
for x in range(0, 30, int(ceil(1/a))):
    print x, a * x + b
    draw_point(x, a*x+b, canvas, mark='o')

draw_canvas(canvas)




