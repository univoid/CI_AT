from compress import compress_str
from decompress import decompress_str
import filecmp


def slice_compress(fin, fout):
    max_size = 1000
    with open(fin, "r") as inFile:
        with open(fout, "w") as outFile:
            while True:
                buf = inFile.read(max_size)
                if not buf:
                    break
                outFile.write(compress_str(buf))
                outFile.write("&")


def slice_decompress(fin, fout):
    with open(fin, "r") as inFile:
        with open(fout, "w") as outFile:
            while True:
                buf = ""
                while True:
                    c = inFile.read(1)
                    if not c or c == "&":
                        break
                    buf += c

                if not buf:
                    break

                outFile.write(decompress_str(buf))

slice_compress("s3.txt", "compress6.txt")
print "File compression completed"
slice_decompress("compress6.txt", "decompress6.txt")
print "File decompression completed"

if filecmp.cmp("s3.txt", "decompress6.txt"):
    print "The processes is correct"
else:
    print "Sad......"








