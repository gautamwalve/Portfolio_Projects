import random
import math
#Taking inputs
lower = int(input("Enter Lower bound Value:- "))
upper = int(input("Enter Upper Bound Value:- "))

#Generating Random Number between the lower and upper bound values
x = random.randint(lower, upper)
print(
    "\n\tYou have only",
    round(math.log(upper - lower+1,2)),"Chances to guess the integer!\n")

#initialization of the  number of guesses
count = 0

#for calculation of minimum number of guess depends upon range.
while count<math.log(upper-lower +1,2):
    count += 1

    #taking guess number from input
    guess = int(input("Guess a number:-"))

    #condition testing
    if x == guess:
        print("Congratulations, You Did It !, in ",count,"try")
        break
    else:
        if x>guess:
            print("You Guessed too Small !")
        elif x<guess:
                print("You Guessed too High !")
    #if Guessing is more than required guesses, then
    if count>=math.log(upper-lower+1,2):
        print (f" \nThe number is %d ", {x})
        print("\tBetter Luck next time!")
