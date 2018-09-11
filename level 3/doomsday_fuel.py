from fractions import Fraction
from fractions import gcd

def reorder(m, finals):
	newm = []
	for i in finals:
		newrow = [0 for i in range(len(m))]
		newrow[len(newm)] = 1
		newm.append(newrow)
	for i in range(len(m)):
		if i in finals:
			continue
		infinals = []
		notfinals = []
		for j in range(len(m[i])):
			if j in finals:
				infinals.append(m[i][j])
			else:
				notfinals.append(m[i][j])
		newrow = infinals + notfinals
		sumrow = sum(newrow)
		newrow = [num*1.0/sumrow for num in newrow]
		newm.append(newrow)
	return newm

# getInverse w/o np: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy/39881366	
def transposeMatrix(m):
    return map(list,zip(*m))

# getInverse w/o np: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy/39881366	
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# getInverse w/o np: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy/39881366	
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

# getInverse w/o np: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy/39881366	
def getMatrixInverse(m):
	if len(m) == 1:
		return [[1.0/m[0][0]]]
	determinant = getMatrixDeternminant(m)
	#special case for 2x2 matrix:
	if len(m) == 2:
	    return [[m[1][1]/determinant, -1*m[0][1]/determinant],
	            [-1*m[1][0]/determinant, m[0][0]/determinant]]

	#find matrix of cofactors
	cofactors = []
	for r in range(len(m)):
	    cofactorRow = []
	    for c in range(len(m)):
	        minor = getMatrixMinor(m,r,c)
	        cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
	    cofactors.append(cofactorRow)
	cofactors = transposeMatrix(cofactors)
	for r in range(len(cofactors)):
	    for c in range(len(cofactors)):
	        cofactors[r][c] = cofactors[r][c]/determinant
	return cofactors


def subtractFromIdentity(Q):
	for i in range(len(Q)):
		for j in range(len(Q[0])):
			if i == j:
				Q[i][j] = 1 - Q[i][j]
			else:
				Q[i][j] = -Q[i][j]
	return Q

def multiplyMatrices(a, b):
    rowNum = len(a)
    colNum = len(b[0])
    res = [[0 for i in range(colNum)] for j in range(rowNum)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k]*b[k][j]
    return res

def toInt(row):
	toMut = 1
	for prob in row:
		if prob == 0:
			continue
		toMut *= Fraction(prob).limit_denominator().denominator
	row = [int(round(num*toMut)) for num in row]
	toDiv = []
	divisor = max(row)
	for num in row:
		if num!=0:
			toDiv.append(num)
	for i in range(len(toDiv)-1):
		newgcd = gcd(toDiv[i], toDiv[i+1])
		divisor = min(newgcd, divisor)
	row = [rownum/divisor for rownum in row]
	return row

def answer(m):
	if len(m) == 1:
		return [1,1]
	finals = []
	for i in range(len(m)):
		if(sum(m[i])) == 0:
			finals.append(i)
	numFinal = len(finals)
	m = reorder(m, finals)
	R = [m[i][:numFinal] for i in range(numFinal,len(m))]
	Q = [m[i][numFinal:] for i in range(numFinal,len(m))]
	F = getMatrixInverse(subtractFromIdentity(Q))
	FR = multiplyMatrices(F, R)
	ans = toInt(FR[0])
	ans.append(sum(ans))
	return ans

m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#m = [[0,3,3,4], [0,0,0,0], [0,0,0,0],[8,1,1,0]]
print(answer(m))