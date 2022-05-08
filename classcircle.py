class circle :
    def __init__(self,radius):
        self.radius =radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference (self):
        return 2*3.14*self.radius
r = int(input("enter radius"))
c1 = circle(r)
a=c1.area()
print("area of circle is",a)
c =c1.circumference()
print("circumference of circle",c)
