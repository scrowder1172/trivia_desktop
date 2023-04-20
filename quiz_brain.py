import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        self.current_question.text references the text attribute of the QuestionModel class.
            This attribute is passed in via q_list which is a list of QuestionModel objects.
            QuestionModel objects include question text (text) and question answers (answer).
        :return:
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(self.current_question)
        q_text = html.unescape(self.current_question.text)
        question = f"Question #{self.question_number}: \n" \
                   f"True or False\n\n" \
                   f"{q_text}"
        return question


