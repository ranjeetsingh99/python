# abcdaa = abcd$$
str =input("Enter a String :")
print("Original string :",str)
char =str[0]
str =str.replace(char,'$')
str =char + str[1:];

print("Replaced string:",str);