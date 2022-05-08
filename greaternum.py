a= input("enter first number")

b = input("enter second number")
c = input("enter third number")

a = int(a)
b = int(b)
c = int(c)
if(a == b == c):
     print("all values are same")
elif(a == b and  c<a  and c<b):
     print(a, "and", b ,"are equal and greater than",c)
elif(b ==c and a<b and a<c):
     print(b, "and", c,"are equal and greater than",a)
elif(a>b and a>c):
     print(a, "is greater than",b ,"and", c )
elif(b>a and b>c):
    print(b, "is greater than",a, "and", c )
else:
     print(c, "is greater than",a ,"and", b )
