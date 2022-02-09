str1 = input("Enter first string :")
str2 = input("Enter second string :")
char_of_str1 =str1[0]
char_of_str2 =str2[0]

str1 = char_of_str2 + str1[1:]
str2 = char_of_str1 + str2[1:]

print(str1+str2)