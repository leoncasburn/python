import random
print("Hello Welcome To The Number Guessing Game!")
range = int(input("Enter the max the number can be:"))
secret_number = random.randint(1,range)

print(f"I have picked a number between 1-{range}")

if range < 20:
    print(f"As you have picked {range}, you will only have 5 guesses")
    guess_counter = 5
else:
    guess_counter = 10

guess = int(input("Enter your guess: "))
counter = 1

won = False

while guess != secret_number:
    if guess_counter < 1:
        print("You ran out of guesses!")
        break
    if guess > secret_number:
        print("Too high, try again!")
        guess = int(input("Enter your guess: "))
        guess_counter -= 1
        counter += 1
    elif guess < secret_number:
        print("Too low, try again!")
        guess = int(input("Enter your guess: "))
        guess_counter -= 1
        counter += 1
else:
    won = True

if won:
    print(f"You got it! The number was {secret_number} and it took you {counter} guesses!")
else:
    print(f"Game over! The number was {secret_number}!")

