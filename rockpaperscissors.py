import random
choices =["Rock","Paper","Scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter Rock, Paper, or Scissors (Enter q to quit)").capitalize()
    if user_choice == "Q":
        break
    if user_choice == "Rock" and computer_choice == "Rock":
        print(f"I picked {computer_choice}! It's a tie!")
    if user_choice == "Rock" and computer_choice == "Paper":
        print(f"I picked {computer_choice}! I win!")
    if user_choice == "Rock" and computer_choice == "Scissors":
        print(f"I picked {computer_choice}! You win!")
    if user_choice == "Scissors" and computer_choice == "Rock":
        print(f"I picked {computer_choice}! I win!")
    if user_choice == "Paper" and computer_choice == "Rock":
        print(f"I picked {computer_choice}! You win!")
    if user_choice == "Paper" and computer_choice == "Scissors":
        print(f"I picked {computer_choice}! I win!")
    if user_choice == "Paper" and computer_choice == "Paper":
        print(f"I picked {computer_choice}! It's a tie!")
    if user_choice == "Scissors" and computer_choice == "Scissors":
        print(f"I picked {computer_choice}! It's a tie!")
    if user_choice == "Scissors" and computer_choice == "Paper":
        print(f"I picked {computer_choice}! You win!")