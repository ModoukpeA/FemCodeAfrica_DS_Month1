"""
This function will read a given number from the user and then
will display it in terms of weeks and days
E.g: 10; This is 1 week and 3 days.
"""
while True:
    numberofdays = int(input("Enter a number : \n"))

    if numberofdays > 0:
        weeks = numberofdays // 7
        days = numberofdays % 7
        print("This is equivalent to {} week(s) and {} day(s).".format(weeks,days))
    else:
        print('You should enter a valid number of days!')