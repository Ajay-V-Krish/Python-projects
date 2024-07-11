def word_dictionary():
    Dictionary = {
        "hi":"The Way of greeting.",
        "bus":"A vehicle for transport.",
        "book":"A bunch of papers that have content in it.",
        "cricket":"A game that have batsman,bowlers and fielders."
    }
    
    
    while True:
        User_Word = input("Enter a word to know its meaning: ")
        if User_Word == '':
            break
        elif User_Word in Dictionary:
            print(User_Word,":",Dictionary[User_Word])
            print('')
        else:
            print("Sorry, The word is not in dictionary")
        
        Next_Input = input("Press (y) to continue (x) to exit: ") 
        
        if Next_Input.lower() != 'y':
            break
        else:
            print("Thanks")
            continue
        
            
word_dictionary()

#To have more words we have to install pydictionary
            