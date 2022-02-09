color1 = input("Enter a set of colors (separated by space ) :")
color2 = input("Enter a set of colors (separated by space ) :")
c1 = set(color1.split())
c2 = set(color2.split())

print("The difference between" ,c1,"and",c2 ,"is",c1.difference(c2),c2.difference(c1))