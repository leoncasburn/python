import random
print("Hello Welcome To The Number Guessing Game!")
range = int(input("Enter the max the number can be:"))
secret_number = random.randint(1,range)

print(f"I have picked a number between 1-{range}")

if range < 20:
    print(f"As you have picked {range}, you will only have 5 guesses")
    guess_counter = 5

guess = int(input("Enter your guess: "))
counter = 1

while guess != secret_number:
    if guess > secret_number:
        print ("Too high, try again!")
        guess = int(input("Enter your guess: "))
        guess_counter -= 1
        counter += 1
    elif guess < secret_number:
        print ("Too low, try again!")
        guess = int(input("Enter your guess: "))
        guess_counter -= 1
        counter += 1
    elif guess_counter < 1:
        print("Game Over! No guesses left!")
print(f"You got it! The number was {secret_number}, it took you {counter} guesses")

