row = int(input())
col = int(input())
mat = []
for i in range(row):
    nums = list(map(int,input().split()))
    mat.append(nums)
magical = 0
for rows in mat:
    sum=0
    for i in rows:
        if(i%2 == 1):
            sum+=i
    if(sum%2==0):
        magical+= 1
print(magical)

