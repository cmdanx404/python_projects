# Project No.14
# Max of Three

def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    return n2

def max_of_three(n1, n2, n3):
    max_two = max_of_two(n1, n2)
    final_max = max_of_two(max_two, n3)
    return final_max

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Call the function and print the result
print("The maximum number is:", max_of_three(num1, num2, num3))

