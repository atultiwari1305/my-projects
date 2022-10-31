from ast import If
import random

user_choice=input("Enter your choice (rock/paper/scissor):")
possible_action=["rock","paper","scissor"]
computer_action=random.choice(possible_action)

print("YOUR INPUT IS: ",user_choice)
print("cOMPUTER INPUT IS: ",computer_action)

if user_choice=="rock":
    if computer_action=="rock":
        print("IT'S A TIE")
    if computer_action=="paper":
        print("YOU LOSE !!!!!")
    if computer_action=="scissor":
        print("YOU WIN !!!!!")

if user_choice=="paper":
    if computer_action=="rock":
        print("YOU WIN !!!!!")
    if computer_action=="paper":
        print("IT'S A TIE")
    if computer_action=="scissor":
        print("YOU LOSE !!!!!")

if user_choice=="scissor":
    if computer_action=="rock":
        print("YOU LOSE !!!!!")
    if computer_action=="paper":
        print("YOU WIN !!!!!")
    if computer_action=="scissor":
        print("IT'S A TIE")