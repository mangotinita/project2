def main():

    def calculate_average(filename):
        # This function calculates the average of the numbers in a file
        # and returns the average.
        # Open the file for reading.
        try:
            # Open the file for reading.
            with open(filename, 'r') as file:
                # Initialize an accumulator to 0.0.
                total = 0.0
                # Initialize a variable to keep track of the number of lines in the file.
                count = 0
                # Read the values from the file and accumulate them.
                for line in file:
                    try:
                        number = float(line)
                        total += number
                        count += 1
                    except ValueError:
                        print(f"Non-numeric data found in the file {filename}.")

            # If at least one number was read, calculate the average.
            if count > 0:
                return total / count
            else:
                return None

        except IOError:
            print(f"An error occurred while trying to open or read the file {filename}.")
            return None
    # process the file number.txt

    average1 = calculate_average('numbers.txt')
    if average1 is not None:
        print(f"The average of the file numbers.txt is {average1}.")
    else:
        print("The average of numbers.txt could not be calculated")

    # Process the file numbers1.txt
    average2 = calculate_average('numbers1.txt')
    if average2 is not None:
        print(f"Average of the file numbers1.txt: {average2}")
    else:
        print("The average of numbers1.txt could not be calculated")

    # If both averages were calculated, calculate the combined average
    if average1 is not None and average2 is not None:
        combined_average = (average1 + average2) / 2
        print(f"Combined average of both files: {combined_average}")
    else:
        print("The combined average could not be calculated due to an error.")

# Call the main function
if __name__ == '__main__':
    main()