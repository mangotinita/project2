from collections.abc import ItemsView
from typing import Tuple

# # Variables Writing data to a file figure 6_1
# employee_name = "Cindy Chandler"
# employee_id = "7451Z"
# pay_rate = 18.65
#
# # Open a file in write mode
# with open("employee_data.txt", "w") as file:
#     # Write the data to the file
#     file.write(employee_name + "\n")
#     file.write(employee_id + "\n")
#     file.write(str(pay_rate) + "\n")
#
# print("Data has been written to employee_data.txt")
#
# # Writing data to a file
# # with open("example.txt", "w") as file:
# #     file.write("This is an example of writing to a file.\n")
# #     file.write("Python makes file I/O easy!")
# #
# # # Reading data from a file
# # with open("example.txt", "r") as file:
# #     content = file.read()
# #     print(content)
# #
# # # Appending data to a file
# # with open("example.txt", "a") as file:
# #     file.write("\nThis is appended text.")
# #
# # # Appending data to a file
# # with open("example.txt", "a") as file:
# #     file.write("\nThis is appended text.")
# # 'r' : Read (default)
# # 'w' : Write (overwrites file)
# # 'a' : Append
# # 'r+': Read and Write
# #
# # with open("example.txt", "r") as file:
# #     for line in file:
# #         print(line.strip())  # strip() removes the extra newline character
#
#
# # 1. Text Files
# # .txt – Plain text file
# # .csv – Comma-separated values (used for spreadsheet or database data)
# # .log – Log file (usually for recording events in plain text)
# # .md – Markdown file (plain text format that supports simple formatting)
# # 2. Document Files
# # .doc / .docx – Microsoft Word document
# # .pdf – Portable Document Format (readable across devices)
# # .odt – OpenDocument Text file (used in LibreOffice, OpenOffice)
# # .rtf – Rich Text Format (supports some formatting)
# # 3. Image Files
# # .jpg / .jpeg – Joint Photographic Experts Group (compressed image)
# # .png – Portable Network Graphics (lossless image format)
# # .gif – Graphics Interchange Format (supports animation)
# # .bmp – Bitmap image file
# # .svg – Scalable Vector Graphics
# # 4. Audio Files
# # .mp3 – MPEG-1 Audio Layer 3 (compressed audio)
# # .wav – Waveform Audio File (uncompressed audio)
# # .aac – Advanced Audio Coding (compressed audio, often used in iTunes)
# # .flac – Free Lossless Audio Codec
# # 5. Video Files
# # .mp4 – MPEG-4 video file (common for online videos)
# # .avi – Audio Video Interleave (an older video format)
# # .mkv – Matroska Video File (supports multiple audio/subtitle tracks)
# # .mov – Apple QuickTime Movie
# # 6. Compressed Files
# # .zip – ZIP compressed file
# # .rar – RAR compressed file
# # .tar – Tarball file (often used in Linux)
# # .gz – Gzip compressed file (often used with .tar files, like .tar.gz)
# # 7. Executable Files
# # .exe – Executable file (used to run programs in Windows)
# # .bat – Batch file (used to automate tasks in Windows)
# # .sh – Shell script (used to automate tasks in Unix/Linux)
# # .msi – Windows installer package
# # 8. Programming Files
# # Python: .py – Python script
# # Java: .java – Java source code
# # C/C++: .c / .cpp – C/C++ source code
# # HTML: .html – HyperText Markup Language file (web page)
# # CSS: .css – Cascading Style Sheets (used for web design)
# # JavaScript: .js – JavaScript file (used in web development)
# # 9. Database Files
# # .sql – SQL file (Structured Query Language used for databases)
# # .db / .sqlite – SQLite database file
# # .mdb / .accdb – Microsoft Access database file
# # .xml – Extensible Markup Language (often used for structured data)
# # 10. System Files
# # .dll – Dynamic Link Library (Windows system file)
# # .sys – System file (used by the operating system)
# # .ini – Initialization file (used to configure settings)
# # 11. Web Files
# # .html / .htm – Hypertext Markup Language (used for web pages)
# # .css – Cascading Style Sheets (defines the layout of web pages)
# # .js – JavaScript file (used to add interactivity to web pages)
# # .php – PHP Hypertext Preprocessor (used for server-side scripting)
# # .asp – Active Server Page (used for dynamic web pages)
# # 12. Miscellaneous Files
# # .json – JavaScript Object Notation (used for structured data)
# # .yaml / .yml – YAML Ain't Markup Language (configuration files)
# # .psd – Photoshop Document (Adobe Photoshop file)
# # .ppt / .pptx – PowerPoint Presentation (Microsoft PowerPoint)
# # .xls / .xlsx – Microsoft Excel Spreadsheet
#
# # Methods
#
# # Sequential
# # Reading a File Sequentially Line by Line
#
# # Example: Reading a file sequentially
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Processes each line in sequence
#
# # Reading the Entire File Sequentially
#
#
# # Example: Reading the entire file
# with open("example.txt", "r") as file:
#     data = file.read()  # Reads the entire content at once, still sequentially
#     print(data)
#
# # Writing to a File Sequentially
#
# # Example: Writing to a file sequentially
# with open("output.txt", "w") as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n")
#     file.write("This is the third line.\n")
#
# # Appending Data Sequentially
# # Example: Appending to a file sequentially
# with open("output.txt", "a") as file:
#     file.write("This line is appended at the end.\n")
#
# # Reading a File in Chunks (Sequentially)
# # Example: Reading a file in chunks sequentially
# with open("largefile.txt", "r") as file:
#     chunk_size = 1024  # Read 1 KB at a time
#     while True:
#         chunk = file.read(chunk_size)
#         if not chunk:
#             break
#         print(chunk)


