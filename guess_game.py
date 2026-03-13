import random

number = random.randint(1, 10)
attempts = 0
score = 0

while True:
    guess = int(input("Guess number between 1 and 10: "))
    attempts += 1

    if guess == number:
        score = 10 - attempts
        print("Correct!")
        print("Attempts:", attempts)
        print("Score:", score)
        break
    else:
        print("Wrong, try again")