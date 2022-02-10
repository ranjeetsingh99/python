import math
n = int(input("Enter a number :"))

for i in range(1, n):
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            break
    else :   
        print(i,"  ");
        
    

