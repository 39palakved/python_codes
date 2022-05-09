# find lcm of number
def cal_lcm(x,y):
    if(x>y):
        greater =x
    else:
        greater =y
    while(True):
        if(greater%x==0 and greater%y==0):
            lcm = greater
            break
        greater = greater +1
    return lcm
def user_input():
    x = int(input("enter first number"))
    y = int(input("enter second number"))
    return(x,y)
x,y = user_input()
print("lcm of the number is",cal_lcm(x,y))
    
