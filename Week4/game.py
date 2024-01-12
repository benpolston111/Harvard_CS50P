import random

while True:
    level = input("Level: ")
    if level.isnumeric() and level is not "0":
        break

level = int(level)

if level != 1:
    right_num = random.randrange(1, level)


while True:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)
        try:
            if guess < right_num:
                print("Too small!")

            elif guess > right_num:
                print("Too large!")

            elif guess == right_num:
                print("Just right!")
                break

        except:
            if level == 1 and guess == 1:
                print("Just right!")
                break