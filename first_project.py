print(" --------------WELCOME IN MY QUIZ GAME ----------------")
ans=input("Do yoy want to start the game ?").upper()
if ans=="YES":
      print("let's begin")
      print("Some Rools and regulations : 1: attempt All question is mandatory.")
import random

def quiz_game():
    questions = [
        {"question": "Question about Capital : What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
        {"question": "Question about planet : Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "answer": "B"},
        {"question": "Question about OCEAN : What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], "answer": "D"},
        {"question": " Question about math :  integration of log x ?", "options": ["A. 1", "B. x logx.x", "C. logx.x", "D. 2/4"], "answer": "B"},
        {"question": "Question about Chemistry : What is the chemical symbol for Gold?", "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"], "answer": "A"}
    ]
    
    score = 0
    random.shuffle(questions)
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    
    print(f"\nYour final score is {score}/{len(questions)}")
    
if __name__ == "__main__":
    quiz_game()
