from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ('Arial', 20, 'italic')


class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Time!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="sample", font=QUESTION_FONT, fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)


        self.window.mainloop()

