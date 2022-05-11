import random
print("value1 -> means scissors")
print("value2 -> means stone")
print("value 3 -> means paper")

user_choice = int(input("enter your choice"))
print(user_choice)
computer_choice= random.randint(1,3)
print(computer_choice)
if(user_choice == 1):
    if(computer_choice == 1):
        print("match is tie")
    elif(computer_choice == 2):
        print("you lost the match")
    elif(computer_choice == 3):
        print("you won the match")
    else:
        print("computer take wrong choice")
elif(user_choice == 2):
    if(computer_choice == 1):
        print("you won the match")
    elif(computer_choice == 2):
        print("match is tie")
    elif(computer_choice == 3):
        print("you lost the match")
    else:
        print("computer take wrong choice")
elif(user_choice == 3):
    if(computer_choice == 1):
        print("you lost the match")
    elif(computer_choice == 2):
        print("you won the match")
    elif(computer_choice == 3):
        print("match tie")
    else:
        print("computer take wrong choice")
else:
    print("you enter wrong choice")
