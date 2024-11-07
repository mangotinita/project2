# # In Python, an object is essentially any entity that has a state (data) and behavior (functionality). Python, being
# # an object-oriented programming (OOP) language, treats everything as an object, including things like numbers, strings,
# # lists, and functions.
# from copyreg import pickle

# # Key Characteristics of an Object:
# # State (Attributes): The state of an object is represented by its attributes or properties. These are variables that
# # store data related to the object.
# # Behavior (Methods): Behavior refers to the functions (methods) associated with the object that define what it can do.
# # Identity: Every object has a unique identity, which can be checked with the id() function in Python. The identity is
# # essentially the object’s address in memory.
# # Example of Creating an Object:
# # python
# # class Car:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #
# #     def display_info(self):
# #         print(f"Car: {self.brand} {self.model}")
# #
# # # Creating an object of the Car class
# # my_car = Car("Toyota", "Corolla")

# # # Accessing attributes
# # print(my_car.brand)  # Output: Toyota

# # # Calling methods
# # my_car.display_info()  # Output: Car: Toyota Corolla
# # Here, my_car is an object (or instance) of the Car class. It has attributes like brand and model, and a method
# # display_info() that defines its behavior.

# # give some of the dictionaries method

# # In Python, dictionaries are key-value pairs and come with various built-in methods to interact with the data they hold
# # Here are some common dictionary methods:

# # 1. dict.get(key, default)
# # Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default
# # is specified).

# # my_dict = {'name': 'Alice', 'age': 25}
# # print(my_dict.get('name'))  # Output: Alice
# # print(my_dict.get('gender', 'Not Specified'))  # Output: Not Specified

# # 2. dict.keys()
# # Returns a view object that displays a list of all the keys in the dictionary.

# # print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# # 3. dict.values()
# # Returns a view object that displays all the values in the dictionary.
# # print(my_dict.values())  # Output: dict_values(['Alice', 25])

# # 4. dict.items()
# # Returns a view object that displays a list of all the key-value pairs as tuples.
# # print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

# # 5. dict.update(other_dict)
# # Updates the dictionary with elements from another dictionary or from key-value pairs. If a key already exists,
# # it will update the value.

# # my_dict.update({'age': 26, 'gender': 'Female'})
# # print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'gender': 'Female'}
# # 6. dict.pop(key, default)
# # Removes the specified key and returns its value. If the key is not found, it returns the default value (or raises a
# # KeyError if no default is provided).

# # age = my_dict.pop('age')
# # print(age)  # Output: 26
# # print(my_dict)  # Output: {'name': 'Alice', 'gender': 'Female'}

# # 7. dict.popitem()
# # Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.

# # item = my_dict.popitem()
# # print(item)  # Output: ('gender', 'Female')
# # print(my_dict)  # Output: {'name': 'Alice'}

# # 8. dict.clear()
# # Removes all items from the dictionary, leaving it empty.

# # my_dict.clear()
# # print(my_dict)  # Output: {}

# # 9. dict.copy()
# # Returns a shallow copy of the dictionary.

# # original_dict = {'name': 'Bob', 'age': 30}
# # new_dict = original_dict.copy()
# # print(new_dict)  # Output: {'name': 'Bob', 'age': 30}

# # 10. dict.fromkeys(iterable, value)
# # Creates a new dictionary with keys from the iterable and all values set to the specified value (or None if not
# # provided).

# # keys = ['name', 'age', 'gender']
# # new_dict = dict.fromkeys(keys, 'Unknown')
# # print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'gender': 'Unknown'}

# # 9.3 Suppose 'start' : 1472 is an element in a dictionary.
# # What is the key? What is the value?

# # Example dictionary
# example_dict = {'start': 1472}

# # Key: 'start'
# # Value: 1472
# print(f"Key: 'start', Value: {example_dict['start']}")

# # 9.4 Suppose a dictionary named employee has been created.
# # What does the following statement do?

# employee = {}
# employee['id'] = 54321
# print(f"Employee ID: {employee['id']}")  # It adds/updates the 'id' key in the dictionary.

# # 9.5 What will the following code display?
# stuff = {1: 'aaa', 2: 'bbb', 3: 'ccc'}
# print(stuff[3])  # Output will be 'ccc'

# # 9.6 How can you determine whether a key-value pair exists in a dictionary?

# # Example check for key existence
# if 2 in stuff:
#     print("Key 2 exists in the dictionary.")
# else:
#     print("Key 2 does not exist in the dictionary.")

