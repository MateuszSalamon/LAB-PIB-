import re

infile = "text1.txt"
outfile = "test.txt"

delete_list = [" sie", " i", " dlaczego", " oraz"," nigdy"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()