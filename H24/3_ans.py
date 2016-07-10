from math import ceil
from draw import initial_canvas, draw_canvas, draw_point

# initialise canvas (32*2 col, 32 row)
canvas = [[" " for x in range(64)] for y in range(32)]
initial_canvas(canvas)

a = 0.5
b = 10
for x in range(0, 30, int(ceil(1/a))):
    draw_point(x, a*x+b, canvas, mark='o')

draw_canvas(canvas)




