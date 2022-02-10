a =int (input("Enter first no.:"))
b =int(input("Enter second no.:"))

mini = min(a,b)+1

for i in range(1,mini):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD of",a,b,"is",gcd)