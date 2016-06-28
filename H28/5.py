roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
decimal = {"1000":"M", "500":"D", "100":"C", "50":"L", "10":"X", "5":"V", "1":"I"}
d = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
r = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
str = ''
num = int(raw_input())
for i in range(0,len(d)):
    j = num / d[i]
    str += r[i] * j
    num = num % d[i]

print str


