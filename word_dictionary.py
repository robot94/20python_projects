#Word dictionary programme

#from PyDictionary import PyDictionary

def dictioanry():
    
    word_dictionary = {
        'hi' : 'A way of greating',
        'eyes' : 'Organ for seaing',
        'earth': 'A planet in the space'
    }
    
    
    
    while True:
        
        user_input = input("Please enter a word to check: ").lower()
        if user_input in word_dictionary:
        
            print(user_input , ":", word_dictionary[user_input] )
        
        else:
            print("Sorry the word dos not exist in the dictioanry: ")
            break

dictioanry()