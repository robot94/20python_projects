#Basic Calculator application

#defining the addition function

def add(a,b):
    
    addition = a+b
    print(addition)


#defining the substraction function

def sub(a,b):
    
    substraction = a-b
    print(substraction)

#defining the division function

def div(a,b):
    
    division = a/b
    print(division)

#defining the mutiplication function

def mult(a,b):
    
    multiplication = a*b
    print(multiplication)

operation = input("Please chose on of the operations: '+' '-' 'x' '/' ")
a = float(input("First number: "))
b = float(input("Second number: "))

if operation == '+':
    add(a,b)
elif operation == '-':
    sub(a,b)
elif operation == 'x':
    mult(a,b)
elif operation == '/':
    div(a,b)
else:
    print(" Invalid operation please try again!")
    
