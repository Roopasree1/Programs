def replace_char(s):
    str1=" "
    for i in str1:
        if i=="a":
            str1+="e"
        elif i=="e":
            str1+="a"
        else:
            str1+=i
    return str1
s=input()
print(replace_char(s))