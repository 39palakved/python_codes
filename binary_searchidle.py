list1 = [2,8,5,3,9,11,16,20,32]

length = len(list1)
list1.sort()
print("after sorting the list")
for i in range(length-1):
      
    print( list1[i],end=" ")
num =int(input("eter any number for searching"))
first=0
last= length-1
mid =1
flag=0

while(mid!=-1 or mid!=length):
    mid= int((first+last)/2)
    if(list1[mid] == num):
         flag = 1
         break
    elif(list1[mid] > num):
         last = mid-1
         
    else:
        first = mid+1
if(flag==1):
    print("number found")

else:
    print("not found")