# # 9.7 Suppose a dictionary named inventory exists.
# # What does the following statement do?

# inventory = {654: "item1", 123: "item2"}
# del inventory[654]  # This deletes the key-value pair with key 654 from the dictionary.

# # 9.8 What will the following code display?

# stuff = {1: 'aaa', 2: 'bbb', 3: 'ccc'}
# print(len(stuff))  # Output will be 3 because there are three key-value pairs in the dictionary.
#
# # 9.9 What will the following code display?

# stuff = {1: 'aaa', 2: 'bbb', 3: 'ccc'}
# for k in stuff:
#     print(k)  # This will print the keys: 1, 2, 3 (each on a new line).

# # 9.10 What is the difference between the dictionary methods pop and popitem?
# # pop(key) removes and returns the value associated with a specific key.
# # popitem() removes and returns the last key-value pair added to the dictionary.

# # 9.11 What does the items method return?
# # items() returns a view object containing the dictionary's key-value pairs as tuples.
# print(stuff.items())  # Output: dict_items([(1, 'aaa'), (2, 'bbb'), (3, 'ccc')])

# # 9.12 What does the keys method return?
# # keys() returns a view object that displays a list of all the keys.
# print(stuff.keys())  # Output: dict_keys([1, 2, 3])

# # 9.13 What does the values method return?
# # values() returns a view object that displays a list of all the values.
# print(stuff.values())  # Output: dict_values(['aaa', 'bbb', 'ccc'])

# # 9.14 Assume the following list exists:
# names = ['Chris', 'Katie', 'Joanne', 'Kurt']
# # Write a statement that uses a dictionary comprehension to create a dictionary
# # in which each element contains a name from the names list as its key,
# # and the length of that name as its value.

# name_lengths = {name: len(name) for name in names}
# print(name_lengths)  # Output: {'Chris': 5, 'Katie': 5, 'Joanne': 6, 'Kurt': 4}
#
# # 9.15 Assume the following dictionary exists:
# phonebook = {
#     'Chris': '919-555-1111',
#     'Katie': '828-555-2222',
#     'Joanne': '704-555-3333',
#     'Kurt': '919-555-3333'
# }
# # Write a statement that uses a dictionary comprehension to create a second dictionary
# # containing the elements of phonebook that have a value starting with '919'.
#
# filtered_phonebook = {name: number for name, number in phonebook.items() if number.startswith('919')}
# print(filtered_phonebook)  # Output: {'Chris': '919-555-1111', 'Kurt': '919-555-3333'}

# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])
# result=set2.issubset(set1)
# print(result)

# set1.issuperset(set2)
# result=set1.issuperset(set2)
# print(result)

# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])
# set2 <= set1
# print(set2)

# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])
# set2 <= set1
# print(set2)

# # Code to evaluate and return the boolean result
# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])

# # Check if set2 is a subset of set1 using the <= operator
# is_subset = set2 <= set1
# print(is_subset)

# # Code to evaluate and return the boolean result
# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])

# # Check if set2 is a subset of set1 using the <= operator
# is_subset = set1 >= set2
# print(is_subset)

# # Code to evaluate and return the boolean result
# set1 = set([1, 2, 3, 4, 5])
# set2 = set([2, 3])

# # Check if set2 is a subset of set1 using the <= operator
# is_subset = set1 <= set2
# print(is_subset)

# # In the spotlight: set operations

# # Create two sets: one for the baseball team and one for the basketball team
# baseball_team = {"John", "Mike", "Sam", "Jake", "Tim"}
# basketball_team = {"Jake", "Tim", "Larry", "Mike", "Tom"}

# # Find the intersection of the two sets (students who play both sports)
# both_sports = baseball_team.intersection(basketball_team)
# print("Students who play both sports:", both_sports)

# # Find the union of the two sets (students who play either sport)
# either_sport = baseball_team.union(basketball_team)
# print("Students who play either sport:", either_sport)

# # Find the difference of baseball team and basketball team (students who play baseball but not basketball)
# only_baseball = baseball_team.difference(basketball_team)
# print("Students who play baseball but not basketball:", only_baseball)
#
# # Find the difference of basketball team and baseball team (students who play basketball but not baseball)
# only_basketball = basketball_team.difference(baseball_team)
# print("Students who play basketball but not baseball:", only_basketball)

