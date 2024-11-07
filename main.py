from emp import Employee, ProductionWorker

from emp import ProductionWorker

def main():
    # Get user input for employee information
    name = input("Enter employee name: ")
    emp_number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number (1 for morning, 2 for evening, 3 for overnight): "))
    hourly_rate = float(input("Enter hourly pay rate: "))

    # Adjust hourly rate based on shift
    if shift_number == 2:
        hourly_rate += 0.50
    elif shift_number == 3:
        hourly_rate += 1.00

    # Create a ProductionWorker instance
    worker = ProductionWorker(name, emp_number, shift_number, hourly_rate)

    # Display the employee information
    print("\nEmployee Information")
    print(f"Name: {worker.get_name()}")
    print(f"ID: {worker.get_emp_number()}")
    print(f"Shift: {worker.get_shift_number()}")
    print(f"Hourly Rate: ${worker.get_hourly_pay_rate():.2f}")

if __name__ == "__main__":
    main()