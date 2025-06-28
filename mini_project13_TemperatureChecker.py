# Project No. 13
# Temperature Checker using Function

def check_temp(temp):
    if temp > 28:
        return "Hot"
    elif temp >= 18 and temp <= 28:
        return "Warm"
    else:
        return "Cold"

temp = int(input("Enter temperature: "))
print(check_temp(temp))