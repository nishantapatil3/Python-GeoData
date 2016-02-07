# Use the file name mbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
fh = open('regex_sum_192158.txt')
data = fh.read()
l = []
for t in data.split():
    try:
        l.append(float(t))
    except ValueError:
        pass
print l
s = 0
for n in l:
    s = s + n
print s

