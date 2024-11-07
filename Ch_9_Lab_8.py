# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Chris Bishop
# Description: Solution to Lab #8
# Author: Mauricio Arriaga
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

import random

# Dictionary of U.S. states and their capitals
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Initialize counters for correct and incorrect answers
correct_count = 0
incorrect_count = 0

# Conduct a quiz with 5 questions
for i in range(5):
    # Select a random state
    state = random.choice(list(state_capitals.keys()))
    # Prompt the user for the capital of the chosen state
    capital_guess = input(f"What is the capital of {state}? ")

    # Check if the answer is correct
    if capital_guess == state_capitals[state]:
        print("Correct!")
        correct_count += 1
    else:
        print(f"Incorrect. The capital of {state} is {state_capitals[state]}.")
        incorrect_count += 1

# Display the results
print("\nQuiz Results:")
print(f"Correct answers: {correct_count}")
print(f"Incorrect answers: {incorrect_count}")

