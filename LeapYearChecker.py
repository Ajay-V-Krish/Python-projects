def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('The entered year is leap year.')
            else:
                print('The entered year is not a leap year.')
        else:
            print('The enterd year is a leap year.')
    else:
        print('The enterd year is not a leap year.')



while True:
    Input_Year = int(input('Enter a year to check whether it is a leap year or not: '))
    if type(Input_Year) == int:
        leap_year(Input_Year)
    else:
        print('Enter a valid year')

    Next_Input = input("If you want to continue press (y) or press (n): ")

    if Next_Input.lower() != 'y':
        break
    else:
        continue