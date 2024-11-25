def remove_special(str1):
    new = ""
    for i in str1:
        if i.isalpha():
            new = new + i
        else:
            new = new + " " #continue
    return new
    
str1 = input()
print(remove_special(str1))