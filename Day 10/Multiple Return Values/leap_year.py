# Check for Leap Year
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

entered_year = int(input("Enter a year: "))
print(is_leap_year(entered_year))