#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calc')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        self.fra = ttk.Frame(self, height=300)
        self.fra.pack(side=tk.BOTTOM, padx=5, pady=10, expand=1)
        self.entry = ttk.Entry(self, width=30)
        self.entry.configure(state='enabled', justify=tk.RIGHT)
        self.entry.insert(tk.END, '0')
        self.entry.configure(state='disabled')
        self.entry.pack(side=tk.TOP, padx=5, pady=10, expand=1)
        self.menu()
        self.keyfunc()
        self.stack = []

    def menu(self):
        m = tk.Menu(self)  # создается объект Меню на главном окне
        self.config(menu=m)  # окно конфигурируется с указанием меню для него
        m.add_command(label='Выход', command=self.close_win)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация', 'Простой калькулятор!')

    def keyfunc(self):
        list_keys = ('Cls', '', '', 'Bck',
                     '7', '8', '9', '/',
                     '4', '5', '6', '*',
                     '1', '2', '3', '-',
                     '0', '.', '=', '+')

        for i, x in enumerate(list_keys):
            if not x:
                continue
            but = ttk.Button(self.fra, text=x, command=lambda y=x: self.calc_main(y), width=4)
            but.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    def calc_main(self, x):
        self.entry.configure(state='enabled')
        operators = ('+', '-', '*', '/')
        if x.isdigit():
            if self.entry.get() == '0' and x == '0':
                self.entry.configure(state='disabled')
                return
            if self.entry.get() == '0':
                self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, x)
        elif x == '.':
            if self.entry.get() == '' or '.' in str(self.entry.get()):
                self.entry.configure(state='disabled')
                return
            self.entry.insert(tk.END, x)
        elif x == 'Cls':
            if self.entry.get():
                self.entry.delete(0, tk.END)
            self.entry.insert(0, '0')
            self.stack.clear()
        elif x == 'Bck':
            if self.entry.get() != '0' or not self.entry.get():
                self.entry.delete(len(self.entry.get()) - 1, tk.END)
                if not self.entry.get():
                    self.entry.insert(0, '0')
        elif x in operators:
            self.stack.append(self.entry.get())
            if self.stack[-1] not in operators:
                self.stack.append(x)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, '0')
        elif x == '=':
            if len(self.stack) > 1:
                self.stack.append(self.entry.get())
                self.entry.delete(0, tk.END)
                try:
                    ansv = eval(''.join(self.stack))
                    if type(ansv) is float and ansv.is_integer():
                        ansv = int(ansv)
                    ansv = str(ansv)
                    self.entry.insert(tk.END, ansv)
                    self.stack.clear()
                except ZeroDivisionError:
                    showerror('Ошибка!', 'Деление на ноль!')
                    self.calc_main('Cls')
        self.entry.configure(state='disabled')


app = App()
app.mainloop()
