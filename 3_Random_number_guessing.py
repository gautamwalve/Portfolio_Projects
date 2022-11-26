import random
import math

lower = int(input('Enter Lower Value: '))
upper = int(input('Enter Upper Value: '))

#Generating a random number between lower and upper values
x = random.randint(lower,upper)

#Generating Attempts to guess the number
print(
   "You have only",(round(math.log(upper - lower+1,2))),"attempts to guess the number"
    )

#Initialization of attempts
count = 0
#for Calculations of the attempts to guess basis the chances
while count < round(math.log(upper - lower+1,2)):
    count+=1
    guess = int(input("Guess the Number : "))
    
    #Validating
    if x == guess:
        print("Congratulations on the correct guess in",count,"attempt/s")
        break
    elif guess < x:
        print("Guessed So Low")
    elif guess > x:
        print("Guessed So High")
    if  count >= round(math.log(upper - lower+1,2)):
            print("The correct guess would have been:",x)
            print("You have exceeded the number of attempts,Better Luck Next time,")
