
operator = input("greetings! what operation do you want to perform today? +, -, *, /,**")
available_operators = ('+','-','*','/','**') 
if (operator in available_operators):
    print("THAT IS AVAILABLE")
else:
    print("=(")
if operator == ('+'):
    print("what do you want to add?")
elif operator == ('-'):
    print("What do you want to subtract? (give me a number)")
elif operator == ('*'):
    print("what do you want to subtract? (give me a number)")
elif operator == ('/'):
    print("what do you want to divide? (give me a number)")
elif operator == ('**'):
    print("what do you want to exponentiate? (give me a number)")
number1 = input()
if(number1.isdigit()):
    number1 = int
if(not number1.isdigit):
    print("that isn't a number")
    print ("what do you want to " ,operator, "it by")
number2 = input()
if(number2.isdigit()):
    number2 = int
if(not number2.isdigit):
    print("that isn't a number either")
print(number1 ,operator, number2)
