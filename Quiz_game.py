#Welcome to the Quiz Game



questions = {
    "What is your name?": "Youssef",
    "Where you wer born?": "Ait Ishak",
    "How Old are you?": "27"
    
}

score = 0

for question in questions:
    print(question)
    user_answer = input("Please enter your answer: ")
    real_answer = questions[question]
    if user_answer == real_answer:
        score += 1
        print("Correct answer!")
    else:
        print("Sorry wrong answer!")
    

print(f"Your score is {score}")