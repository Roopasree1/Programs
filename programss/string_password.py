def checkValid(s):
    if(len(s)<4):
        return 0
    if(" " in s or "/" in s):
        return 0
    if(s[0].isdigit()):
        return 0
    d=0
    u=0
    for i in s:
        if(i.isdigit()):
            d+=1
        elif(i.isupper()):
            u+=1
    if(d>0 and u>0):
        return 1
    return 0
s = input()
print(checkValid(s))