n=int(input())

import math
def hcf(a,b):
    return math.gcd(a,b)
def lcm(a,b):
    return abs(a*b)
a = int(input())
b = int(input())
print(hcf(a,b))
print(lcm(a,b))
    