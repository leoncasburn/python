quiz = { "What is the planet closest to the Sun?": "Mercury",
         "How many moons does Mars have?": "2",
         "What planet is furthest from the Sun?": "Neptune",
         "How many planets have rings in the Solar System?": "4",
         "On which planet is a day longer than it's year?": "Venus"}

print("Welcome to the Space Quiz!")
score = 0

for question, answer in quiz.items():
    print(question)
    user_answer = input("Your answer: ").capitalize()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer was {answer}")
print(f"Quiz completed! You got {score}/{len(quiz)} questions right!")


    