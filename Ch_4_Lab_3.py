
# Lab #3

tuition = float(input('how much is full-time student tuition:'))
increase_rate = float(input('what is  the percentage of increase (e.g., 0.03 for 3%): '))
years = int(input('how many years does the tuition have been paid? : '))

for year in range(1, years + 1):
    tuition = tuition + (tuition * increase_rate)
    print(f"Year {year}: New tuition cost = {int(tuition):}")
