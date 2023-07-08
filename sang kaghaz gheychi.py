import random

print("rock...paper...scissor")

lap = int(input("please return lap? "))
for num in range(1,lap):
    user = input("please return your choise? ")

    number = random.randint(1,3)
    
    player = ""
    if number == 1 :
        player = "rock"
        print("player choise rock")
    elif number == 2 :
        player = "paper"
        print("player choise paper")
    elif number == 3 :
        player = "scissor"
        print("player choise scissor")

    if player == "rock" and user =="paper":
        print("user win")  
    elif player == "rock" and user =="scissor":
        print("player win")  
    elif player == "paper" and user =="rock":
        print("player win") 
    elif player == "paper" and user =="scissor":
        print("user win")  
    elif player == "rock" and user =="paper":
        print("user win")    
    elif player == "scissor" and user =="rock":
        print("user win") 
    elif player == "scissor" and user =="paper":
        print("player win")
    else:
        print("equls !")