num = int(input("enter how many elements you wan"))
exp = [None]*num

for i in range(num):
    exp[i]=str.lower(input())

stack  = [None]*num

str1 =[None]*num

print("our string is")
i=0
for i in range(num):
    print(exp[i],end="")
print("\n")
top =-1
def prec(opr):
    if(opr=='^'):
        return 3
    elif(opr == '*' or opr=='/' ):
        return 2
    elif(opr=='+' or opr =='-'):
        return 1
    else :
        return -1                                                      #list object is not callable error occur when we mistakly used round bracked on the place of
                                                                          #square like list1(i) in the place of list1[i]
def push(expr):
    global top
    global stack                                                              # we can define any list be using list1 = [None]*n
    if(top == num):
        print("stack overflow")
    else:
        top = top+1
        stack[top] = expr
def pop():
    global temp
    global stack
    global top
    if(top==-1):
        print("stackunderflow")
    else:
        temp = stack[top]
        top = top-1
        return temp
def infixtopostfix():
    
    
    global exp
    global top
    k=0
    i=0
    for i in range (num):
        if(exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z'):
          str1[k] = exp[i]
          k=k+1
        elif(exp[i] =='('):
            push(exp[i])
        elif(exp[i] ==')'):

            while(stack[top] != '('):
                
                j=pop()
                str1[k] = j
                k=k+1
            if(stack[top] == '('):
                pop()
        else:
            while(top !=-1 and  prec(exp[i])<= prec(stack[top])):
                  p = pop()
                  str1[k] = p 
                  k=k+1
            push(exp[i])
                
        
    while(top!=-1):
        p=pop()
        str1[k] = p
        k=k+1

    i=0
    for i in range(num):
        print (str1[i], end=" ")
    
    
infixtopostfix()
