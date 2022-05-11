str1 = input("enter a string")
length = len(str1)
j = length-1
flag = 0

for i in range(length-1):
    if(str1[i] != str1[j]):
        flag = 1
        break
    j=j-1
if(flag==1):
    print("not palindrom")
else:
    print("palindrom")
    
        
    
