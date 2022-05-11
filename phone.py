class phonebook:
    def __init__(self ,first_name,last_name,contact_no):
        self.first_name = first_name
        self.last_name = last_name
        self.contact_no = contact_no
    def putdata(self):
        f = open("contactlist.txt",'a')
        f.write(self.first_name)
        f.write(self.last_name)
        f.write(self.contact_no)
        f.close()
    def getdata(self):
        f = open("contactlist.txt",'r')
        first_name= f.read()
        last_name = f.read()
        contact_no = f.read()
        print( first_name , last_name, contact_no)
        print("\n")
        f.close()
    def table(self):
        print("| F_NAME|" , "| L_NAME |"," C_NAME")
        p1.getdata()
        p2.getdata()  
p1 = phonebook("palak","ved","9926092521")            
p2 = phonebook("alvira","khan","0000000000")             
p1.putdata()
p2.putdata()
p1.table()
  
