from printf import printf

def draw_point(x, y, canvas, mark='*'):
    x = int(x)
    # if ceil depended on 2nd of Decimal point
    y = int(y + 0.05)
    canvas[30-y][2*x+2] = mark


def initial_canvas(canvas):
    fc = open("canvas.txt", "r")
    y = 0
    x = 0
    for line in fc:
        line = line.replace("\n", "")
        for c in line:
            canvas[y][x] = c
            x += 1
        y += 1
        x = 0


def draw_canvas(canvas):
    with open("output.txt", "w") as outFile:
        for row in canvas:
            for c in row:
                printf(c, outFile)
            print >> outFile
