class test:
    def __init__(self,sub1,sub2):
        self.sub1 = sub1
        self.sub2 = sub2
    def show(self):
        print(self.sub1)
        print(self.sub2)
    def __add__(self,other):
        
        sub1 = self.sub1 - other.sub1
        sub2 = self.sub2 - other.sub2
        return test(sub1,sub2)


t1 = test(21,17)
print("marks of sub 1")
t1.show()
t2 = test(18,17)
print("marks of sub 2")
t2.show()

t3 = t1+t2
print("makrs after addition")
t3.show()       
