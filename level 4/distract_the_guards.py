'''
Distract the Guards
===================

The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the guards are fond of bananas. And gambling. And thumb wrestling.

The guards, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. The guard with fewer bananas will bet all their bananas, and the other guard will match the bet. The winner will receive all of the bet bananas. You don't pair off guards with the same number of bananas (you will see why, shortly). You know enough guard psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of guards will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to guarding the prisoners, and you don't want THAT to happen!

For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to guarding.

How is all this useful to distract the guards? Notice that if the guards had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into an infinite thumb wrestling loop!

Write a function answer(banana_list) which, given a list of positive integers depicting the amount of bananas the each guard starts with, returns the fewest possible number of guards that will be left to watch the prisoners. Element i of the list will be the number of bananas that guard i (counting from 0) starts with.

The number of guards will be at least 1 and not more than 100, and the number of bananas each guard starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) banana_list = [1, 1]
Output:
    (int) 2

Inputs:
    (int list) banana_list = [1, 7, 3, 21, 13, 19]
Output:
    (int) 0
'''

from fractions import gcd
def isInfPair(x, y):
	if x == y:
		return False
	if (x+y)%2 == 1:
		return True
	g = gcd(x,y)
	x,y = min(x,y)/g, max(x,y)/g
	return isInfPair(y-x, 2*x)
	


def findMinPair(pairs, noPair, paired):
	minPairs = len(pairs)
	minIdx = -1
	for i in range(len(pairs)):
		if i in noPair or i in paired:
			continue
		currPairs = sum(pairs[i])
		if currPairs == 0:
			noPair.add(i)
			continue
		if currPairs < minPairs:
			minIdx = i
			minPairs = currPairs
	return minIdx, minPairs, noPair

def findFirstPair(pairs, i):
	for j in range(len(pairs[i])):
		if pairs[i][j]:
			return j
	return 0

def cleanPair(pairs, i):
	for j in range(len(pairs[i])):
		if pairs[i][j]:
			pairs[j][i] = False
	return pairs

def answer(banana_list):
	pairs = [[False for j in range(len(banana_list))] for i in range(len(banana_list))]
	noPair = set()
	paired = set()
	for i in range(len(banana_list)):
		for j in range(i+1, len(banana_list)):
			if(isInfPair(banana_list[i], banana_list[j])):
				pairs[i][j] = True
				pairs[j][i] = True
	minIdx, minPairs, noPair = findMinPair(pairs, noPair, paired)
	while len(noPair) + len(paired) < len(pairs):
		pairIdx = findFirstPair(pairs, minIdx)
		pairs[minIdx][pairIdx] = False
		pairs[pairIdx][minIdx] = False
		pairs = cleanPair(pairs, minIdx)
		pairs = cleanPair(pairs, pairIdx)
		paired.add(minIdx)
		paired.add(pairIdx)
		minIdx, minPairs, noPair = findMinPair(pairs, noPair, paired)
	return len(noPair)

l = [1,1]
l = [1,7,3,21,13,19]
print answer(l)




