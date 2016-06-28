f = open("program1.txt", "r")
sl = []
for line in f:
    if len(line) >= 20:
        sl.append(line)

sl.sort(key=lambda x: -len(x))
#print sl

total = 0
for i, a in enumerate(sl):
    for j, b in enumerate(sl[i+1:]):
        error = len(a)-len(b) + len(filter(lambda c: c==" ", a[len(b):]))

        if error >= 5:
            break

        for k in range(0, len(b)):
            if a[k] != b[k]:
                error += 1
            if error >=5:
                break

        if error < 5:
            total += 1
            print "similar pair {}:\n{}\n{}\n".format(total, a, b)

print "process completed."
print "Sum of pairs: {}".format(total)
