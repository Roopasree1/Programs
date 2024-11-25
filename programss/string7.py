# n=4
# m=20  # sungle line input n,m=map(int,input().split()) 
def differenceofSum(n,m):
    sum1 = 0
    sum2 = 0
    for i in range(n,m+1):
        if i % n == 0:
            sum1 = sum1 + i
        else:
            sum2 = sum2 + i
    return abs(sum1 - sum2)
n = int(input())
m = int(input())
print(differenceofSum(n,m))