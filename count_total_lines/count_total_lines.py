#fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open("mbox-short.txt")
count = 0

a = []
s = []
for line in fh:
    if not line.startswith("From:") : continue
    s = line.split()
    n1 = s[1]
    a.append(n1)
    count = count + 1

for i in a:
	print i

print "There were", count, "lines in the file with From as the first word"

