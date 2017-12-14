#!/usr/bin/python3

import random
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Формула-1')
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
        self.canv = tk.Canvas(self, width=1000, height=500, bg="grey")
        self.canv.pack()
        self.create_cars()

    def create_cars(self):
        self.list_car = []
        colors = ("white", "black", "red", "green", "blue", "cyan", "yellow", "magenta")
        for i in range(8):
            self.list_car.append(Car(self.canv, False, colors[i], i))

    @staticmethod
    def about():
        showinfo('Информация', 'Гонки')

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    def move(self, n):
        if len(n) < len(self.list_car) + 1:
            self.run_flag = True
            for car in self.list_car:
                car.update()
                n.add(car.fin_flag)
            print(n)
            self.canv.after(30, lambda: self.move(n))
        else:
            s = ''
            for car in self.list_car:
                s += "Цвет - %s, время = %d\n" % (car.color, car.n)
            showinfo('Финиш', 'Заезд окончен\n' + s)
            self.run_flag = False
            self.canv.delete('all')
            self.create_cars()

    def start(self):
        if self.run_flag is True:
            showinfo('Извините', 'Гонка уже началась!')
            return
        n = set()
        self.move(n)


class Car:
    def __init__(self, canv, mycar, color, line):
        self.size_x = 60
        self.size_y = 30
        self.color = color
        self.mycar = mycar
        self.finish_x = 950
        self.mycar = mycar
        random.seed()
        self.canv = canv
        self.fin_flag = None
        self.n = 0
        self.v = 0
        self.x = 20
        self.y = 10 + (self.size_y + 30) * line
        self.idc = self.canv.create_rectangle(self.x, self.y, self.x + self.size_x, self.y + self.size_y,
                                              fill=self.color)

    def update(self):
        if self.x + self.size_x < self.finish_x:
            self.v = self.v + random.randint(-self.v + 1, 10)
            self.n += 1
            self.x += self.v
            self.canv.move(self.idc, self.v, 0)
            self.canv.update()
        else:
            self.fin_flag = self.color


app = App()
app.mainloop()
