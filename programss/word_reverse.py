str1 = input()
str2 = str1.split(" ") # it is used to form a word with spaces
str2 = str2[::-1]  # slice[::-1] is used to reverse string 
print(*str2)  # * is used to give string for from list
# print(" ".join(str2)) # used when we use return in functions