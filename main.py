import random

'''
1 is snake
2 is water
3 is gun

'''

computer = random.choice([1 , 2 ,3]) 
youstr = input("enter your choice :")
youDict = {"s" :1 , "w" : 2, "g" :3}
reversedict = {1 : "Snake" , 2: "Water" ,3 : "Gun"}
you = youDict[youstr]

print(f'Computer choose  {reversedict[computer]} \nyour choice is {reversedict[you]}')

if((computer == you)):
   print("it's draw 🤦‍♂️")
else:
    if(computer == 1 and you == 2):
        print("you loose! 😢")

    elif(computer == 1 and you == 3):
        print("you win! 👏")

    elif(computer == 2 and you == 1):
        print("you win! 👏")

    elif(computer == 2 and you == 3):
        print("you loose! 😢")

    elif(computer == 3 and you == 1):
        print("you loose! 😢")

    elif(computer == 3 and you == 2):
        print("you win! 👏")

    else:
        print("somthing went wrong 🤦‍♂️")