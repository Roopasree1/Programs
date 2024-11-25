# 

str = input()
u = 0
l = 0
for i in str:
    if(i.isupper):
        u+=1
    elif(i.islower):
        l+=1
if(u>l):
    print(str.upper())
else:
    print(str.lower())