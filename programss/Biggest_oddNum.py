str = input()
b = -1 #empty string
for i in range(len(str)-1,-1,-1):
    if(int(str[i])%2==1):
        b=i
        break
k=""
if(b!=-1):
    for i in range(0,b+1):
        k+=str[i]
print(k)
