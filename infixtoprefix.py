# infix to prefix
n = int(input("enter how many element you want in list")) 
exp = [None]*n
for i in range(0,n):
    exp[i] = input()
print("our infix expression is")
for i in range(n):
     print(exp[i],end=" ")
top = -1

stack = [None]*n
str1 = [None]*n
def push(expr):
    global top
    if(top==n):
        print("stack overflow")
    else:
        top = top+1
        stack[top] = expr
def pop():
    global top
    global temp
    if(top==-1):
        print("stack underflow")
    else:
        temp = stack[top]
        top = top-1
        return temp;
def prec(opr):
    if(opr =='^'):
        return 3
    elif(opr =='*' or opr=='/'):
        return 2
    elif(opr=='+' or opr =='-'):
        return 1
    else:
        return -1
def infixtoprefix():

    k=0
    for i in range (n-1,-1,-1):
        if((exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z')):
            str1[k] = exp[i]
            k= k+1
        elif(exp[i]==')'):
             push(exp[i])
        elif (exp[i]=='('):
             while(stack[top]!=')'):
                p= pop()
                str1[k] = p
                k=k+1
             pop()
        else:
            while(top!=-1 and prec(exp[i])<= prec(stack[top])):
                p=pop()
                str1[k] = temp
                k=k+1
            push(exp[i])
    while(top!=-1):
        p = pop()
        str1[k] = p
        k=k+1
    print("our prefix expression is")
    for i in range(n-1,-1,-1):
        print(str1[i],end=" ")
infixtoprefix()
    

             


    
    