# # Create two sets: one for the baseball team and one for the basketball team
# # baseball_team = {"John", "Mike", "Sam", "Jake", "Tim"}
# # basketball_team = {"Jake", "Tim", "Larry", "Mike", "Tom"}

# 1. Find the intersection of the two sets (students who play both sports)
# # both_sports = baseball_team.intersection(basketball_team)
# # print("Students who play both sports:", both_sports)

# 2. Find the union of the two sets (students who play either sport)
# # either_sport = baseball_team.union(basketball_team)
# # print("Students who play either sport:", either_sport)

# # # 3. Find the difference of the baseball team and basketball team (students who play baseball but not basketball)
# # only_baseball = baseball_team.difference(basketball_team)
# # print("Students who play baseball but not basketball:", only_baseball)

# # # 4. Find the difference of basketball team and baseball team (students who play basketball but not baseball)
# # only_basketball = basketball_team.difference(baseball_team)
# # print("Students who play basketball but not baseball:", only_basketball)

# # This program demonstrates various set operations.
# baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
# basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# # Display members of the baseball set.
# print('The following students are on the baseball team:')
# for name in baseball:
#     print(name)

# # Display members of the basketball set.
# print()
# print('The following students are on the basketball team:')
# for name in basketball:
#     print(name)

# # Demonstrate intersection
# print()
# print('The following students play both baseball and basketball:')
# for name in baseball.intersection(basketball):
#     print(name)

# # Demonstrate union
# print()
# print('The following students play either baseball or basketball:')
# for name in baseball.union(basketball):
#     print(name)

# # Demonstrate difference of baseball and basketball
# print()
# print('The following students play baseball, but not basketball:')
# for name in baseball.difference(basketball):
#     print(name)

# # Demonstrate difference of basketball and baseball
# print()
# print('The following students play basketball, but not baseball:')
# for name in basketball.difference(baseball):
#     print(name)

# # Demonstrate symmetric difference
# print()
# print('The following students play one sport, but not both:')
# for name in baseball.symmetric_difference(basketball):
#     print(name)

# # 9.2 Noninteractive checkpoint questions from the book
# 9.16 Are the elements of a set ordered or unordered?
# Answer: Unordered.

# 9.17 Does a set allow you to store duplicate elements?
# Answer: No, sets do not allow duplicate elements.

# 9.18 How do you create an empty set?
# Answer: myset = set()

# 9.19 After the following statement executes, what elements will be stored in the myset set?
# myset = set('Jupiter')

# 9.20 After the following statement executes, what elements will be stored in the myset set?
# myset = set(25)
# Answer: This will raise a TypeError because the set() function expects an iterable, and 25 is not iterable.

# 9.21 After the following statement executes, what elements will be stored in the myset set?
# myset = set([1, 2, 2, 3, 4, 4])
# Answer: {'w', 'x', 'y', 'z', ' '}

# 9.22 After the following statement executes, what elements will be stored in the myset set?
# myset = set([1, 2, 2, 3, 4, 4])
# Answer: {1, 2, 3, 4}

# 9.23 After the following statement executes, what elements will be stored in the myset set?
# myset = set(['www', 'xxx', 'yyy', 'zzz'])
# Answer: {'www', 'xxx', 'yyy', 'zzz'}

# 9.24 How do you determine the number of elements in a set?
# Answer: Use the len() function. Example: len(myset)

# 9.25 After the following statement executes, what elements will be stored in the myset set?
# myset = set([10, 9, 8])
# myset.update([1, 2, 3])
# print(myset)

# myset = set([10, 9, 8])
# myset.update([10, 9, 8])
# print(myset)

# # 9.26 After the following statement executes, what elements will be stored in the myset set?
# myset = set([10, 9, 8])
# myset.update('abc')
# print(myset)

# 9.27 What is the difference between the remove and discard methods?
# Answer: remove(): Removes the specified element. If the element is not found, it raises a KeyError.
# discard(): Removes the specified element. If the element is not found, it does not raise an error.

# 9.28 How can you determine whether a specific element exists in a set?
# Use the in operator.
# Example:
# if 5 in myset:
#     print("5 is in the set")

# # 9.29 After the following code executes, what elements will be members of set3?

# # 9.29 After the following code executes, what elements will be members of set 3?
# set1 = set([10, 20, 30])
# set2 = set([100, 200, 300])
# set3 = set1.union(set2)
# print(set3)

# # 9.30 After the following code executes, what elements will be members of set3?
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.intersection(set2)
# print(set3)

