
from draw import initial_canvas, draw_canvas, draw_point

# initialise canvas (32*2 col, 32 row)
canvas = [[" " for x in range(64)] for y in range(32)]
initial_canvas(canvas)

# read data
f = open("data1.txt", "r")
dList = []
for line in f:
    tmp = eval(line)
    dList.append(tmp)

for (x, y) in dList:
    draw_point(x, y, canvas, mark='*')

draw_canvas(canvas)




