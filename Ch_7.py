# # # Chapter 7 Lists and Tuple
# #
# # numbers = [5, 10, 15, 20]
# # print(numbers)
# #
# # # List function
# # numbers = list(range(5))
# # print(numbers)
# #
# # numbers = list(range(1, 10, 2))
# # print(numbers)
# #
# # # The Repetition Operator
# # numbers = [0] * 5
# # print(numbers)
# #
# # # Iterating over a list with the loop
# # numbers = [1, 2, 3, 4]
# # for number in numbers:
# #     print(number)
# #
# # # Iterating over the list
# # numbers = [1, 1, 3, 4]
# # for number in numbers:
# #     num = 99
# # print(numbers)
# #
# # # Indexing
# # my_list = [10, 20, 30, 40]
# # print(my_list[0], my_list[1], my_list[2], my_list[3])
# #
# # index = 0
# # while index < 4:
# #     print(my_list[index])
# #     index += 1
# #
# # my_list = [10, 20, 30, 40]
# # print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])
# #
# #
# # # The len Function
# # my_list = [10, 20, 30, 40]
# # size = len(my_list)
# # print(len(my_list))
# #
# # # Using a for loop to iterate by index over a list
# # names = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
# # for index in range(len(names)):
# #     print(names[index])
# #
# # # Lists are mutable
# # numbers = [1, 2, 3, 4, 5]
# # print(numbers)
# # numbers[0] = 99
# # print(numbers)
# #
# # # number = [1, 2, 3, 4, 5]
# # # numbers[5] = 99
# # # print(number)
# #
# # # Concatenating Lists
# # list1 = [1, 2, 3, 4]
# # list2 = [5, 6, 7, 8]
# # list3 = list1 + list2
# #
# # girl_names = ['Joanne', 'Karen', 'Lori']
# # boy_names = ['Chris', 'Jerry', 'Will']
# # all_names = girl_names + boy_names
# # print(all_names)
# #
# # list1 = [1, 2, 3, 4]
# # list2 = [5, 6, 7, 8]
# # list1 += list2
# # print(list1)
# #
# # # 7.2 (Noninteractive) Checkpoint questions from the book
# #
# # # 7.1
# # numbers = [1, 2, 3, 4, 5]
# # numbers[2] = 99
# # print(numbers)  # Output: [1, 2, 99, 4, 5]
# #
# # # 7.2
# # numbers = list(range(3))
# # print(numbers)  # Output: [0, 1, 2]
# #
# # # 7.3
# # numbers = [10] * 5
# # print(numbers)  # Output: [10, 10, 10, 10, 10]
# #
# # # 7.4
# # numbers = list(range(1, 10, 2))
# # for n in numbers:
# #     print(n)  # Output: 1, 3, 5, 7, 9 (each on a new line)
# #
# # # 7.5
# # numbers = [1, 2, 3, 4, 5]
# # print(numbers[-2])  # Output: 4
# #
# # # 7.6
# # # To find the number of elements in a list, use the len() function.
# #
# # # 7.7
# # numbers1 = [1, 2, 3]
# # numbers2 = [10, 20, 30]
# # numbers3 = numbers1 + numbers2
# # print(numbers1)  # Output: [1, 2, 3]
# # print(numbers2)  # Output: [10, 20, 30]
# # print(numbers3)  # Output: [1, 2, 3, 10, 20, 30]
# #
# # # 7.8
# # numbers1 = [1, 2, 3]
# # numbers2 = [10, 20, 30]
# # numbers2 += numbers1
# # print(numbers1)  # Output: [1, 2, 3]
# # print(numbers2)  # Output: [10, 20, 30, 1, 2, 3]
# #
# # # List Slicing
# # days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# # mid_days = days[2:5]
# # print(mid_days)
# #
# # numbers = [1, 2, 3, 4, 5]
# # print(numbers)
# # print(numbers[1:3])
# #
# # # 7.3: (Noninteractive) Checkpoint questions from the book
# # # 7.9
# # numbers = [1, 2, 3, 4, 5]
# # my_list = numbers[1:3]
# # print(my_list)  # Output: [2, 3]
# #
# # # 7.10
# # numbers = [1, 2, 3, 4, 5]
# # my_list = numbers[1:]
# # print(my_list)  # Output: [2, 3, 4, 5]
# #
# # # 7.11
# # numbers = [1, 2, 3, 4, 5]
# # my_list = numbers[:1]
# # print(my_list)  # Output: [1]
# #
# # # 7.12
# # numbers = [1, 2, 3, 4, 5]
# # my_list = numbers[:]
# # print(my_list)  # Output: [1, 2, 3, 4, 5]
# #
# # # 7.13
# # numbers = [1, 2, 3, 4, 5]
# # my_list = numbers[-3:]
# # print(my_list)  # Output: [3, 4, 5]
#
# # 7.4 Finding items in list with the in operator
# # This program demonstrates the in operator
# # used with a list.
#
# # def main():
# #     # Create a list of product numbers.
# #     prod_nums = ['V475', 'F987', 'Q143', 'R688']
# #
# #     # Get a product number to search for.
# #     search = input('Enter a product number: ')
# #
# #     # Determine whether the product number is in the list.
# #     if search in prod_nums:
# #         print(f'{search} was found in the list.')
# #     else:
# #         print(f'{search} was not found in the list.')
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # 7.4 (Noninteractive) checkpoint questin from the book
# # # 7.14 What will the following code display?
# # names = ['Jim', 'Jill', 'John', 'Jasmine']
# # if 'Jasmine' not in names:
# #     print('Cannot find Jasmine.')
# # else:
# #     print("Jasmine's family:")
# #     print(names)
#
# # The append Method
# # This program demonstrates how the append
# # method can be used to add items to a list.
#
# # def main():
# #     # First, create an empty list.
# #     name_list = []
# #
# #     # Create a variable to control the loop.
# #     again = 'y'
# #
# #     # Add some names to the list.
# #     while again == 'y':
# #         # Get a name from the user.
# #         name = input('Enter a name: ')
# #
# #         # Append the name to the list.
# #         name_list.append(name)
# #
# #         # Add another one?
# #         print('Do you want to add another name?')
# #         again = input('y = yes, anything else = no: ')
# #         print()
# #
# #     # Display the names that were entered.
# #     print('Here are the names you entered.')
# #     for name in name_list:
# #         print(name)
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # The count Method
# names = ['Katrina', 'Kara', 'Zoya', 'Kara', 'Nettie', 'Kara']
# print(f'Kara appears {names.count("Kara")} times.')
#
#
# # The index Method
# # This program demonstrates how to get the
# # index of an item in a list and then replace
# # that item with a new item.
#
# # def main():
# #     # Create a list with some items.
# #     food = ['Pizza', 'Burgers', 'Chips']
#
#     # Display the list.
# #     print('Here are the items in the food list:')
# #     print(food)
# #     print()
# #
# #     # Get the item to change.
# #     item = input('Which item should I change? ')
# #
# #     try:
# #         # Get the item's index in the list.
# #         item_index = food.index(item)
# #
# #         # Get the value to replace it with.
# #         new_item = input('Enter the new value: ')
# #
# #         # Replace the old item with the new item.
# #         food[item_index] = new_item
# #
# #         # Display the list.
# #         print('Here is the revised list:')
# #         print(food)
# #     except ValueError:
# #         print('That item was not found in the list.')
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
#
# # The insert method
# # This program demonstrates the insert method.
#
# # def main():
# #     # Create a list with some names.
# #     names = ['James', 'Kathryn', 'Bill']
# #
# #     # Display the list.
# #     print('The list before the insert:')
# #     print(names)
# #
# #     # Insert a new name at element 0.
# #     names.insert(0, 'Joe')
# #
# #     # Display the list again.
# #     print('The list after the insert:')
# #     print(names)
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # The sort method
# my_list = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
# print('Original order:', my_list)
# my_list.sort()
# print('Sorted order:', my_list)
#
# my_list = ['beta', 'alpha', 'delta', 'gamma']
# print('Original order:', my_list)
# my_list.sort()
# print('Sorted order:', my_list)
#
# # The remove method
# # This program demonstrates how to use the remove
# # method to remove an item from a list.
#
# # def main():
# #     # Create a list with some items.
# #     food = ['Pizza', 'Burgers', 'Chips']
# #
# #     # Display the list.
# #     print('Here are the items in the food list:')
# #     print(food)
# #
# #     # Get the item to change.
# #     item = input('Which item should I remove? ')
# #
# #     try:
# #         # Remove the item.
# #         food.remove(item)
# #
# #         # Display the list.
# #         print('Here is the revised list:')
# #         print(food)
# #
# #     except ValueError:
# #         print('That item was not found in the list.')
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # The reverse method
# my_list = [1, 2, 3, 4, 5]
# print('Original order:', my_list)
# my_list.reverse()
# print('Reversed:', my_list)
#
# # The del statement
# my_list = [1, 2, 3, 4, 5]
# print('Before deletion:', my_list)
# del my_list[2]
# print('After deletion:', my_list)
#
# # The sum function
# my_list = [1, 2, 3, 4, 5]
# print(f'The sum is {sum(my_list)}.')
#
# # The min and max functions
# my_list =[5, 4, 3, 2, 50, 40, 39]
# print(f'The lowest value is {min(my_list)}.')
#
# my_list =[5, 4, 3, 2, 50, 40, 30]
# print(f'The highest value is {max(my_list)}.')
#
# # 7.5 (Noninteractive) checkpoint questions from the book
# #The remove method searches for the first occurrence of a specific value and removes it
# # from the list. If the value is not found, it raises a ValueError
# # 7.15 difference between remove and del
#
# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # Removes the first occurrence of 2
# print(my_list)  # Output: [1, 3, 2]
#
# # The del statement, on the other hand, removes an element based on its index position.
# # It does not search for a value.
#
# my_list = [1, 2, 3, 2]
# del my_list[1]  # Removes the element at index 1
# print(my_list)  # Output: [1, 3, 2]
#
# # 7.16 Finding the Lowest and Highest Values in a List
# # You can use the min() and max() functions to find the lowest and highest values, respectively.
#
# my_list = [5, 1, 8, 3]
# lowest = min(my_list)  # Output: 1
# highest = max(my_list)  # Output: 8
#
# #  Adding 'Wendy' to the List at Index 0
# # Option b, names.append('Wendy'), is the correct choice.
#
# # a. index: Finds the index of the first occurrence of a specified value in the list
# my_list = ['a', 'b', 'c']
# idx = my_list.index('b')  # Output: 1
#
# # b. insert: Inserts an element at a specific position in the list
# my_list = ['a', 'c']
# my_list.insert(1, 'b')  # Inserts 'b' at index 1
# print(my_list)  # Output: ['a', 'b', 'c']
#
# # c. sort: Sorts the elements of the list in ascending order by default. You can also use
# # reverse=True to sort in descending order.
# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3]
#
# # d. reverse: Reverses the order of the elements in the list
# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]
#
# # Totaling the values in a list
# # This program calculates the total of the values
# # in a list.
#
# # def main():
# #     # Create a list.
# #     numbers = [2, 4, 6, 8, 10]
# #
# #     # Create a variable to use as an accumulator.
# #     total = 0
# #
# #     # Calculate the total of the list elements.
# #     for value in numbers:
# #         total += value
# #
# #     # Display the total of the list elements.
# #     print(f'The total of the elements is {total}.')
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # Averaging the values in a list
# # This program calculates the average of the values
# # in a list.
# #
# # def main():
# #     # Create a list.
# #     scores = [2.5, 7.3, 6.5, 4.0, 5.2]
# #
# #     # Create a variable to use as an accumulator.
# #     total = 0.0
# #
# #     # Calculate the total of the list elements.
# #     for value in scores:
# #         total += value
# #
# #     # Calculate the average of the elements.
# #     average = total / len(scores)
# #
# #     # Display the total of the list elements.
# #     print(f'The average of the elements is {average}.')
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # Passing a list as an argument to a function
# # This program uses a function to calculate the
# # total of the values in a list.
#
# # def main():
# #     # Create a list.
# #     numbers = [2, 4, 6, 8, 10]
# #
# #     # Display the total of the list elements.
# #     print(f'The total is {get_total(numbers)}.')
# #
# #
# # # The get_total function accepts a list as an
# # # argument and returns the total of the values in
# # # the list.
# # def get_total(value_list):
# #     # Create a variable to use as an accumulator.
# #     total = 0
# #
# #     # Calculate the total of the list elements.
# #     for num in value_list:
# #         total += num
# #
# #     # Return the total.
# #     return total
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# # Returning a list from a function
# # This program uses a function to create a list.
# # The function returns a reference to the list.
#
# # def main():
# #     # Get a list with values stored in it.
# #     numbers = get_values()
# #
# #     # Display the values in the list.
# #     print('The numbers in the list are:')
# #     print(numbers)
#
#
# # The get_values function gets a series of numbers
# # from the user and stores them in a list. The
# # function returns a reference to the list.
# # def get_values():
# #     # Create an empty list.
# #     values = []
# #
# #     # Create a variable to control the loop.
# #     again = 'y'
# #
# #     # Get values from the user and add them to
# #     # the list.
# #     while again == 'y':
# #         # Get a number and add it to the list.
# #         num = int(input('Enter a number: '))
# #         values.append(num)
# #
# #         # Want to do this again?
# #         print('Do you want to add another number?')
# #         again = input('y = yes, anything else = no: ')
# #         print()
# #
# #     # Return the list.
# #     return values
# #
# #
# # # Call the main function.
# # if __name__ == '__main__':
# #     main()
#
# #
# # Defining a list of animal
#
#
# squares = [x**2 for x in range(10)]
# print("List of squares from 0 to 9:", squares)
#
#
#
#
for num in range(0, 20, 5):
    num += num
print(num)


#
#
#
#
#
#
#
#
#
#
#
#
