def swap(str1):
    new = ""
    for i in str1:
        if i.isupper():
            new = new + i.lower()
        else:
            new = new + i.upper()
    return new
            
str1 = input()
print(swap(str1))

# print(dir(str)) to see methods