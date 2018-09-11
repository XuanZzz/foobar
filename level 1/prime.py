from math import sqrt 

def answer(n):
    p = "2357111317192329"
    for i in range(31, 30000):
        if len(p) > n + 5:
            return p[n:n+5]
        isPrime = True
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            p += str(i)
    return p[n:n+5]

print(answer(1000))