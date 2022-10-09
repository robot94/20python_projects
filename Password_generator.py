#Welcome to the Password Generator Programme
import string
import random
#Requesting the user input for the password Length and complexity

password_length = int(input("Please enter your password Length: "))

password_pool = list(string.ascii_uppercase + string.ascii_lowercase + string.punctuation)
random.shuffle(password_pool)

password = []

for x in range(password_length):
    
    password.append(random.choice(password_pool))
    random.shuffle(password)
    
    #password = "".join(password)
user_password = ''.join(password)
    
print(user_password)
    

