def cal_num_indic_str(file):
    list = []
    with open(file, "r") as strFile:
        s = strFile.read()
        i = 0
        while i < len(s):

            if unicode(s[i]).isdecimal():
                num = s[i:i+3]
                if num not in list:
                    list.append(num)
                i += 2
            i += 1
    return len(list)

print "the number of replacement-indication strings in c1.txt is {}".format(cal_num_indic_str("c1.txt"))
print "the number of replacement-indication strings in c1.txt is {}".format(cal_num_indic_str("c2.txt"))





