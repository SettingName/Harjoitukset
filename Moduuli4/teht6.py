'''
Docstring for Moduuli4.teht6
import math
import random
N = int(input())
n = (N*math.pi)/4
x = 4*n/N
while N == n:
    #doNothing
    break
print(f"Approximation of pi: {x}")
'''
import math
import random
N = int(input())
n = 0
loopNum = 0
while loopNum < N:
    x = random.uniform( -1, 1) 
    y = random.uniform( -1, 1)
    if (x**2 + y**2) < 1:
        n += 1
    loopNum += 1
loppuTulos = 4 * n/N 
print(f"Approximation of pi: {loppuTulos}")