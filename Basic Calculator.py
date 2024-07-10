#Creating functions for basic operators
def add(a, b):
    answer = a+b
    print(str(a)+" + "+str(b)+" = "+answer)
    
def subtract(a,b):
    answer = a-b
    print(str(a)+" - "+str(b)+" = "+answer)
    
def multiply(a,b):
    answer = a*b
    print(str(a)+" * "+str(b)+" = "+answer)
    
def divide(a,b):
    answer = a/b
    print(str(a)+" / "+str(b)+" = "+answer)
    
#Inserting the calculator into loop
while True:
        #Asking input from the user and calling the functions
        print('')
        print("Add/Subtract/Multiply/Divide/Exit")
        print('')

        User_Input = input("Enter any one of the operations above to perform: ")
        if User_Input.lower() == 'exit':
            print("😎Bye Thanks")
            break
        
        
        print('')
        First_no = int(input("Enter the first number: "))
        Second_no = int(input("Enter the second number: "))
        print("")

        if User_Input.capitalize() == "Add":
            print("The answer is:")
            print("")
            add(First_no, Second_no)
        
        elif User_Input.capitalize() == "Subtract":
            print("The answer is:")
            print("")
            subtract(First_no,Second_no)
        
        elif User_Input.capitalize() == "Multiply":
            print("The answer is:")
            print("")
            multiply(First_no,Second_no)
            
        elif User_Input.capitalize() == "Divide":
            print("The answer is:")
            print("")
            divide(First_no,Second_no) 
            
        else:
            print("🤞😎Bye Thanks!Invalid operation to perform")
            