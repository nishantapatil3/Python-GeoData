#tokenize string and print in accending order, repeating elements print only once

fh = open('romeo.txt')
l2 = []
for line in fh:
	#print line
	l1 = line.split()
	#print l1
	l2 = l2 + l1
#print l2
l2.sort()
#print l2
seen = set()
uniq = []
for x in l2:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
print uniq

