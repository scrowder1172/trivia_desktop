from ui import QuizUI
from data import question_data


question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = "hold"
    question_bank.append(new_question)

quiz_ui = QuizUI()
