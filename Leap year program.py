input_year = int(input("Enter a year:"))
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
    
import calendar

if calendar.isleap(input_year):
    print("It is a leap year")
else:
    print("It is not a leap year")

