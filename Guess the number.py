#project3.

import random 
hidden_number = random.randint(1,100)
limit_of_try = float(5)
_try = (0)
while _try <= 5 :
    user_input = float(input("Enter a number: "))
    if _try == 4:
        print("Game over")
        break
    elif user_input == hidden_number:
        print("Congratulations! you guess the number. ")
        _try = _try + 1
        print("you guess the number in " + str(_try) + " tries")
        break
    elif user_input > hidden_number:
        print(str(hidden_number) + " is less than " + str(user_input) + " Please try again")
        _try = _try + 1
        print("life left " + str(limit_of_try - _try))
    elif user_input < hidden_number:
        print(str(hidden_number) + " is greatter than " + str(user_input) + " Please try again")
        _try = _try + 1
        print("life left " + str(limit_of_try - _try))
    else:
        print("Error")
