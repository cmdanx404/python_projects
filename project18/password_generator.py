# Password Generator

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "-+=!@#$%^&*"

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your password? "))
number_of_symbols = int(input("How many symbols do you want in your password? "))

password = ""

for _ in range(number_of_letters):
    password += random.choice(letters)

for _ in range(number_of_numbers):
    password += random.choice(numbers)

for _ in range(number_of_symbols):
    password += random.choice(symbols)

print(f"Your password is: {password}")

password_list = list(password)
random.shuffle(password_list)

advanced_password = ""
for char in password_list:
    advanced_password += char

print(f"Your advanced password is: {advanced_password}")
