#Gross Pay

#variables
hour = input(("Enter Hours: "))
rate = input(("Enter Rate: "))

#casting
hour = float(hour)
rate = float(rate)
pay = round(hour * rate, 2)
print (f"Pay: {pay}")

