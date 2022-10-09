#This is a lown interest calculator

def Interest_calculator():
    
    principal = int(input("Please enter the Loan amount: "))
    years = int(input("Please enter the number of years of the loan: "))
    interest = float(input("Please enter the amount of the interesr: %"))
    
    interest_paid = principal * (interest/100) * years
    
    print(f" The Amount of the Interest to be paied over {years} Years is : {interest_paid}$")
    

Interest_calculator()
    