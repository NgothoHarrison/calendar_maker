import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

print("Calender by Hank")

while True:
    response = input(print("Enter the year for the calendar: "))

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break