from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]

for i in range(len(question_data)):
    question=Question(question_data[i]["question"],question_data[i]['correct_answer'] )
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have Completed the quiz")
print(f"Your total score is: {quiz.score}/{quiz.question_number}")