def calculate(r, unit, arr, n):
    if arr is None or n==0:
        return -1
    
    totalFoodRequired = r * unit
    foodTillNow = 0

    for house in range(n):
        foodTillNow += arr[house]
        if foodTillNow >= totalFoodRequired:
            return house + 1
    return 0

# input handling
r = int(input("enter the number of cats: "))
unit = int(input("enter the value of units: "))
n = int(input("Number of elements in an array: "))
arr = list(map(int, input("List elements with space separated: ").split()))

# calculate and print the result
print(calculate(r, unit, arr, n))

