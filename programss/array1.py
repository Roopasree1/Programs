# array = list(map(int, input().split(",")))
# print(array)
def LargeSmallSum(arr):
   arr.sort()
   return arr[2]+arr[3]
arr = list(map(int, input().split(",")))
print(arr)