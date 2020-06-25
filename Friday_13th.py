#Given the month and year as numbers, return whether that month contains a Friday 13th

import datetime #Python library to work with dates

#ask the user for a month and convert it to type int
user_month = input('Give me a month (from 1-12): ') 
month = int(user_month)

#ask user for a year and convert it to type int
user_year = input('Give me a year YYYY: ')
year = int(user_year)

#set the day to the 13th as we're looking for that date.
day = 13

#define variable date with specific format of year, month and day
date = datetime.datetime(year, month, day)

#format the variable date to look at the day only (short version)
day = date.strftime('%A')

#function to check if a given month in a given year had a Friday.
def isFriday(month, year): 
    if date.strftime('%a') == 'Fri': #checking if there was a Friday on the 13th.
        print('yes, watch out!')
        return True
    else:
        print('nope, you\'re lucky.')
        return False

#call the function
print(isFriday(user_month, user_year))