def EmailSlicer():
    
    print("--Welcome to the E-mail slicer--")
    print('')

    User_input = input("Enter your email: ")

    email_list= User_input.split('@')
    domain = email_list[1]
    domain_list = domain.split('.')

    print("User_Name: "+ email_list[0])
    print("E-mail Domain: "+domain_list[0])
    print("Extension: "+domain_list[1])
    
while True:
    EmailSlicer()
    
    Next_Input = input("If you want to continue press (y) or press (n): ")
    
    if Next_Input.lower() != 'y':
        print("😎Bye Thanks")
        break
    
    else:
        continue