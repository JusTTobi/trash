#!/usr/bin/python3

import random
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Таракан-1')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        menu = tk.Menu(self)
        self.config(menu=menu)
        first_menu = tk.Menu(self)
        menu.add_cascade(label="Игра", menu=first_menu)
        first_menu.add_command(label="Старт", command=self.start)
        first_menu.add_command(label="Выход", command=self.close_win)
        menu.add_command(label="Справка", command=self.about)
        self.run_flag = False
        self.wight = 1000
        self.finish = self.wight - 50
        self.canv = tk.Canvas(self, width=self.wight, height=470, bg="grey")
        self.canv.pack()
        self.list_bugs = []
        self.create_bugs()

    def create_bugs(self):
        if self.list_bugs:
            for bug in self.list_bugs:
                self.canv.delete(bug.idc, bug.txt)
        self.list_bugs.clear()
        colors = ("white", "lightgrey", "red", "green", "blue", "cyan", "yellow", "magenta")
        names = ('Гоша', 'Гриша', 'Саша', 'Миша', 'Федя', 'Фруня', 'Хрюня', 'Паша')
        for i in range(8):
            self.list_bugs.append(Bug(self.canv, names[i], False, colors[i], self.finish, i))

    @staticmethod
    def about():
        showinfo('Информация', 'Гонки тараканов')

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    def move(self, n):
        if len(n) < len(self.list_bugs) + 1:
            self.run_flag = True
            for bug in self.list_bugs:
                bug.update()
                n.add(bug.fin_flag)
            print(n)
            self.canv.after(20, lambda: self.move(n))
        else:
            vremya = []
            s = ''
            for bug in self.list_bugs:
                s += "%s: время = %d\n" % (bug.name, bug.n)
                vremya.append(bug.n)
            victory = 'Подедитель: {0:s}'.format(self.list_bugs[vremya.index(min(vremya))].name)
            showinfo('Финиш', 'Заезд окончен\n' + s + '\n' + victory)
            self.run_flag = False
            self.create_bugs()

    def start(self):
        if self.run_flag is True:
            showinfo('Извините', 'Гонка уже началась!')
            return
        self.create_bugs()
        n = set()
        self.move(n)


class Bug:
    def __init__(self, canv, name, mybug, color, finish, line):
        self.name = name
        self.size_x = 60
        self.finish_x = finish
        self.size_y = 30
        self.color = color
        self.mycar = mybug
        random.seed()
        self.canv = canv
        self.fin_flag = None
        self.n = 0
        self.v = 0
        self.x = 20
        self.y = 10 + (self.size_y + 30) * line
        self.idc = self.canv.create_rectangle(self.x, self.y, self.x + self.size_x, self.y + self.size_y,
                                              fill=self.color)
        self.txt = self.canv.create_text(self.x + self.size_x / 2, self.y + self.size_y / 2, text=self.name,
                                         anchor=tk.CENTER)

    def update(self):
        if self.x + self.size_x < self.finish_x:
            self.v = self.v + random.randint(-self.v + 1, 5)
            self.n += 1
            self.x += self.v
            self.canv.move(self.idc, self.v, 0)
            self.canv.move(self.txt, self.v, 0)
            self.canv.update()
        else:
            self.fin_flag = self.color


app = App()
app.mainloop()
