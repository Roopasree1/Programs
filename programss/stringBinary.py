s=input()
dec=64
result=""
for i in s:
    if(i=="1"):
        dec+=1
    else:
        result+=chr(dec)  # 11101101 = CBA
        dec=64
if(dec>64):
    result+=chr(dec)
    print(result)



#str1=(input())
#if(str1=="1C0C1C1A0B1"):
#   print(1)
#else: 
#   print(0)
