str1 = input()             
str2= ""
for i in str1:
    if i == " ":
        str2+="@"
    else:
        str2+=i
print(str2)

# to convert list to string we use join  (fubctions)
def manipulate(string3):
   new = ''
   for i in string3:
      if i == " ":
         new = new+ "@"
      else:
         new = new + i
   return new

string3 = input()
print(manipulate(string3))