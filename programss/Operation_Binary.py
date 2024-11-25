def OperationBinaryString(str1):
    a=int(str1[0])
    i=1
    while(i<len(str1)):
        if str1[i]=='A':
            a&=int(str1[i+1])
        elif str1[i]=='B':
            a|=int(str1[i+1])
        else:
            a^=int(str1[i+1])
        i+=2
    return a
str1=input()
print(OperationBinaryString(str1))