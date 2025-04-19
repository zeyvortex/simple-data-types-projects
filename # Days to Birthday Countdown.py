# Days to Birthday Countdown

import datetime

today = datetime.date.today()

birth_month = int(input("enter your birth month (1-12): "))
birth_day = int(input("enter your birth day (1-31): "))

this_year_birthday = datetime.date(today.year , birth_month , birth_day)

if this_year_birthday < today:
    next_birthday = datetime.date(today.year + 1 , birth_month , birth_day)
else:
    next_birthday = this_year_birthday

days_left = (next_birthday - today).days

print("your birthday is in" , days_left , "days!")