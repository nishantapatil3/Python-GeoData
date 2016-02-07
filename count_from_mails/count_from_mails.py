#count highest number of email ids starting with "From:" and print the count

mdict = {}

name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

a = []
s = []
for line in handle:
	if not line.startswith("From:") : continue
	s = line.split()
	n1 = s[1]
	a.append(n1)
	mdict[n1] = 1

word_counter = {}
for word in a:
	if word in word_counter:
		word_counter[word] = word_counter[word] + 1
	else:
		word_counter[word] = 1

popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

print popular_words[0], word_counter[popular_words[0]]

