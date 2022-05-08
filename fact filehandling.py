def fact(x):
    fact = 1
    if x == 1 or x == 0:
        return 1
    else:
        for i in range(1,x+1):
            fact = fact*i
        return fact
user_input = 5
y = fact(user_input)
print(user_input,y)
z="factorial of" +" "+ str(user_input) + "is" + str(y)

f=open("sample.txt","a")
f.write(z)
f.write("\n")
f.write("factorial of 3 is 6")
f.close()
