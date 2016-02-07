#count hours and print occurances

import collections

name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

a = []
s = []
s1 = []
hrs = []
i = 0
for line in handle:
	if not line.startswith("From") : continue
	s = line.split()
	if s[0] == 'From':
		#print s
		n1 = s[5]
		s1 = n1.split(':')
		a.append(s1[0])
		hrs = a[0]
	#mdict[n1] = 1

a = sorted(a, key=int)               # ascending order

d = {x:a.count(x) for x in a}

for k in sorted(d):
    print k, d[k]