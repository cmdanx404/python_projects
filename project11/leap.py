def leap_year(year_input):
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                return "Leap year"
            else:
                return "Not Leap year"
        else:
            return "Leap year"
    else:
        return "Not leap year"       
