f = open("myfirstfile.txt",'w')
x ="hello world"
f.write(x)
y="jai shree ram"
f.write("\n")
f.write(y)
f.close()
# reading
f = open("myfirstfile.txt", 'r')
x = f.read()
y =f.read()
print(x)
f.close()
