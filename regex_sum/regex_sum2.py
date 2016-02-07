# Use the file name mbox-short.txt as the file name
import re
fh = open('regex_sum_192158.txt')
data = fh.read()
l = []
l = re.findall('[0-9]+', data)
#print l
s = 0
for n in l:
    s = s + float(n)
print s

