'''
Workflow of our project 
==========================
1. User Choice = what the user want 
2. Computer Choice = what's the computer want( computer user randomly using random module )
3. result print

Cases: 
a - Rock - Rock = tie
b - Rock - Paper = i win 
c - Rock - Scissors = computer win
d - Paper - Rock = computer win 
e - Paper - Paper = tie
f - Paper - Scissors = i win
g - Scissors - Rock = i win
h - Scissors - Paper = computer win
i - Scissors - Scissors = tie
'''
# first we import the random module
import random 

# we create a list 
choices = ['rock', 'paper', 'scissors']
# create var for user and computer  choices 
user_choice = input("Enter a choice (rock, paper, scissors): ")
computer_choice = random.choice(choices)# here choice is a list and random.choice is a function it is used for choose 
print(f"User_Choice is: {user_choice} and Computer_Choice is {computer_choice}");

# used conditional statement 
if (user_choice == computer_choice):
    print("Both Choose same So the game is: Tie")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("You choose rock and computer choice is paper so the paper is cover the rock so : Computer Win")
elif(user_choice == "rock" and computer_choice == "scissors"):
    print("You choose rock and computer choice is scissors so rock will brake the scissors so : You Win")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("You choose paper and computer choice is rock so paper covered the rock : You Win")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("You choose paper and computer choice is scissors so scissor will cut the paper so : Computer Win")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("You choose scissors and computer choice is paper so scissor will cut the paper so: You Win")
elif(user_choice == "scissors" and computer_choice == "rock"):
    print("You choose scissors and computer choice is rock so rock will brake the scissors so : Computer Win")
else:
    print("Invalid Input")
