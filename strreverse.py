str1 = "palak"
length = len(str1)

for i in str1:
    print(i,"\n")

for j in range(length):
    print(str1[length-1])
    length = length -1
"""for i in range(length):
    str2[i] = str1[length-1]
    

for i in range(length):
    print(str2[i])"""
# if we want to declare any variable without assigning any value we can use None in the palce of valuereverse()
a = reverse(str1)
