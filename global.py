"""count =1
def plus():
    count += 1
def minus():
    count -= 1
print("count=",count)
plus()
plus()
minus()
minus()
print("count=",count)"""
count =1
def plus():
    global count += 1
def minus():
    global count -= 1
print("count=",count)
plus()
plus()
minus()
minus()
print("count=",count)
