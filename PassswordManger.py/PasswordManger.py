Main_Pwsd = input("Enter your main password:")

def view():
    with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                print(line.strip())

def add():
    Account_Name = input("Account name:")
    Pwd = input("Enter password:")
    
    with open('passwords.txt', 'a') as f:
        f.write("Name:"+Account_Name+"| Password:"+Pwd+'\n')


while True:
    User_Input = input("To create new password press add(a)/To view the existing ones press view(v)/To quit press (q):")
    
    if User_Input.lower() == 'q':
        break
    
    if User_Input.lower() == 'a':
        add()
    elif User_Input.lower() == 'v':
        view()
    else:
        print('')
        print('Inavlid Input')

