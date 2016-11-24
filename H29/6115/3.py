from num import numList

rowMax = 5
def printNum(inputList):
    with open("out3.txt", "w") as outFile:

        for row in range(0, rowMax):
            s = ""
            j = 0
            for num in inputList:
                for c in num[row]:
                    s += c
                if j < len(whitC):
                    for k in range(0, whitC[j]):
                        s += " "
                j += 1
            s += "\n"
            # DEBUG<1>
            # print s
            outFile.writelines(s)
    return True

def getMatrix(i, vert):
    num = numList[i]
    m = []
    for j in range(0, vert):
        if i == 1:
            m.append([" "])
        else:
            m.append([" ", " ", " ", " "])
    for line in num:
        m.append(line)
    for j in range(0, rowMax - vert - 5):
        if i == 1:
            m.append([" "])
        else:
            m.append([" ", " ", " ", " "])
    return m

s = raw_input()
inputList = s.split(",")
num = []
for c in inputList[0]:
    num.append(int(c))

vert = []
whitC = []
for i in range(1, len(inputList)):
    if i % 2:
        vert.append(int(inputList[i]))
    else:
        whitC.append(int(inputList[i]))


print "The number is {}".format(num)
print vert
print whitC
rowMax = 5 + max(vert)
ans = []
j = 0
for i in num:
    m = getMatrix(i, vert[j])
    j += 1
    ans.append(m)

if printNum(ans):
    print "The answer has been printed at out3.txt"





