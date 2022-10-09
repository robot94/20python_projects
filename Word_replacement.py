# Word replacement programme 

def wordreplace():
    
    message = 'Hello Youssef, Thank you for enroling in this Cloud course as well as powershell mastery course'
    word_to_replace = input("Please enter the word that you want to replace: ")
    word_replacement = input("Please enter the word replacement: ")
    
    print(message.replace(word_to_replace, word_replacement))

wordreplace()
