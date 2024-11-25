def sum_divisible_by_11(n1, n2):
    result = 0
    for i in range(n1, n2+1):
        if i % 11 == 0:
            result += i
    return result

# Input two numbers
n1 = int(input())
n2 = int(input())



