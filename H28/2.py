str = raw_input()[::-1]
sum = 0
for i,c in enumerate(str):
    sum += (ord(c)-ord('a')) * 8**i

print sum

