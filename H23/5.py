from decompress import decompress_str

with open("c1.txt", "r") as strFile:
    s = strFile.read()
    print "the original string of c1.txt is \"{}\"".format(decompress_str(s))


with open("c2.txt", "r") as strFile:
    s = strFile.read()
    # print "the original string of c2.txt is \"{}\"".format(decompress_str(s))
    print decompress_str(s)