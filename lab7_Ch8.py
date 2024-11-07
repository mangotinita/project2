# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Chris Bishop
# Description: Solution to Lab # 7
# Author: Mauricio Arriaga

# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

# Create arrays to contain all the Morse code symbols
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
              '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
              '..-', '...-', '.--', '-..-', '-.--', '--..',
              '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
              '---..', '----.']

# Ask the user for input
user_input = input("Enter the string to be converted to Morse code: ")

# Convert input into Morse code
result = ""

for char in user_input.upper():
    if char == ' ':
        result += '  '
    elif char in letters:
        index = letters.index(char)
        result += morse_code[index] + ' '
    else:
        # For characters not in letters list, we can skip or display a placeholder
        result += '? '

# Display the result
print("Morse Code:")
print(result)
