a = int (input("input a integer :"))
n1= int("%s%s"%(a,a))
n2= int("%s%s" %(a,n1))

print(a," ",n1," ",n2)

print("Sum= ",(a+n1+n2))