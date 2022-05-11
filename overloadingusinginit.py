class school():
    def __init__(self):
        self.name = input("emter name of school")
        self.address = input("enter address of school")
    def show(self):
        print("{} is situated at {}". format(self.name , self.address))
s1 = school()
s1.show()