# # 9.31 After the following code executes, what element will be members of set3?
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.difference(set2)
# print(set3)

# # 9.32 After the following code executes, what elements will be members of set 3?
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set2.difference(set1)
# print(set3)

# # 9.33 After the following code executes, what elements will be members of set3?
# set1 = set(['a', 'b', 'c'])
# set2 = set(['b', 'c', 'd'])
# set3 = set1.symmetric_difference(set2)
# print(set3)

# # 9.34 Look at the following code:
# set1 = set([1, 2, 3, 4])
# set2 = set([2, 3])
# print(set1)
# print(set2)

# # Which of the sets is a subset of the other?
# # Set2 is a subset of set1,

# # Which of the sets is a superset of the other?
# # Set1 is a sujperset of set2

# SERIALIZATION
#    import pickle()
#       dump method
#    import JSON

# This program demonstrates object pickling.
# import pickle

# # main function
# def main():
#     again = 'y'  # To control loop repetition

#     # Open a file for binary writing.
#     with open('info.dat', 'wb') as output_file:
#         # Get data until the user wants to stop.
#         while again.lower() == 'y':
#             # Get data about a person and save it.
#             save_data(output_file)

#             # Does the user want to enter more data?
#             again = input('Enter more data? (y/n): ')

# # The save_data function gets address data about a person,
# # stores it in a dictionary, and then pickles the
# # dictionary to the specified file.
# def save_data(file):
#     # Create an empty dictionary.
#     person = {}

#     # Get data for a person and store
#     # it in the dictionary.
#     person['name'] = input('Name: ')
#     person['street number'] = int(input('Street Number: '))
#     person['street name'] = input('Street Name: ')

#     # Pickle the dictionary.
#     pickle.dump(person, file)

# # Call the main function.
# if __name__ == '__main__':
#     main()

# This program demonstrates object unpickling.
# import pickle

# # main function
# def main():
#     end_of_file = False  # To indicate end of file

#     # Open a file for binary reading.
#     with open('info.dat', 'rb') as input_file:
#         # Read to the end of the file.
#         while not end_of_file:
#             try:
#                 # Unpickle the next object.
#                 person = pickle.load(input_file)

#                 # Display the object.
#                 display_data(person)
#             except EOFError:
#                 # Set the flag to indicate the end
#                 # of the file has been reached.
#                 end_of_file = True

# # The display_data function displays the person data
# # in the dictionary that is passed as an argument.
# def display_data(person):
#     print('Name:', person['name'])
#     print('Street Number:', person['street number'])
#     print('Street Name:', person['street name'])
#     print()

# # Call the main function.
# if __name__ == '__main__':
#     main()

# 9.3: (Noninteractive) Checkpoint Questions
# 9.35 What is object serialization?

# Answer: Object serialization is the process of converting an object into a format that can be saved to a file or transmitted over a network and later reconstructed.
# 9.36 When you open a file for the purpose of saving a pickled object to it, what file access mode do you use?

# Answer: You use 'wb' (write binary) mode.
# 9.37 When you open a file for the purpose of retrieving a pickled object from it, what file access mode do you use?

# Answer: You use 'rb' (read binary) mode.
# 9.38 What module do you import if you want to pickle objects?

# Answer: You import the pickle module.
# 9.39 What function do you call to pickle an object?

# Answer: You use the pickle.dump() function.
# 9.40 What function do you call to retrieve and unpickle an object?

# Answer: You use the pickle.load() function.

# 9: Review Questions (Multiple Choice)
# You can use the ________ operator to determine whether a key exists in a dictionary.
#
# Answer: b. in
# You use ________ to delete an element from a dictionary.
#
# Answer: d. the del statement

# The ________ function returns the number of elements in a dictionary:

# Answer: b. len()
# You can use ________ to create an empty dictionary.

# Answer: a. {}
# The ________ method returns a randomly selected key-value pair from a dictionary.

# Answer: c. popitem()
# The ________ method returns the value associated with a specified key and removes that key-value pair from the dictionary.

# Answer: a. pop()
# The ________ dictionary method returns the value associated with a specified key. If the key is not found, it returns a default value.

# Answer: d. get()
# The ________ method returns all of a dictionary’s keys and their associated values as a sequence of tuples.

# Answer: c. items()

