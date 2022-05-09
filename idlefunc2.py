def fact(n):
    
    fact =1

    for i in range(1,n+1):
        fact = fact*i
        return(fact)
x = int(input("enter  number"))
y =  int (input("enter number"))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
p*int("p=",p)
    
