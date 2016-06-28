f = open("program.txt", "r")
sum = 0
for line in f:
    tmp = filter(lambda c: c==";", line)
    sum += len(tmp)

print sum
