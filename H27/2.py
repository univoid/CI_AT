f = open("program.txt", "r")
num = 0
for line in f:
    num += 1
    if "main" in line:
        print "line {}: {}".format(num, line)

