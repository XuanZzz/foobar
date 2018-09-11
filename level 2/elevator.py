def answer(l):
	li = [(map(int,l[i].split('.')), l[i]) for i in range(len(l))]
	li.sort()
	return [t[1] for t in li]

#l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
print(answer(l))