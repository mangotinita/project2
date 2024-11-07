# Function header: first line of function

# Block: set of statements that belong together as a group

# main function: called when the program starts

# Hierarchy chart: depicts relationship between functions

# Designing a program Figure 5-10

# Main function that controls the flow of the program
# def main():
#     hours_worked = get_hours_worked()
#     hourly_rate = get_hourly_rate()
#
#     gross_pay = calc_gross_pay(hours_worked, hourly_rate)
#     overtime_pay = calc_overtime(hours_worked, hourly_rate)
#
#     taxes = calc_taxes(gross_pay)
#     benefits = calc_benefits(gross_pay)
#     withholdings = calc_withholdings(taxes, benefits)
#
#     net_pay = calc_net_pay(gross_pay, overtime_pay, withholdings)
#
#     print(f"Gross Pay: ${gross_pay:.2f}")
#     print(f"Overtime Pay: ${overtime_pay:.2f}")
#     print(f"Taxes: ${taxes:.2f}")
#     print(f"Benefits: ${benefits:.2f}")
#     print(f"Total Withholdings: ${withholdings:.2f}")
#     print(f"Net Pay: ${net_pay:.2f}")
#
#
# # Function to get input for hours worked
# def get_hours_worked():
#     return float(input("Enter the number of hours worked: "))
#
#
# # Function to get input for hourly rate
# def get_hourly_rate():
#     return float(input("Enter your hourly rate: "))
#
#
# # Function to calculate gross pay
# def calc_gross_pay(hours_worked, hourly_rate):
#     return hours_worked * hourly_rate


# Function to calculate overtime pay
# def calc_overtime(hours_worked, hourly_rate):
#     overtime_hours = max(0, hours_worked - 40)  # Overtime only if more than 40 hours worked
#     return overtime_hours * hourly_rate * 1.5  # Assuming 1.5x pay for overtime
#
#
# # Function to calculate taxes
# def calc_taxes(gross_pay):
#     tax_rate = 0.2  # Example: 20% tax rate
#     return gross_pay * tax_rate
#
#
# # Function to calculate benefits
# def calc_benefits(gross_pay):
#     benefit_rate = 0.05  # Example: 5% benefits deduction
#     return gross_pay * benefit_rate
#
#
# # Function to calculate total withholdings (taxes + benefits)
# def calc_withholdings(taxes, benefits):
#     return taxes + benefits
#
#
# # Function to calculate net pay
# def calc_net_pay(gross_pay, overtime_pay, withholdings):
#     return gross_pay + overtime_pay - withholdings
#
#
# # Run the program
# if __name__ == "__main__":
#     main()

# Passing Arguments to Function

# Main function
# def main():
#     value = 5
#     show_double(value)
#
# # Function to double the number and display the result
# def show_double(number):
#     result = number * 2
#     print(result)
#
# # Run the program
# if __name__ == "__main__":
#     main()

# Passing multiple arguments figure 5-6

# Main function
# def main():
#     print('The sum of 12 and 45 is')
#     show_sum(12, 45)
#
# # Function to calculate and display the sum of two numbers
# def show_sum(num1, num2):
#     result = num1 + num2
#     print(result)
#
# # Run the program
# if __name__ == "__main__":
#     main()

# Making changes to Parameters figure 5-18

# Main function
# def main():
#     value = 99
#     print(f'The value is {value}.')
#     change_me(value)
#     print(f'Back in main the value is {value}.')
#
# # Function to demonstrate changing the value of a parameter
# def change_me(arg):
#     print('I am changing the value.')
#     arg = 0
#     print(f'Now the value is {arg}.')
#
# # Run the program
# if __name__ == "__main__":
#     main()

# Keyword-only parameters slice 31
#
# def example_function(a, b, *, c, d):
#     return f"a={a}, b={b}, c={c}, d={d}"
#
# # Correct usage with keyword-only arguments
# print(example_function(1, 2, c=3, d=4))
#
# # Incorrect usage: passing keyword-only arguments by position raises an error
# # print(example_function(1, 2, 3, 4))  # This would raise a TypeError
#
# def calculate_price(base_price, quantity, *, tax=0.05, discount=0.0):
#     """
#     Calculate the total price of items with optional tax and discount.
#
#     Parameters:
#     - base_price: The price of a single item (positional argument)
#     - quantity: The number of items (positional argument)
#     - tax: The tax rate as a decimal (keyword-only argument)
#     - discount: The discount rate as a decimal (keyword-only argument)
#
#     Returns:
#     The total price after applying tax and discount.
#     """
#     subtotal = base_price * quantity
#     taxed_price = subtotal + (subtotal * tax)
#     discounted_price = taxed_price - (taxed_price * discount)
#
#     return round(discounted_price, 2)


# Example usage:
# Correct usage with keyword arguments for tax and discount
print(calculate_price(100, 2, tax=0.07, discount=0.1))  # Output: 189.0

# Using default values for tax and discount
print(calculate_price(100, 2))  # Output: 210.0

# Incorrect usage: Trying to pass tax and discount by position (raises TypeError)
# print(calculate_price(100, 2, 0.07, 0.1))  # This would raise a TypeError

# Function with multiple default arguments

# def calculate_total(price, quantity=1, tax=0.05):
#     total = price * quantity * (1 + tax)
#     return round(total, 2)
#
# # Using default values for quantity and tax
# print(calculate_total(100))  # Output: 105.0
#
# # Specifying quantity but using default tax
# print(calculate_total(100, quantity=3))  # Output: 315.0
#
# # Specifying both quantity and tax
# print(calculate_total(100, quantity=3, tax=0.1))  # Output: 330.0

Usin IPO Charts

# def get_regular_price():
#     price = float(input("Enter the item's regular price: "))
#     return price
# # Define the discount percentage as a global constant
# DISCOUNT_PERCENTAGE = 0.10
#
# def discount(price):
#     discount_amount = price * DISCOUNT_PERCENTAGE
#     return discount_amount
# # Get the regular price
# regular_price = get_regular_price()
#
# # Calculate the discount
# discount_amount = discount(regular_price)
#
# # Display the discount
# print(f"The discount amount is: ${discount_amount:.2f}")

# Returning strings





