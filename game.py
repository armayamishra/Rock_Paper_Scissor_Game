import random
computer = random.choice([1,2,3])
choice = input("Enter your choice: ")
dic = {"s": 1,
       "p": 2,
       "r": 3}
revdic = {1: "Scissor", 2: "Paper", 3:"Rock"}

you = dic[choice]
print(f"You Chose {revdic[you]} \nComputer Chose {revdic[computer]}")
if(computer == you):
    print("Oops, Game draw!")
else:
    if(computer == 1 and you == 2): 
        print("Sorry, You lose!")
    elif(computer == 1 and you == 3):
        print("Congrats, You win!")
    
    elif(computer == 2 and you == 1):
        print("Congrats, You win!")
    elif(computer == 2 and you == 3):
        print("Sorry, You lose!")
    
    elif(computer == 3 and you == 1):
        print("Sorry, You lose!")
    elif(computer == 3 and you == 2):
        print("Congrats, You win!")
    
    else:
        print("Something went wrong")