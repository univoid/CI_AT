from math import sqrt

def area_k(n):
    if n == 0:
        return 25 * sqrt(3)
    elif n == 1:
        return 4.0/3 * area_k(0)
    else:
        return 13.0/9 * area_k(n - 1) - 4.0 / 9 * area_k(n - 2)

n = int(raw_input("input n: "))
print "K{} = {}".format(n, area_k(n))
