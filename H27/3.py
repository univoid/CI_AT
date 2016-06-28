f = open("program.txt", "r")
pre = ""
flag = 0

for line in f:

    if line == pre:
        flag = 1
    elif flag == 1:
        print pre
        flag = 0

    pre = line

# deal with last line
if flag == 1:
    print pre
    flag = 0
