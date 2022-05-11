"""num = int(input("enter any number"))
flag =1
for i in range(2,num):
    if(num%i ==0):
        
        flag = 0
        break
    
if(flag==0):
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")"""

for i in range(2,num-1):
    if(num%i ==0):
        print("not prime")
        break
else:
    print("prime)
