import json

with open("files/questions.json", 'r') as f:
    content = f.read()

individual_questions = json.loads(content)

user_score = 0
for i in range(len(individual_questions)):
    print(f"Question {i+1}")
    print(individual_questions[i]['question'])
    for k, v in individual_questions[i]['answers'].items():
        print(f"{k}: {v}")
    user_answer = input("Select Your Answer: ")
    if(user_answer == individual_questions[i]['correct']):
        user_score+=1

print(f"You got {user_score} out of {len(individual_questions)} correct")
