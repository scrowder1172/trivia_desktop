from ui import QuizUI
from data import QuestionData
from question_model import Question


number_of_questions = 20
data = QuestionData(question_count=number_of_questions)

question_bank = []
for question in data.get_question_data():
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz_ui = QuizUI()

