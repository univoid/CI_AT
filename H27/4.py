f = open("program.txt", "r")
d = {}
total = 0
for line in f:
    if d.has_key(line):
        if d[line] == 1:
            print line
            total += 1
        d[line] += 1
    else:
        d[line] = 1

print total
