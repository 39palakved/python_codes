terms = int(input("enter how many terms"))
n1 =0
n2 =1
if(terms>0):
    print("fabbonaci series")
    print(n1)
    print(n2)
    for i in range(terms):
        n3 = n1+n2
        print(n3)
        n1 = n2
        n2 = n3
else:
    print("invalid terms")
        
    
