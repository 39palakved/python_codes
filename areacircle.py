class A:
    def area(self,r=None , l=None ):
        
        if(r!=None and l==None ):
            a =3.14*r*r
            return a
        elif(l!=None and  r != None):
            a = l*r
            return a
        else:
            a = "no value provided"
            return a
           
ar = A()
x =ar.area(3)
print("area of circle =",x)
y =ar.area(3,4)
print("area of rectangle =",y)
z =ar.area()
print(z)
