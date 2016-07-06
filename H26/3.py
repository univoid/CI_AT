from math import sqrt
def areaK(n):
    if n == 0:
        return 25 * sqrt(3)
    elif n == 1:
        return 4.0/3 * areaK(0)
    else:
        return 13.0/9 * areaK(n-1) - 4.0/9 * areaK(n-2)

print "K{} = {}".format(2, areaK(2))

