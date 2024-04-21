#Create a simple Tic Tac Toe game that can be played between two players or against the computer.

#Import the module
import random

#Make the list by the name of game and give 3 parameters R, P, S

Game = ["Rock", "Paper", "Scissor"]

#Make the user input and computer choice

user_input = input("Choose Rock, Paper, Scissor : ")

computer_choose = random.choice(Game)

#Use Print function to define user choose and computer choose
print("You choose : ", user_input)
print("Computer choose : ", computer_choose)

#Using if else

if user_input == computer_choose:
    print("It's tie.")

elif user_input == "Rock" and computer_choose == "Paper":
    print("You Win the game.")

elif user_input == "Paper" and computer_choose == "Rock":
    print("You win the game.")

elif user_input == "Scissor" and computer_choose == "Paper":
    print("You Win the game.")

elif user_input == "Rock" and computer_choose == "Scissor":
    print("You win the game.")

else:
    print("Computer win the game.")