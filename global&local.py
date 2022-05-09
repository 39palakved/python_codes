"""def user_input():
	a=input("enter value 1")
	b=input("enter value 2")
	print(a,b)
def add(a,b):
    return a+b
user_input
add(a,b)
print(a,'+',b,'=',add(a,b))"""
def user_input():
    a=int(input("enter value 1"))
    b=int(input("enter value 2"))
    return(a,b)
def add(a,b):
    return a+b
a,b =user_input()
add(a,b)
print(a,'+',b,'=',add(a,b))

a,b = int(input("enter value of a and b"))
print(a)
print(b)
