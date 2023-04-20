from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ('Arial', 20, 'italic')


class QuizUI:

    def __init__(self):
        """
        Create UI window
        Create canvas with text that will wrap (width=280)
        """
        self.window = Tk()
        self.window.title("Trivia Time!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="sample", font=QUESTION_FONT, fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)


        self.window.mainloop()

