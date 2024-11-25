def mail(str1):
    str2 = ""
    str3 = "@gmail.com"
    if str1.isalpha():  # if entire given input contains alpha
        str2=str1+str3
    else:
        str2=str1 #original 
    return str2
str1 = input()
print(mail(str1))