#!/usr/bin/python3


import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.choice_flag = False
        self.title('Точки и линии')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        menu = tk.Menu(self)
        self.config(menu=menu)
        first_menu = tk.Menu(self)
        menu.add_cascade(label='Точки', menu=first_menu)
        first_menu.add_command(label='Добавить точку', command=self.add_point)
        first_menu.add_command(label='Удалить последнюю', command=self.del_point)
        first_menu.add_command(label='Очистить точки', command=self.clear_all)
        first_menu.add_command(label='Выход', command=self.close_win)
        second_menu = tk.Menu(self)
        menu.add_cascade(label='Линия', menu=second_menu)
        second_menu.add_command(label='Добавить прямые', command=self.lines_add)
        second_menu.add_command(label='Очистить прямые', command=self.lines_del)
        self.width, self.height = 500, 500
        self.canv = tk.Canvas(self, width=self.width, height=self.height, bg='grey90')
        self.canv.pack()
        self.lines_ids = []
        self.point_list = []

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    def add_point(self):
        self.win = tk.Toplevel(self)
        self.win.title('Задайте координаты точки')
        self.win.minsize(width=270, height=50)
        self.win.resizable(False, False)
        lab_x = tk.Label(self.win, text='X-координата (0-{0:d})'.format(self.width))
        lab_y = tk.Label(self.win, text='Y-координата (0-{0:d})'.format(self.height))
        self.ent_x = tk.Entry(self.win, width=10, bd=3)
        self.ent_y = tk.Entry(self.win, width=10, bd=3)
        but_cancel = tk.Button(self.win, text='Отмена', command=self.win.destroy)
        but_ok = tk.Button(self.win, text='ОK', command=self._add_point)
        lab_x.grid(row=0, column=0, pady=5, padx=5)
        lab_y.grid(row=1, column=0, pady=5, padx=5)
        self.ent_x.grid(row=0, column=1, pady=5, padx=5)
        self.ent_y.grid(row=1, column=1, pady=5, padx=5)
        but_cancel.grid(row=2, column=0, pady=5, padx=5)
        but_ok.grid(row=2, column=1, pady=5, padx=5)

    def _add_point(self):
        try:
            x = int(self.ent_x.get())
            y = int(self.ent_y.get())
            if x < 0 or x > self.width or y < 0 or y > self.height:
                raise ValueError
        except ValueError:
            showerror('Ошибка!',
                      'Координаты должны быть целыми числами\nи находится в заданном диапазоне')
            self.win.destroy()
        else:
            id_point = self.canv.create_oval(x - 2, y - 2, x + 2, y + 2, fill='green')
            self.point_list.append((x, y, id_point))
            self.win.destroy()

    def del_point(self):
        if self.point_list:
            last_point = self.point_list.pop()
            self.canv.delete(last_point[2])

    def clear_all(self):
        if self.point_list:
            for x, y, id in self.point_list:
                self.canv.delete(id)
            self.point_list.clear()

    def lines_add(self):
        self.lines_del()
        self.line_draw(self.point_list[0][0], self.point_list[0][1],
                       self.point_list[1][0], self.point_list[1][1], )

    def lines_del(self):
        if self.lines_ids:
            for line in self.lines_ids:
                self.canv.delete(line)
            self.lines_ids.clear()

    def line_draw(self, x1, y1, x2, y2):
        y_minx = self.line_eqy(0, x1, y1, x2, y2)
        x_miny = self.line_eqx(0, x1, y1, x2, y2)
        y_maxx = self.line_eqy(self.width, x1, y1, x2, y2)
        x_maxy = self.line_eqx(self.height, x1, y1, x2, y2)
        dots = []
        if 0 < y_minx < self.height:
            dots.append((0, y_minx))
        if 0 < y_maxx < self.height:
            dots.append((self.width, y_maxx))
        if 0 < x_miny < self.width:
            dots.append((x_miny, 0))
        if 0 < x_maxy < self.width:
            dots.append((x_maxy, self.width))
        line_id = self.canv.create_line(dots)
        self.lines_ids.append(line_id)

    @staticmethod
    def line_eqy(x, x1, y1, x2, y2):
        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
        return y

    @staticmethod
    def line_eqx(y, x1, y1, x2, y2):
        x = ((x2 - x1) / (y2 - y1)) * (y - y1) + x1
        return x


if __name__ == '__main__':
    app = App()
    app.mainloop()
