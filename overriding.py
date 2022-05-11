class A:
    def random1(self):
        print("Iam in class A")
class C:
    def random2(self):
        print("I am in class C")
class B(A,C):
    def random(self):
        print("I am in class B")
item1 = B()
item1.random()
    
