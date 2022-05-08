def add(x,y):
    z = x+y
    return z
def sub(x,y):
    z= x-y
    return z
def mul(x,y):
    z= x*y
    return z
def div(x,y):
    z= x/y
    return z
def mod(x,y):
    z= x%y
    return z
def  square(x):
    z = x*x
    return z
def  cube(x):
    z = x*x*x
    return z
def  power(x):
    n = int(input("enter power u want"))
    z = x**n
    return z
def  sqroot(x):
    
    z = x**(0.5)
    return z
def cuberoot(x):
    z = x**(1/3)
    return z
print("Welcome to my calculater")

while True:
    op_choice = str.lower(input("which type of operation u want to peform unary or binary"))
    if(op_choice == 'unary'):
        num = int(input("enter number"))
    elif(op_choice == 'binary'):
        a = str.lower(input("enter which type of value (int,float) u want to enter"))
        if(a =='int'):
            num1 = int( input("enter first number"))
            num2 = int (input(" enter second number"))
            print("choose arithmetic operation")

        elif(a =='float'):
            num1 = float( input("enter first number"))
            num2 = float (input(" enter second number"))
            print("choose arithmetic operation")

        else:
            print("take value  either int or float")
    else:
        print("plz choose either unary or binary")


    choice = input("choose operation")


    if(choice == '+'):
        print(num1, "+",num2, "=", add(num1,num2))
    elif(choice == '-'):
        print(num1, "-",num2,"=", sub(num1,num2))
    elif(choice == '*'):
        print(num1, "*",num2,"=", mul(num1,num2))
    elif(choice == '/'):
        if(num2 == 0):
            print("zero division error")
        else :
           print(num1, "/",num2,"=", div(num1,num2))
    elif(choice == '%'):
         print(num1, "%",num2,"=", mod(num1,num2))
    elif(choice == 'sq'):
        print("square of",num,"=",square(num))
    elif(choice == 'cb'):
        print("cube of",num,"=",cube(num))
    elif(choice =='pow'):
        print("power of",num,"=",power(num))
    elif(choice =='sr'):
        print("square root of",num,"=",sqroot(num))
    elif(choice =='cr'):
        print("cube root of",num,"=",cuberoot(num))
    else:
        print("invalid choice")
    next_calculation = str.lower(input("do you want to perform more operation or not"))
    if(next_calculation == 'no'):
        break
    
    
