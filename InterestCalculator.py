print('')
print("---Interst Payment Calculator---")
print('')

def Interst_Calculator(a,b,c):
    interest_per_year = (b/100)*a
    interest_for_c_years = interest_per_year*c
    print('')
    print("The total intrest to be paid for",c,"year(s) is:$",interest_for_c_years)
    print('')
    interest_monthly = interest_for_c_years/(12*c)
    print("The monthly interest to be paid is:$",interest_monthly)
    # amount_of_months = c*12
    # payment_monthly = a*interest_monthly/(1-(1+interest_monthly)**(-amount_of_months))
    # print("The monthly payment is:$",payment_monthly)

while True:
    
    Principal_Amount = float(input("Enter the principal amount(in numbers):$"))
    print('')
    r_P_A = float(input("Enter the rate per annum(in percentage):"))
    print('')
    Years = int(input("Enter the number of year(s):"))


    Interst_Calculator(Principal_Amount,r_P_A,Years)
    
    print('')
    Next_Input = input("Press (y) to continue or (n) to exit:")
    print('')
    
    if Next_Input.lower() != 'y':
        print("😉😉😉Thanks")
        break
    
    else:
        continue