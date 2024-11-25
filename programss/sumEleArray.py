def sumArray(num):
    arr = 0
    for i in num:
        if i<len(num):
            arr+=i
        else:
            arr+=i
    return arr
num=list(map(int,input().split()))
print(sumArray(num))
    