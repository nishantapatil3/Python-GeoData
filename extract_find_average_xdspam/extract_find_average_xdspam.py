#search line that starts with "X-DSPAM-Confidence:", extract and print the value and average value

fh = open('mbox-short.txt')
a=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sline = line.find(":")
    n = line[sline+1:]
    n1 = n.strip('\n')
    a.append(float(n1))
print a
s = 0
for n in a:
    s = s + n
average = s / len(a)
print average
print "Done"

