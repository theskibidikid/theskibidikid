from tkinter import *
from tkinter import messagebox


class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "English or Spanish?",
                "options": [
                    "English",
                    "Spanish",
                    "Whoever moves first is Gay",
                    "69",
                    "420",
                ],
                "answer": "Whoever moves first is Gay",
            },
            {
                "question": "What is Orange?",
                "options": ["Fruit", "Color", "Feeling", "none", "all"],
                "answer": "all",
            },
            {
                "question": "1+1",
                "options": ["window", "2", "gender equality", "3", "69420"],
                "answer": "gender equality",
            },
            {
                "question": "state of usa political right now?",
                "options": [
                    "sleepy joe will drink one more mcdonalds sprite and meet kobe bryant",
                    "trump will trump the reporters",
                    "freedom!!!",
                    "cheeseburgers will take over the world and use humans greatest weakness: obesity",
                    "ben shapiro",
                ],
                "answer": "freedom!!!",
            },
            {
                "question": "what planet has the thicc atmosphere of all!!!",
                "options": ["venus", "sun", "jupiter", "caseoh", "saturn"],
                "answer": "jupiter",
            },
            {
                "question": "ben,dover has 8 apples, his toilet is 7 minutes late, calculate the mass of the sun",
                "options": ["69", "420", "69420", "100000000", "1.989 × 10^30 kg"],
                "answer": "1.989 × 10^30 kg",
            },
            {
                "question": "if boe jiden eats 420 ice creams from his beer dispenser, and his favorite number of the alphabet is pink, how many grams of powder will he feed his pet garbage can?",
                "options": [
                    "idk",
                    "wgyatt the sigma",
                    "cheezbruhgher wufrel",
                    "touch grass kid",
                    "An error has occured. To continue:",
                ],
                "answer": "An error has occured. To continue:",
            },
        ]
        self.score = 0
        self.current_question = 0

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score = self.score + 1
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.current_question + 1
        if self.current_question < len(self.questions):
            return True
        else:
            return False


class App(Tk):
    def __init__(self, quiz):
        Tk.__init__(self)
        self.title("Brain is where")
        self.my_quiz = quiz
        self.config(bg="yellow")
        self.geometry("800x550")
        self.title = Label(self, text="your brain has gone to mars")
        self.title.config(font=("Giddyup Std", 15))
        self.title.place(x=250, y=10)
        self.question_label = Label(self, text="", wraplength=400)
        self.question_label.config(font=("Comic Sans MS", 12))
        self.question_label.pack(pady=50)
        self.option_list = StringVar(value="")
        self.option_button = []
        for i in range(5):
            rb = Radiobutton(self, text="", variable=self.option_list, value="")
            rb.pack(anchor=W, padx=20, pady=5)
            self.option_button.append(rb)
        self.submit_button = Button(
            self, text="ydk the answer then die", command=self.submit_answer
        )
        self.submit_button.config(font=("Jokerman", 12))
        self.submit_button.pack(pady=20)
        self.answer_label = Label(self, text="")
        self.answer_label.config(font=("Haettenschweiler", 12))
        self.answer_label.pack(pady=20)
        self.score_label = Label(self, text="brain sigma moments: 0")
        self.score_label.config(font=("Comic Sans MS", 12))
        self.score_label.pack(pady=10)
        self.load_question()

    def load_question(self):
        question_data = self.my_quiz.questions[self.my_quiz.current_question]
        self.question_label.config(text=question_data["question"])
        self.option_list.set("")
        for index, option in enumerate(question_data["options"]):
            self.option_button[index].config(text=option, value=option)

    def submit_answer(self):
        selected_option = self.option_list.get()
        correct = self.my_quiz.check_answer(selected_option)
        if correct:
            self.answer_label.config(text="skibidi edge w rizzler", fg="green")
        else:
            correct_answer = self.my_quiz.questions[self.my_quiz.current_question][
                "answer"
            ]
            self.answer_label.config(
                text=f"lol L rizz cant talk to girls without peeing your pants LLLL\n correct answer: {correct_answer}",
                fg="maroon",
            )
        self.score_label.config(text=f"brain sigma moments: {self.my_quiz.score}")
        if self.my_quiz.next_question():
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo(
            "go back to work you monkey", f"your rizz level: {self.my_quiz.score}/{len(self.my_quiz.questions)}"
        )
        self.submit_button.config(state=DISABLED)


my_quiz = Quiz()
App(my_quiz)
mainloop()
