# input roopa__sree # output __roopasree
def spacesBack(str1):
    str2=""
    str3=""
    for i in str1:
        if(i== "-"):
            str2+=i  
        else:
            str3+=i
        return str2+str3
        
str1 = int(input())
print(spacesBack(str1))