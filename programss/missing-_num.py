def missingNum(n,numbers):
    s1 = (n*(n+1))//2
    s2 = sum(numbers)
    return s2-s1
n = int(input())
numbers = list(map(int,input().split()))
print(missingNum(n,numbers))


#  same but using for loop # 1,3,4 n=4 output = 
def missingNum(n,numbers):
    s1 = (n*(n+1))//2
    s2 = 0
    for i in range(0,len(numbers)):
        s2 = s2+numbers[i]
    return s2-s1
n = int(input())
numbers = list(map(int,input().split()))
print(missingNum(n,numbers))