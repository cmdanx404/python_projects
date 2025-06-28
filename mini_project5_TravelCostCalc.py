#Trip Cost Calculator

# Greeting
print("Welcome to the Trip Cost Calculator!\n")

#variables
stay_duration = input("How many days will you stay? ")
cost_per_night = input("How much does hotel cost per night? $")
flight_cost = input("How much does flight cost? $")
car_rental = input("If you need rental car please enter the price otherwise enter zero. $")
other_expenses = input("Enter other possible expenses $")

# casting
stay_duration = int(stay_duration)
cost_per_night = float(cost_per_night)
flight_cost = float(flight_cost)
car_rental = float(car_rental)
other_expenses = float(other_expenses)

# total expenses
total_expenses = round(stay_duration * cost_per_night + flight_cost + stay_duration * car_rental + other_expenses, 2)
print(f"Total Expenses: ${total_expenses}")


