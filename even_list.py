"""list1 =[2,13,42,4,524,331,452,321,22]
list_even = []
print(list1)
print(list_even)
for i in (list1):
    if i%2==0:
         list_even.append(i)
print(list_even)"""


## using function  

"""def even(n):
    return n%2==0
list1 =[2,13,42,4,524,331,452,321,22]
list_even=[]
print(list1)
print(list_even)
for i in (list1):
    y = even(i)
    if y ==true:
        list_even.append(i)
print(list_even)"""

## FILTER METHOD
"""from functools import reduce

list1 =[2,13,42,4,524,331,452,321,22,55]
list_even = list(filter(lambda x:x%2==0,list1))
# for filtering even and odd values from 
list_odd = list(filter(lambda x:x%2!=0,list1))
# for multiplying 
list_mul = list(map(lambda x:2*x, list1))
# for sum (we have to import reduce)
list_sum = reduce(lambda x,y:x+y,list1)

print(list1)
print(list_even)
print(list_odd)
print(list_mul)
print(list_sum)"""

## normal div function for division but output should not be less than 1

"""def div(x,y):
    if x<y:
        x,y = y,x
    return x/y
a = int(input("enter val of a"))
b = int(input("enter val of b"))
c =div(a,b)
print("a =", a)
print("b =", b)
print("c = ",c)"""

## using decorators


def smart_div(func):
    def inner(m,n):
        if m<n:
            m,n = n,m
            return func(m,n)
        return inner
a= int(input("Enter value of a:"))
b= int(input("Enter value of b:"))
c= div(a,b)
div= smart_div(div)
d= div(a,b)
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
        
        




















