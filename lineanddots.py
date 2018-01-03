#!/usr/bin/python3

import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror


def close_win():
    if askyesno('Выход', 'Вы точно хотите выйти?'):
        root.destroy()


def add_point():
    win = tk.Toplevel(root)
    win.title('Задайте координаты точки')
    win.minsize(width=270, height=50)
    win.resizable(False, False)
    lab_x = tk.Label(win, text='X-координата (0-{0:d})'.format(width))
    lab_y = tk.Label(win, text='Y-координата (0-{0:d})'.format(height))
    ent_x = tk.Entry(win, width=10, bd=3)
    ent_y = tk.Entry(win, width=10, bd=3)
    but_cancel = tk.Button(win, text='Отмена', command=win.destroy)
    but_ok = tk.Button(win, text='ОK',
                       command=lambda: _add_point(ent_x=ent_x, ent_y=ent_y, win=win))
    lab_x.grid(row=0, column=0, pady=5, padx=5)
    lab_y.grid(row=1, column=0, pady=5, padx=5)
    ent_x.grid(row=0, column=1, pady=5, padx=5)
    ent_y.grid(row=1, column=1, pady=5, padx=5)
    but_cancel.grid(row=2, column=0, pady=5, padx=5)
    but_ok.grid(row=2, column=1, pady=5, padx=5)


def _add_point(e=None, *, ent_x=None, ent_y=None, win=None):
    if e:
        x = e.x
        y = e.y
    else:
        try:
            x = int(ent_x.get())
            y = int(ent_y.get())
            if x < 0 or x > width or y < 0 or y > height:
                raise ValueError
        except ValueError:
            showerror('Ошибка!',
                      'Координаты должны быть целыми числами\nи находится в заданном диапазоне')
            win.destroy()
            return
        win.destroy()
    id_point = canv.create_oval(x - 2, y - 2, x + 2, y + 2, fill='green')
    point_list.append((x, y, id_point))


def del_point():
    if point_list:
        last_point = point_list.pop()
        canv.delete(last_point[2])


def clear_all():
    if point_list:
        for x, y, id in point_list:
            canv.delete(id)
        point_list.clear()


def lines_add():
    if len(point_list) < 4:
        return

    lines_del()
    rms_lines = []
    for p1l1 in point_list:
        for p2l1 in point_list:
            if p1l1 == p2l1:
                break
            for p1l2 in point_list:
                if p1l1 == p1l2 or p2l1 == p1l2:
                    break
                for p2l2 in point_list:
                    if p1l1 == p2l2 or p2l1 == p2l2 or p1l2 == p2l2:
                        break
                    if ((p2l1[1] - p1l1[1]) / (p2l1[0] - p1l1[0])) == ((p2l2[1] - p1l2[1]) / (p2l2[0] - p1l2[0])):
                        break
                    i, j, k, l = 0, 0, 0, 0
                    for point in point_list:
                        if point[1] > line_eqy(point[0], p1l1[0], p1l1[1], p2l1[0], p2l1[1]) and point[1] > line_eqy(
                                point[0], p1l2[0], p1l2[1], p2l2[0], p2l2[1]):
                            i += 1
                        if point[1] > line_eqy(point[0], p1l1[0], p1l1[1], p2l1[0], p2l1[1]) and point[1] < line_eqy(
                                point[0], p1l2[0], p1l2[1], p2l2[0], p2l2[1]):
                            j += 1
                        if point[1] < line_eqy(point[0], p1l1[0], p1l1[1], p2l1[0], p2l1[1]) and point[1] > line_eqy(
                                point[0], p1l2[0], p1l2[1], p2l2[0], p2l2[1]):
                            k += 1
                        if point[1] < line_eqy(point[0], p1l1[0], p1l1[1], p2l1[0], p2l1[1]) and point[1] < line_eqy(
                                point[0], p1l2[0], p1l2[1], p2l2[0], p2l2[1]):
                            l += 1
                    n_sr = (i+j+k+l)/4
                    rms = (0.25*((i-n_sr)**2+(j-n_sr)**2+(k-n_sr)**2+(l-n_sr)**2))**0.5
                    rms_lines.append((rms, p1l1, p2l1, p1l2, p2l2))
    line = min(rms_lines, key=lambda x: x[0])
    line_draw(line[1][0], line[1][1],
              line[2][0], line[2][1])
    line_draw(line[3][0], line[3][1],
              line[4][0], line[4][1])

def lines_del():
    if lines_ids:
        for line in lines_ids:
            canv.delete(line)
        lines_ids.clear()


def line_draw(x1, y1, x2, y2):
    if x1 == x2:
        line_id = canv.create_line(x1, 0, x1, height)
        lines_ids.append(line_id)
        return
    if y1 == y2:
        line_id = canv.create_line(0, y1, width, y1)
        lines_ids.append(line_id)
        return
    y_minx = line_eqy(0, x1, y1, x2, y2)
    x_miny = line_eqx(0, x1, y1, x2, y2)
    y_maxx = line_eqy(width, x1, y1, x2, y2)
    x_maxy = line_eqx(height, x1, y1, x2, y2)
    if y_minx == 0 and y_maxx == height:
        line_id = canv.create_line(0, 0, width, height)
        lines_ids.append(line_id)
        return
    if y_minx == height and y_maxx == 0:
        line_id = canv.create_line(0, height, width, 0)
        lines_ids.append(line_id)
        return
    dots = []
    if 0 < y_minx < height:
        dots.append((0, y_minx))
    if 0 < y_maxx < height:
        dots.append((width, y_maxx))
    if 0 < x_miny < width:
        dots.append((x_miny, 0))
    if 0 < x_maxy < width:
        dots.append((x_maxy, width))
    line_id = canv.create_line(dots)
    lines_ids.append(line_id)


def line_eqy(x, x1, y1, x2, y2):
    y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
    return y


def line_eqx(y, x1, y1, x2, y2):
    x = ((x2 - x1) / (y2 - y1)) * (y - y1) + x1
    return x


root = tk.Tk()
root.title('Точки и линии')
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', close_win)
menu = tk.Menu(root)
root.config(menu=menu)
first_menu = tk.Menu(root)
menu.add_cascade(label='Точки', menu=first_menu)
first_menu.add_command(label='Добавить точку', command=add_point)
first_menu.add_command(label='Удалить последнюю', command=del_point)
first_menu.add_command(label='Очистить точки', command=clear_all)
first_menu.add_command(label='Выход', command=close_win)
second_menu = tk.Menu(root)
menu.add_cascade(label='Линия', menu=second_menu)
second_menu.add_command(label='Добавить прямые', command=lines_add)
second_menu.add_command(label='Очистить прямые', command=lines_del)
width, height = 500, 500
canv = tk.Canvas(root, width=width, height=height, bg='grey90')
canv.bind('<Button-1>', _add_point)
canv.pack()
lines_ids = []
point_list = []

root.mainloop()
