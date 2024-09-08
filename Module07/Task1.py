number_of_month = int(input("Enter the number of a month: "))

seasons = "Spring", "Summer", "Fall", "Winter"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_selection = months[number_of_month - 1]

if number_of_month < 1 or number_of_month > 12:
    print("Number of month not in range. ")

elif number_of_month == 12 or number_of_month == 1 or number_of_month == 2: # December, January or February
    print(f'The month {month_selection} is during the {seasons[3]} season. ') # Winter

elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5: # March, April or May
    print(f'The month {month_selection} is during the {seasons[0]} season. ') # Spring

elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8: # June, July or August
    print(f'The month {month_selection} is during the {seasons[1]} season. ') # Summer

elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11: # September, October or November
    print(f'The month {month_selection} is during the {seasons[2]} season. ') # Fall

