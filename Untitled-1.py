while(True):
    user_input = input ("Provide a number")
    if(user_input() == "q"):
        break
    if(not user_input.isdigit()):
        print("you didn't provide a number =(")
    if(user_input.isdigit()):
        print("cool number")

fruits = ['apples','oranges','bananas','tomatoes']
user_fruits = input("What is your favorite fruit?")
if (user_fruits in fruits):
    print("cool")
else:
    print("meh")