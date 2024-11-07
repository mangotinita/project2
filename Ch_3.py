# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Chris Bishop
# Description: Solution to Lab #2
# Author: (Student Mauricio Arriaga)


import random

# Pick a random number between 0 and 36
pocket = random.randint(0, 36)

if pocket == 0:
    color = "Green"
elif (1 <= pocket <= 10 or 19 <= pocket <= 28) and pocket % 2 != 0:
    color = "Red"
elif (1 <= pocket <= 10 or 19 <= pocket <= 28) and pocket % 2 == 0:
    color = "Black"
elif (11 <= pocket <= 18 or 29 <= pocket <= 36) and pocket % 2 != 0:
    color = "Black"
elif (11 <= pocket <= 18 or 29 <= pocket <= 36) and pocket % 2 == 0:
    color = "Red"

# Display the pocket number and its color
print(f"Pocket Number: {pocket}")
print(f"Color: {color}")


# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.


