from compress import compress_str

with open("s1.txt", "r") as strFile:
    s = strFile.read()
    print "compressed string of s1.txt is \"{}\"".format(compress_str(s))

with open("s2.txt", "r") as strFile:
    s = strFile.read()
    print "compressed string of s2.txt is \"{}\"".format(compress_str(s))


