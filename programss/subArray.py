nums = list(map(int,input().split()))
k = int(input())
nums.sort()
low = 0
high = len(nums)-1
count = 0
while(low<=high):
    if(nums[low]+nums[high]<=k):
        count+=high-low+1
        low+=1
    else:
        high-=1
print(count)
