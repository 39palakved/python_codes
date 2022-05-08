import time
seconds = time.time()
print(seconds)

num = int(input("enter any number"))

fact =1

for i in range(1,num+1):
    fact = fact*i
print(fact)


import time
seconds2 = time.time()
print(seconds)

def fact(num):
    if num==1:
        return 1
    else:
        fact1 = num*fact(num-1)
        return fact1

num = int(input("enter any number"))
func_val = fact(num)
print("factorial of num is", func_val)

f = open("factorialfile.text", 'w')
x = str(seconds)
y = str(seconds2)
z = str(fact)
m = str(func_val)

f.write(x+"\n")

f.write(y+"\n")
f.write(z+"\n")
f.write(m)
f.close()
