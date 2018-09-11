def answer(l):
	if len(l) < 3:
		return 0
	res = 0
	divides = [[] for i in range(len(l))]
	for i in range(len(l)-1):
		for j in range(i+1, len(l)):
			if l[j] % l[i] == 0:
				divides[i].append(j)
	for i in range(len(divides)):
		for j in divides[i]:
			res += len(divides[j])
	return res

l = [1,2,3,4,5,6]
print answer(l)