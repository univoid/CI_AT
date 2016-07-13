from math import sqrt, ceil, floor
def computesA0(d):
    return (int(10/d)+1) ** 2

def computesA1(d):
    sum = 0
    for i in range(0, int(10/d)+1):
        y = i * d
        xl = 5 - sqrt(10 * y - y ** 2)
        xr = 5 + sqrt(10 * y - y ** 2)
        sum += floor(xr/d) - ceil(xl/d) + 1
        # print "{}: ({}, {}) sum = {}".format(y, int(xl/d), int(xr/d), sum)

    return float(sum)

d = float(raw_input())
print computesA1(d)/(computesA0(d) * 4)