# You can add a group of elements to a set with this method.
# Answer: c. update
# This set method removes an element but does not raise an exception if the element is not found.
# Answer: b. discard
# This set method removes an element and raises an exception if the element is not found.
# Answer: a. remove
# This operator can be used to find the union of two sets.
# Answer: a. |
# This operator can be used to find the difference of two sets.
# Answer: c. -

# This operator can be used to find the intersection of two sets.
# Answer: b. &
# This operator can be used to find the symmetric difference of two sets.
# Answer: d. ^

# True or False
# The keys in a dictionary must be mutable objects.
#
# Answer: False. Dictionary keys must be immutable (e.g., strings, numbers, tuples).
# Dictionaries are not sequences.
#
# Answer: True. Dictionaries are collections of key-value pairs and do not maintain sequential order.
# A tuple can be a dictionary key.
#
# Answer: True. Tuples are immutable, so they can be used as dictionary keys.
# A list can be a dictionary key.
#
# Answer: False. Lists are mutable, so they cannot be used as dictionary keys.
# The dictionary method popitem does not raise an exception if it is called on an empty dictionary.
#
# Answer: False. popitem raises a KeyError if called on an empty dictionary.
# The following statement creates an empty dictionary:
#
# python
# Copy code
# mydct = {}
# Answer: True. {} creates an empty dictionary.
# The following statement creates an empty set:
#
# python
# Copy code
# myset = ()
# Answer: False. () creates an empty tuple, not a set. An empty set is created using set().
# Sets store their elements in an unordered fashion.
#
# Answer: True. Sets are unordered collections.
# You can store duplicate elements in a set.
#
# Answer: False. Sets do not allow duplicate elements.
# The remove method raises an exception if the specified element is not found in the set.
#
# Answer: True. remove raises a KeyError if the element is not found in the set.
# Short Answer
# What will the following code display?
#
# python
# Copy code
# dct = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
# print(dct['Tuesday'])
# Answer: 2 (The value associated with the key 'Tuesday')
# What will the following code display?
#
# python
# Copy code
# dct = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
# print(dct.get('Monday', 'Not found'))
# Answer: 1 (The value associated with the key 'Monday')
# What will the following code display?
#
# python
# Copy code
# dct = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
# print(dct.get('Friday', 'Not found'))
# Answer: Not found (The key 'Friday' is not in the dictionary, so the default value 'Not found' is returned)

# 5. How do you delete an element from a dictionary?
# To delete an element from a dictionary, use the del statement with the key of the item you want to remove. Here’s an example:
#
# python
# Copy code
# # Example dictionary
# stuff = {'aaa': 111, 'bbb': 222, 'ccc': 333}
#
# # Deleting the element with key 'bbb'
# del stuff['bbb']
# print(stuff)  # Output will be {'aaa': 111, 'ccc': 333}
# 6. How do you determine the number of elements that are stored in a dictionary?
# To get the number of elements in a dictionary, use the len() function. Here’s an example:
#
# python
# Copy code
# # Example dictionary
# stuff = {'aaa': 111, 'bbb': 222, 'ccc': 333}
#
# # Getting the number of elements
# num_elements = len(stuff)
# print(num_elements)  # Output will be 3
# 7. What will the following code display?
# python
# Copy code
# stuff = {'aaa': 111, 'bbb': 222, 'ccc': 333}
# print(stuff.get('ddd', 'Not Found'))
# Answer: Not Found (The key 'ddd' does not exist in the dictionary, so the default value 'Not Found' is returned)



















# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #X
# Author: (Student Name Here)
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.


import random

# Dictionary containing U.S. states and their capitals


# main function
def main():
    again = 'y'  # To control loop repetition

    # Open a file for binary writing.
    with open('SanAndres.dat', 'wb') as output_file:
        # Get data until the user wants to stop.
        while again.lower() == 'y':
            # Get data about a person and save it.
            save_data(output_file)

            # Does the user want to enter more data?
            again = input('Enter more data? (y/n): ')

# The save_data function gets address data about a person,
# stores it in a dictionary, and then pickles the
# dictionary to the specified file.
# def save_data(file):
#     # Create an empty dictionary.
#     person = {}
#
#     # Get data for a person and store
#     # it in the dictionary.
#     person['name'] = input('Name: ')
#     person['street number'] = int(input('Street Number: '))
#     person['street name'] = input('Street Name: ')
#
#     # Pickle the dictionary.
#     pickle.dump(person, file)
#
# # Call the main function.
# if __name__ == '__main__':
#     main()


Grocery List




