import random

def guess_the_number():
    print("Welcome to the Number Guessing Game")
    print("I have Picked a Number between 1 and 1000")
    print("Try to Guess it!")

    number_to_guess=random.randint(1,1000)
    attempts=0
    while True:
        try:
            guess=int(input(" Enter Your Guess Number:"))
            attempts+=1
            if guess>number_to_guess:
             print(" Your Guess is So High")
            elif guess<number_to_guess:
             print(" Your Guess is So Low")
            elif guess==number_to_guess:
             print(f" You Guessed the Number in {attempts} attempts")
            else:
             print(" Invalid Input")
            break
        except ValueError:
         print(" Invalid Input. Please Try Again")

guess_the_number()

        