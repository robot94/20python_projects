#This is a curency convefrter application

from lib2to3.pytree import convert


curency1 = float(input("Enter your DH amount: "))
exchange_rate = float(input("Enter The exchange rate: "))


def converter(dirhams,exchange):
    
    dirhams_to_dollars = dirhams * exchange
    
    #dollars_to_dirhams = dollars * 10.65
    
    print(f"{dirhams}DH is equal to {dirhams_to_dollars}$")
    
converter(curency1,exchange_rate)
    
    
    
    