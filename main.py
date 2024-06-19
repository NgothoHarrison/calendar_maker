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
    
    print("Please enter a numeric year")
    continue

while True:
    response = input("Enter the month : ")

    if not response.isdecimal():
        print("Enter a numeric month: ")
        continue
    
    month = int(response)
    if 1<= month <= 12:
        break
    
    print("Enter a month between 1 and 12")
    