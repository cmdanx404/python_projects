# Project No. 4
# Celsius to Fahrenheit

print("Welcome to Celsius to Fahrenheit Converter!\n")

celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = round((celsius * 9/5 + 32),1)

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")