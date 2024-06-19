import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

print("Calender by Hank")

while True:
    response = input(print("Enter the year for the calender: "))

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Please enter a numeric year")
    continue

while True:
    response = input("Enter the month : ")

    if not response.isdecimal():
        print("Enter a numeric Month")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("Please enter a number 1 - 12")


def getcalendar(year, month):
    calText = ''

    # enter text on top of the calendar

    calText += ('' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    calText += '...Sunday....Monday....Tuesday....Wednesday....Thursday...Friday...Saturday...\n'

    weekSeparator = ('+-----------' * 7) + '\n'

    blankRow = ('|        ' * 7) + '\n'

    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '  |' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += ' | \n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText


calText = getcalendar(year, month)
print(calText)

# save to a txt file
calendarFilename = 'calender_{}_{}.txt'.format(year, month)

with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('saved to ' + calendarFilename)
