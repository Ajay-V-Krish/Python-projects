print("-----Word Replacement-----\n")

while True:
    def word_replacement():
        
        base_str = "Hello. This is Phython. The easiest programming language."
        print(base_str)
        Befor_replace = input("Enter the word to be raplaced: \n")
        Replaced_word = input("Enter the word after replacement: \n")
        
        print(base_str.replace(Befor_replace, Replaced_word))
        

    word_replacement()
    
    User_Input = input("If you want to continue make changes press (y) or press (n): ")
    
    if User_Input.lower() != 'y':
        print("\nYou have ended making changes")
        break
    else: 
        continue   