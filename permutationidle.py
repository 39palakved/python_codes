num = int(input("enter any number"))

fact1 =1
fact2 = 1
r = int(input("enter value of r"))
d = int(num -r)
j=0
if(num !=0):
    for i in range(1,num+1):
        fact1 = fact1*i
    print("factorial of n",fact1)
    for j in range (1,d+1):
        fact2 = fact2*j
    print("factorial of n-r",fact2)

    ans = fact1/fact2
    print(ans)
else:
    print("factorial of 0 is 1")
    
