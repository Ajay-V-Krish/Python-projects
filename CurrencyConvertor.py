print('')
print("This program prints Dollars($) into Rupees(Rs)")
print('')

def currency_covertor(Currency_To_Be_Converted):
    Converted_Currency = Currency_To_Be_Converted*83.58
    return Converted_Currency

User_Input = eval(input("Enter the amount in dollars($):$ "))
 
Rupees = currency_covertor(User_Input)

print("The Currency in Rupees is:₹",Rupees)
print('')
    
    
    