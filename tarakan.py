#!/usr/bin/python3

import random
import time
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.choice_flag = False
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
        self.canv = Doroga(self, width=self.wight, height=470, bg="grey20", finish=self.finish)
        self.canv.pack()
        self.list_bugs = []
        self.tstep = 10
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
            for bug in self.list_bugs:
                bug.update()
                n.add(bug.fin_flag)
            self.canv.after(self.tstep, lambda: self.move(n))
        else:
            self.dofinish()

    def dofinish(self):
        vremya = []
        names = []
        flags = []
        s = ''
        for bug in self.list_bugs:
            vremya.append(bug.n * self.tstep / 1000)
            names.append(bug.name)
            flags.append(bug.mycar)
        vremya_sort = vremya[:]
        vremya_sort.sort()
        for t in vremya_sort:
            s += "%s: время = %.2f c\n" % (names[vremya.index(t)], t)
        victory = '\nПоздравляем!!!' if flags[
                                            vremya.index(vremya_sort[0])] is True else '\nПовезёт в следующий раз!'
        showinfo('Финиш', 'Забег окончен!\n\n' + 'Результаты:\n' + s + victory)
        self.run_flag = False
        self.create_bugs()

    def start(self):
        if self.run_flag is True:
            showinfo('Извините', 'Гонка уже началась!')
            return
        self.choice_flag = False
        self.run_flag = True
        self.choice_bugs()
        while True:
            if self.choice_flag is True:
                break
            time.sleep(0.1)
            self.canv.update()
        n = set()
        self.move(n)

    def choice_bugs(self):
        self.win = tk.Toplevel(self)
        self.win.title("Выбор таракана:")
        self.win.minsize(width=220, height=150)
        self.win.resizable(False, False)
        self.win.protocol('WM_DELETE_WINDOW', self.rechoice)
        fra = tk.Frame(self.win)
        fra.pack()
        nrows = 4
        btns = []
        for bug in self.list_bugs:
            btns.append(tk.Button(fra, text=bug.name, bg=bug.color,
                                  command=lambda bugl=bug: self.choice(bugl), width=3))
        for i, btn in enumerate(btns):
            btn.grid(row=i % nrows, column=i // nrows, pady=5, padx=10)

    def choice(self, bug):
        self.win.destroy()
        self.choice_flag = True
        bug.choice()

    def rechoice(self):
        self.win.destroy()
        showinfo('Так нечестно!', 'Пожалуйста, выберите таракана!')
        self.choice_bugs()


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

    def choice(self):
        self.mycar = True
        self.canv.delete(self.idc, self.txt)
        self.idc = self.canv.create_rectangle(self.x, self.y, self.x + self.size_x, self.y + self.size_y,
                                              fill=self.color, width=3)
        self.txt = self.canv.create_text(self.x + self.size_x / 2, self.y + self.size_y / 2, text=self.name,
                                         anchor=tk.CENTER, font=('bold',))


class Doroga(tk.Canvas):
    def __init__(self, root, width, height, bg, finish):
        super().__init__(root, width=width, height=height, bg=bg)
        self.create_line(0, height / 2, width, height / 2, dash=(20,), fill='white', width=4)
        self.create_line(finish, 0, finish, height, dash=(10,), fill='red', width=4)
        self.create_text(finish + 10, height // 2, font=('Helvetica', '20', 'bold'), text='ФИНИШ', anchor=tk.S,
                         angle=-90, fill='red')


app = App()
app.mainloop()