# Change a Range of Item Values
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# Change the second and third value by replacing it with one value:

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
#
# # Insert Items
# # Insert "watermelon" as the third item:
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# Python - Add List Items
# Using the append() method to append an item:

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# Extend List
# Add the elements of tropical to thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# Python - Remove List Items

# Remove "banana":

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
#
# Remove the first occurrence of "banana":

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
#
# Example
# Remove the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
#
# Remove the last item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# Clear the list content:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# Python - Loop Lists
# Loop Through a List
#
# Print all items in the list, one by one:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
#
# Loop Through the Index Numbers
#
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# Using a While Loop
# print all items, using a while loop to go through all the index numbers

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# Looping Using List Comprehension
# A short hand for loop that will print all items in a list:
#
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)
#
# Python - Sort Lists
# Sort List Alphanumerically
# Sort the list alphabetically:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# Sort the list numerically:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# Sort the list descending:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# Case sensitive sorting can give an unexpected result:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.sort()
# # print(thislist)

# Perform a case-insensitive sort of the list:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# Make a copy of a list with the copy() method:

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# Make a copy of a list with the list() method:

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# Make a copy of a list with the : operator:

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# Python - Join Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

# Join two list:

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# Append list2 into list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# Use the extend() method to add list2 at the end of list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# Python Tuple

# Create a Tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Tuples allow duplicate values:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Print the number of items in the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# thistuple = ("apple",)
# print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# String, int and boolean data types:

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# print(tuple1)
# print(tuple2)
# print(tuple3)

# A tuple with strings, integers and boolean values:

# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)

# What is the data type of a tuple?

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# The tuple() Constructor
# Using the tuple() method to make a tuple:

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Python - Access Tuple Items
# Access Tuple Items
# Print the second item in the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# Negative Indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# Range of Indexes

# Return the third, fourth, and fifth item:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Check if "apple" is present in the tuple:

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
# print("Yes, 'apple' is in the fruits tuple")

# Python - Update  Tuples
# Convert  the  tuple  into  a  list  to  be  able  to  change  it:

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)

# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
