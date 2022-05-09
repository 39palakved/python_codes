#instance method

class student():
    institution = "IIPS"
    def __init__(self,a,b):
         self.a=a
         self.b=b
    def show(self):
        print("___________________")
        print("marks in python",self.a)
        print("________________________")
        print("marks in python lab",self.b)
    @classmethod
        def info(self):
           print("class belongs to",self.institution)


        def about():
           print("this class hold the data of marks")
s1= student(12,10)
s2= student(13,11)
s3= student(14,9)
s1.show()
s2.show()
s3.show()
student.info()
student.show()
print(student.institution)


# class method:this metjhod is used to get the info about particular content of class.

