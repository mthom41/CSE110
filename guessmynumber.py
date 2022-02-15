import random

guessed = False
target = random.randint(1,10)
guess = 0
guesses = 0
while guessed == False:
    guess = int(input("Pick a number between 1 and 10: \n"))
    guesses += 1
    if guess == target:
        guessed = True
        print("You got it!")
        print("Guesses: "+str(guesses))
        pa = input("Play again? (y/n): ")
        if pa.lower() == "y":
            guessed = False
            target = random.randint(1,10)
            guesses = 0
    elif guess < target:
        print("You're too low, go up a little")
    elif guess > target:
        print("Too high! Guess a little lower.")

