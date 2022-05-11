class student:
    """def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c"""
    def avg(self, a = None , b =None , c = None):
        average = 0
        if(a !=None and b!=None and c !=None):
            average = (a+b+c)/3
        elif(a !=None and b!=None and c == None):
            average = (a+b)/2
        elif(a!=None and b==None and c ==  None):
            average =a
        else:
            average = "No values provided"
        return average
s1 = student()
a = s1.avg()
print(a)
b =s1.avg(2,3)
print(b)
