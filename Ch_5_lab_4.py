
# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Chris Bishop
# Description: Solution to Lab 4
# Author: Mauricio Arriaga

# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.   # 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

import random
print("Welcome to Rock, Paper, Scissor!")
while True:
    player = int(input("Enter 1 for rock, 2 for paper, 3 for scissors "))
    computer_choice = random.randint(1, 3)
    print("Computer chose: ", computer_choice)
    print("Player chose: ", player)
    if player == computer_choice:
        print("It's a tie!")
    elif player == 1:
        if computer_choice == 3:
            print("Player wins!")
        else:
            print("Computer wins!")
    elif player == 2:
        if computer_choice == 1:
            print("Player wins!")
        else:
            print("Computer wins!")
    elif player == 3:
        if computer_choice == 2:
            print("Player wins!")
        else:
            print("Computer wins!")
    start_over = input("Would you like to play again? (y/n) ")
    if start_over != "y":
        print("Thank you for playing!")
        break









