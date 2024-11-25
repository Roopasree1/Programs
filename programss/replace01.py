def numbers_Replac(num1):
    num2=""
    for i in str(num1):
        if(i=='0'):
            num2+='1'
        else:
            num2+=i
    return int(num2)
num1 = int(input())
print(numbers_Replac(num1))