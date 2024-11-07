from itertools import count
from os import times

# name = 'Juliet'
# for ch in name:
#     print(ch)

# name = 'Juliet'
# for ch in name:
#     ch = 'X'
# print(name)





# my_string = 'one two three four'
# word_list = my_string.split()
# print(word_list)
#
# my_string = '1/2/3/4/5'
# number_list = my_string.split('/')
# print(number_list)
#
# str = 'peach raspberry strawberry vanilla'
# tokens = str.split()
# print(tokens)
#
#
# my_address = 'WWW.example.com'
# tokens = my_address.split('.')

# count ts py
# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string

# def main():
#     # create a variable to use to hold the count
#     # The variable must start with 0
#     # appears in a string
#
#     count = 0
#     # get a string from the user
#     my_string =input('Enter a sentence: ')
#
#     # Count the Ts.
#     for ch in my_string:
#         if ch == 'T' or ch == 't':
#             count += 1
#
#     # Print the result
#     print(f'The letter T appears {count}  times.')
#
#     # Call the main function.
# if __name__ == '__main__':
#     main()

#
# my_string = 'Roses are red'
# ch = my_string[6]
# print(ch)
#
# my_string = 'Roses are red'
# print(my_string[0], my_string[6], my_string[10])
#
# my_string = 'roses are red'
# print(my_string[-1], my_string[-2], my_string[-13])

# IndexError Exceptions
# city = 'Boston'
# print(city[6])
#
# city = 'Boston'
# index = 0
# while index < 7:
#     print(city[index])
#     index += 1

# city = 'Boston'
# index = 0
# while index < 6:
#     print(city[index])
#     index += 1
#
# city = 'Boston'
# index = 0
# while index < 6:
#     print(city[index], end=" ")
#     index += 1

# The len Function
# city = 'Boston'
# size = len(city)
# print(size)

# city = 'Boston'
# index = 0
# while index < len(city):
#     print(city[index])
#     index += 1

# String Concatenation

# message = 'Hello ' + 'world'
# print(message)
#
# first_name = 'Emily'
# last_name = 'Arriaga'
# full_name = first_name + ' ' + last_name
# print(full_name)
#
# letters = 'abc'
# letters += 'def'
# print(letters)

# letters = 'abc'
# letters = letters + 'def'
# print(letters)


# String are immutable

# This program concatenates strings.
#
# def main()

# name = 'Kelly'
# name += '  '
# name += 'Yvonne'
# name += '  '
# name += 'Smith'
# print(name)

# Strings are immutable

# def main():
#     name = 'Carmen'
#     print(f'The name is: {name}')
#     name = name + ' Brown'
#     print(f'The name is: {name}')
# if __name__ == '__main__':
#     main()

# 8.1; (Noninteractive) checkpoint questions from the book
# Assume the variable name references a string. Write a for loop that prints each character in the string.

# name = 'Mauricio'
# for char in name:
#     print(char)
#
# # 8.2: What is the index of the first character in a string?
# name = 'Mauricio'
# first_char = name[0]
# print(first_char)

# # 8.3: If a string has 10 characters, what is the index of the last character?
# name = 'Mauricio'
# last_char = name[7]
# print(last_char)

# 8.4: What happens if you try to use an invalid index to access a character in a string?

# name = 'Mauricio'
# invalid_char = name[10]
# print(invalid_char)
#
# name = 'Mauricio'
# try:
#     invalid_char = name[10]
#     print(invalid_char)
# except ValueError as e:
#     print(f"Error: {e}")

# 8.5 How do you find the length of a string?
# name = 'Mauricio'
# len_of_string = len(name)
# print(len_of_string)

# animal = 'Tiger'
# animal[0] = 'L'
# print(animal)

# animal = 'Tiger'
# new_animal = 'L' + animal[1:]
# print(new_animal)
#
# full_name = 'Patty Lynn Smith'
# first_name = full_name[:5]
# print(first_name)

# full_name = 'Patty Lynn Smith'
# middle_name = full_name[6:10]
# print(middle_name)

# full_name = 'Patty Lynn Smith'
# first_name = full_name[:5]
# print(first_name)

# full_name   = 'Patty Lynn Smith'
# las_name = full_name[11:]
# print(las_name)

# full_name = 'Patty Lynn Smith'
# my_string = full_name[:]
# print(my_string)

#
# full_name = 'Patty Lynn Smith'
# my_string = full_name[0 : len(full_name)]
# print(my_string)

# full_name = 'Patty Lynn Smith'
# last_name = full_name[-5:]
# print(last_name)

# full_name = 'Parry Lynn Smith'
# my_string = full_name[0 : len(full_name)]
# print(my_string)

# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters[0:26:2])

# full_name = 'Patty Lynn Smith'
# las_name = full_name[-5:]
# print(las_name)

# In the Spotlight: extracting characters from a string

# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.

# def get_login_name(first, last, idnumbers):
#     set1 = first[0 : 3]
#     set2 = last[0 : 3]
#     set3 = idnumbers[-3 :]
#     login_name = set1 + set2 + set3
#     return login_name
# print(get_login_name('Mauricio', 'Arriaga', '123456789'))

# Generate_login.py)
#This program gets the user's first name, last name, and
#student ID number. Using this data it generates a
#system login name
#
# import login.py
#
# def main():
#     # get the user's first name, last name, and ID number.
#     first = input('Enter first name: ')
#     last = input('Enter your last name: ')
#     idnumber = input('Enter your student id: ')
#
#     # get the login name
#     print('Your system login name is:')
#     print(login.get_login_name(first, last, idnumber))
#
# if __name__ == '__main__':
#     main()

# main.py
# import login
#
# def main():
#     # Get the user's first name, last name, and ID number
#     first = input('Enter first name: ')
#     last = input('Enter your last name: ')
#     idnumber = input('Enter your student id: ')
#
#     # Get the login name from the login module
#     print('Your system login name is:')
#     print(login.get_login_name(first, last, idnumber))
#
# # Execute the main function when this script is run directly
# if __name__ == '__main__':
#     main()

# # main.py
# import login
#
# def main():
#     # Get the user's first name, last name, and ID number
#     first = input('Enter first name (at least 1 character): ')
#     last = input('Enter your last name (at least 1 character): ')
#     idnumber = input('Enter your student id (at least 1 character): ')
#
#     # Check that the inputs are valid
#     if len(first) < 1 or len(last) < 1 or len(idnumber) < 1:
#         print('Error: Please provide valid inputs for all fields.')
#         return
#
#     # Get the login name from the login module
#     print('Your system login name is:')
#     print(login.get_login_name(first, last, idnumber))
#
# # Execute the main function when this script is run directly
# if __name__ == '__main__':
#     main()

# login.py
# def get_login_name(first, last, idnumber):
#     # Get the first 3 characters of the first name
#     set1 = first[0:3] if len(first) >= 3 else first
#
#     # Get the first 3 characters of the last name
#     set2 = last[0:3] if len(last) >= 3 else last
#
#     # Get the last 3 characters of the ID number
#     set3 = idnumber[-3:] if len(idnumber) >= 3 else idnumber
#
#     # Concatenate the parts to form the login name
#     login_name = set1 + set2 + set3
#
#     # Return the generated login name
#     return login_name

# 8.2 (Noninteractive) checkpo9int questions from the book

# 8.7 What will the following code display?

# mystring = 'abcdefg'
# print(mystring[2:5])
#
# # 8.8 What will the following code display?
#
# mystring = 'abcdefg'
# print(mystring[3:])
#
# # 8.9 What will the following code display?
#
# mystring = 'abcdefg'
# print(mystring[:3])
#
# # 8.10 What will the following code display?
#
# mystring = 'abcdefg'
# print(mystring[:])

# 8.3 Testing, searching, and manipulating strings

# operators
# methods

# Testing strings with in and not in

# text = 'Four score and seven years ago'
# if 'seven' in text:
#     print('The string "seven" was found. ')
# else:
#     print('The string "seven" was not found. ')
#
# names = 'Bill Joanne Susan Chris Juan katie'
# if 'Pierre' not in names:
#     print('The string "Pierre" was not found. ')
# else:
#     print('The string "Pierre" was found. ')

# String Methods

# stringvar.method(arguments)

# string1 ='1200'
# if string1.isdigit():
#     print(f'{string1} contains only digits')
# else:
#     print(f'{string1} contain characters other than digits.')
#
# string2 = '123abc '
# if string2.isdigit():
#     print(f'{string1} contains only digits')
# else:
#     print(f'{string2} contain characters other than digits.')

# tring_test.py

# def main():
#     # Get a string from the user.
#     user_string = input('Enter a string: ')
#
#     print('This is what I found about that string:')
#
#     # Test the string.
#     if user_string.isalnum():
#         print('The string is alphanumeric.')
#     if user_string.isdigit():
#         print('The string contains only digits.')
#     if user_string.isalpha():
#         print('The string contains only alphabetic characters.')
#     if user_string.isspace():
#         print('The string contains only whitespace characters.')
#     if user_string.islower():
#         print('The letters in the string are all lowercase.')
#     if user_string.isupper():
#         print('The letters in the string are all uppercase.')
#
#
# # Call the main function
# if __name__ == '__main__':
#     main()

# letters = 'WXYZ'
# print(letters, letters.lower())
#
# letters = 'abcd'
# print(letters, letters.upper())

# Insensitive comparison
again = 'y'
while again.lower() == 'y':
    print('Hello')
    print('Do you want to see that again?')
    again = input('Y = yes, anything else = no:')





