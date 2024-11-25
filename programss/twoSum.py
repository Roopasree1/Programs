def twoDef(nums,target):
    low = 0
    high = len(nums)-1
    while(low<high):
        sum=nums[low]+nums[high]
        if(sum==target):
            return True 
        elif(sum>target):
            high=-1
        elif(sum<target):
            low+=1
    return False
nums = list(map(int, input().split()))
target = int(input())
print(twoDef(nums,target))