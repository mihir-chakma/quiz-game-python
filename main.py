print("Welcome to Quize Game !!")

score = 0
question_no = 0

play = input("Do you want to play? ").lower()

if play == "yes":
    # --- 1
    question_no += 1  
    ques = input(f"\n{question_no}. What does CPU stand for? ").lower()

    if ques == "central processing unit":
        score += 1
        print("Correct ! you got 1 point.")
    else:
        print("Incorrect !")
        print("Correct answer is --> 'central processing unit' ")

    # --- 2
    question_no += 1  
    ques = input(f"{question_no}. What does GPU stand for? ").lower()

    if ques == "graphics processing unit":
        score += 1
        print("Correct ! you got 1 point.")
    else:
        print("Incorrect !")
        print("Correct answer is --> 'graphics processing unit' ")

    # --- 3 
    question_no += 1  
    ques = input(f"{question_no}. What does RAM stand for? ").lower()

    if ques == "random access memory":
        score += 1
        print("Correct ! you got 1 point.")
    else:
        print("Incorrect !")
        print("Correct answer is --> 'random access memory' ")
    
    # --- 4
    question_no += 1  
    ques = input(f"{question_no}. What does ROM stand for? ").lower()

    if ques == "read only memory":
        score += 1
        print("Correct ! you got 1 point.")
    else:
        print("Incorrect !")
        print("Correct answer is --> 'random access memory' ")

    # --- 5
    question_no += 1  
    ques = input(f"{question_no}. What does PSU stand for? ").lower()

    if ques == "power supply unit":
        score += 1
        print("Correct ! you got 1 point.")
    else:
        print("Incorrect !")
        print("Correct answer is --> 'random access memory' ")

else:
    print("Thank You ! For playing the game.\n")
    quit()

print(f"Number of question is : {question_no}")
print(f"Your score is : {score}")

try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print("0% questions are correct.")

print(f"{percentage}% questions are correct.")