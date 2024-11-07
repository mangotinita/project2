# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Chris Bishop
# Description: Solution to Lab # 7
# Author: Mauricio Arriaga
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

# Morse code dictionary
# MORSE_CODE_DICT = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
#     'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
#     'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
#     'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
#     '7': '--...', '8': '---..', '9': '----.', '0': '-----',
#     ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
#     '(': '-.--.', ')': '-.--.-', ' ': ' '
# }
#
#
# # Function to convert a string to Morse code
# def string_to_morse(input_string):
#     morse_code = ""
#     for char in input_string.upper():  # Convert input to uppercase for matching dictionary
#         morse_code += MORSE_CODE_DICT.get(char, '') + ' '  # Append Morse code with space between characters
#     return morse_code
#
#
# # Main code
# if __name__ == "__main__":
#     # Ask user for input
#     user_string = input("Enter the string to be converted to Morse code: ")
#
#     # Convert to Morse code
#     morse_output = string_to_morse(user_string)
#
#     # Display the result
#     print(morse_output)
