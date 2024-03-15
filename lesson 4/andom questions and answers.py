import tkinter as tk
import random

class RandomQuestionsApp:
    def __init__(self, root ):
        self. A = A
        self.questions = []

        self.question_label = tk.Label(A, text="")
        self.question_label.pack()

        self.add_question_button = tk.Button(A, text="Добавить вопрос", command=self.add_question)
        self.add_question_button.pack()

        self.edit_question_button = tk.Button(A, text="Редактировать вопрос", command=self.edit_question)
        self.edit_question_button.pack()

        self.delete_question_button = tk.Button(A, text="Удалить вопрос", command=self.delete_question)
        self.delete_question_button.pack()

        self.ask_question_button = tk.Button(A, text="Задать вопрос", command=self.ask_question)
        self.ask_question_button.pack()

    def add_question(self):
        question = input("Введите ваш вопрос: ")
        self.questions.append(question)

    def edit_question(self):
        index = int(input("Введите индекс вопроса, который вы хотите отредактировать: "))
        new_question = input("Введите ваш вопрос: ")

    def delete_question(self):
        index = int(input("Введите индекс вопроса, который вы хотите удалить: "))
        del self.questions[index]

    def ask_question(self):
        if not self.questions:
            self.question_label.config(text="Вопросов нет")
        else:
            random_question = random.choice(self.questions)
            self.question_label.config(text=random_question)

A = tk.Tk()
app = RandomQuestionsApp(A)
A.mainloop()
