def is_leap_year(year):
    if year % 400 == 0 or year %100 != 0 and year % 4 == 0:
        return f"{year} is Leap Year"
    return f"{year} is not a leap year"


print(is_leap_year(2024))