# The while Loop: a condition-Controlled Loop Figure 4-1
# # Initialize a variable (example)
# condition = True
#
# # While loop
# while condition:
#     # Statements to execute
#     print("Condition is True, executing statements...")
#
#     # Update condition to eventually exit the loop (for example purposes, we set it to False after one iteration)
#     condition = False
#
# print("Exited the loop, condition is now False.")

# condition = True
# while condition:
#     print ("This loop will continue until condition becomes False.")
#     user_input = input("Do you want to stop the loop? (yes/no): ")
#     if user_input.lower() == "yes":
#         condition = False




# Figure 4-3 Flowchart for Program 4-1
# Commission calculation program
#
# keep_going = 'y'  # Initial value to start the loop
#
# while keep_going == 'y':  # Loop continues as long as the user inputs 'y'
#     Prompt the user to enter the sales amount and commission rate
#     sales = float(input("Enter the amount of sales: "))
#     comm_rate = float(input("Enter the commission rate (as a decimal): "))
#
#     Calculate the commission
#     commission = sales * comm_rate
#
#     Display the commission
#     print(f"The commission is: ${commission:.2f}")
#
#     Ask if the user wants to calculate another commission
#     keep_going = input("Do you want to calculate another commission? (Enter 'y' for yes): ").lower()

#print("End of the commission calculator program.")

# Figure 4-6 Logic for calculating a running total
#  set accumulator to 0
#  accumulator  = 5

#
# numbers = input(" its a another number to read? ( yes / no ) ").lower()
#
#
# while numbers == 'yes':
#     next_number = float(input("Enter the next number: "))
#     accumulator += next_number
#     numbers = input(" its a another number to read? ( yes / no ) ").lower()
#
# print(f"The accumulator is: ${accumulator:.2f}")

# Figure 4-7 Logic containing an input validation loop

# get_input = input("are you human:  write y for 'yes' or n for 'no'").lower()
#
# while get_input != 'y':
#     print('print no are human')
#     get_input = input("are you human:  write y for 'yes' or n for 'no'").lower()
#     if get_input == 'y':
#         print('keep going ')

# figure 4-8 flowchart for a clock simulator (wrong)

# hour_list = [1, 2, 3, ]
# minute_list = [0, 15, 30, 45]
# second_list = [0, 10, 20, 30, 40,50]
#
# hour_index = 0
#
# while hour_index < len(hour_list):
#     hour_list = hour_list[hour_index]
#
#     minute_index = 0
#     while minute_index < len(minute_list):
#         minute_list = minute_list[minute_index]
#         second_index = 0
#         while second_index < len(second_list):
#             second_list = second_list[second_index]
#             print(hour_value, ":", minute_value, ":", second_value)
#             second_list += 1
#         minute_index += 1
#     hour_index += 1
# figure 4-8 flowchart for a clock simulator

# hour_list = [1, 2, 3]
# minute_list = [0, 15, 30, 45]
# second_list = [0, 10, 20, 30, 40, 50]
#
# hour_index = 0
#
# while hour_index < len(hour_list):
#     hour_value = hour_list[hour_index]  # Keep the list intact, assign individual values to new variables
#
#     minute_index = 0
#     while minute_index < len(minute_list):
#         minute_value = minute_list[minute_index]  # Use a different variable to store the minute
#
#         second_index = 0
#         while second_index < len(second_list):
#             second_value = second_list[second_index]  # Use a different variable to store the second
#
#             print(hour_value, ":", minute_value, ":", second_value)
#             second_index += 1
#
#         minute_index += 1
#
#     hour_index += 1

# Single-Line while Loops (single_line_while.py)
#
# n = 0
# while n < 10: n += 1
# print(f'After the loop, n is {n}.')

# Pseudocode for lab-3

# Start

# # Input the initial tuition cost
# print("Enter the full-time student tuition amount: ")
# tuition = input()  # Get input from user and store it in tuition
#
# # Input the percentage of increase (as a decimal)
# print("Enter the percentage of increase as a decimal (e.g., 0.03 for 3%): ")
# increase_rate = input()  # Get input from user and store it in increase_rate
#
# # Input the number of years for the tuition projection
# print("Enter the number of years for tuition projection: ")
# years = input()  # Get input from user and store it in years
#
# # Convert input values from string to float/int
# tuition = float(tuition)
# increase_rate = float(increase_rate)
# years = int(years)

# Display header for output
# print("Year  |  New Tuition Cost")

# tuition = 8487 * 0.3
# Loop through each year and calculate the new tuition
# for year in range(1, years + 1):
    # Increase the tuition by the percentage rate
    # tuition = tuition + (tuition * increase_rate)

    # Display the new tuition for the current year
    # print(f"Year {year}: New tuition cost = {tuition:.2f}")

# End


# tuition = float(input('how much is full-time student tuition:'))
# increase_rate = float(input('what is  the percentage of increase (e.g., 0.03 for 3%): '))
# years = int(input('how many years does the tuition have been paid? : '))
#
#
# for year in range(1, years + 1):
#     tuition = tuition + (tuition * increase_rate)
#     print(f"Year {year}: New tuition cost = {tuition:.2f}")










