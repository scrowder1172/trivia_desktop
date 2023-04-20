from ui import QuizUI
from data import QuestionData
from question_model import Question
from quiz_brain import QuizBrain


number_of_questions = 20
data = QuestionData(question_count=number_of_questions)

question_bank = []
for question in data.get_question_data():
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

