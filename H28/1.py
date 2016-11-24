str = raw_input()[::-1]
sum = 0

for i, c in enumerate(str):
    sum += (ord(c) - ord('0')) * 4**i

print sum
