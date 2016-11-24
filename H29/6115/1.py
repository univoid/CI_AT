from num import numList


def printNum(inputList):
    with open("out1.txt", "w") as outFile:

        for row in range(0, 5):
            s = ""
            for num in inputList:
                for c in numList[num][row]:
                    s += c
                s += "  "
            s += "\n"
            # DEBUG<1>
            # print s
            outFile.writelines(s)
    return True

s = raw_input()
inputList = []
for c in s:
    inputList.append(int(c))

print "The number is {}".format(inputList)

if printNum(inputList):
    print "The answer has been printed at out1.txt"





