
import random


print("========== NUMBER GUESSING GAME ==========")

# Generate random number
number = random.randint(1, 100)

attempts = 0


while True:

    guess = int(input("Guess a number between 1 and 100: "))

    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! 🎉")
        print("You guessed the correct number!")
        print("Number of attempts:", attempts)
        break
