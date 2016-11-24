from num import recognizeNumHash, hashList
def sliceStr(s):
    seq = []
    # [x, y]: from x to y
    seq.append([0, 0])
    i = 0
    while i+2 < len(s):
        c1 = s[i]
        c2 = s[i+1]
        c3 = s[i+2]
        if c1 == "*" and c2 == " " and c3 == " ":
            seq[-1][1] = i+1
            if i+3 < len(s)-2:
                seq.append([i+3, i+3])
        i += 1

    return seq

def getMatrix(x,y,inList):
    m = []
    for i in range(0,5):
        line = []
        for j in range(x, y):
            c = inList[i][j]
            line.append(c)
        m.append(line)
    return m




with open("out1.txt", "r") as inFile:
    inList = []
    for line in inFile:
        cList = []
        for c in line:
            cList.append(c)
        inList.append(cList)

    # DEBUG<2>
    # print inList
    # for line in strList:
    #    print line

    # none of "  " in the line[4] expect the ones between two pictographic
    # the point of the first cha of each number
    slicePointSeq = sliceStr(inList[4])
    print slicePointSeq

    # recognization
    ans = []
    for rang in slicePointSeq:
        x = rang[0]
        y = rang[1]

        m = getMatrix(x, y, inList)
        # print m
        hashNum = recognizeNumHash(m)
        # print hashNum
        num = hashList.index(hashNum)
        ans.append(num)
    str = ""
    for item in ans:
        str += unicode(item)
    print "The Number is {}".format(str)


