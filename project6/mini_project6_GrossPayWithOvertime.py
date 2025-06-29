# Project No.6
# Gross Paty with overtime

hour = float(input("Enter hour: "))
rate = float(input("Enter rate: "))
overtime = hour - 40

if hour > 40:
    pay = (rate * 40.0) + (1.5 * rate * overtime)
else:
    pay = (hour * rate)

print(f"Pay: {pay}")