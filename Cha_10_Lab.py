# Program to simulate car acceleration and braking
# Author: Mauricio Arriaga
# Date: 10/30/2024

class Car:
    def __init__(self, year_model, make, speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed  # Initialize with user-provided speed or default to 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0  # Prevents speed from going below 0

    def get_speed(self):
        return self.__speed


def main():
    # Create a Car object with user input for the year model, make, and initial speed
    year_model = input("Enter the car's year model: ")
    make = input("Enter the car's make: ")
    try:
        speed = int(input("Enter the car's current speed: "))  # Get the initial speed from the user
    except ValueError:
        speed = 0
        print("Invalid input. Speed set to 0.")

    car = Car(year_model, make, speed)

    # Accelerate the car 5 times
    print("\nAccelerating the car:")
    for _ in range(5):
        car.accelerate()
        print("Current speed:", car.get_speed())

    # Brake the car 5 times
    print("\nBraking the car:")
    for _ in range(5):
        car.brake()
        print("Current speed:", car.get_speed())


if __name__ == "__main__":
    main()
