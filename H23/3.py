from compress import make_dic

with open("s1.txt", "r") as strFile:
    s = strFile.read()
    dic = make_dic(s)
    print len(dic)
    print dic
