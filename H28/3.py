roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

str = raw_input()[::-1]
sum = 0
max = 0
for i,c in enumerate(str):
    certain = roman[c]
    if certain >= max:
        sum += certain
        max = certain
    elif certain < max:
        sum -= certain

print sum

