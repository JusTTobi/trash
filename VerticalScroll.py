#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:08:26 2018

@author: lashkov
"""
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    """
    Consider me a regular frame with a vertical scrollbar
    on the right, after adding/removing widgets to/from me
    call my method update() to refresh the scrollable area.
    Don't pack() me, nor place() nor grid().
    I work best when I am alone in the parent frame.
    """

    def __init__(self, parent, *args, **kw):

        # scrollbar on right in parent
        yscrollbar = ttk.Scrollbar(parent)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        self.parent = parent
        # canvas on left in parent
        self.canvas = tk.Canvas(parent, yscrollcommand=yscrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        def fill_canvas(event):
            """enlarge the windows item to the canvas width"""
            canvas_width = event.width
            self.canvas.itemconfig(self.windows_item, width=canvas_width)
            self.update()

        self.canvas.bind('Configure', fill_canvas)

        yscrollbar.config(command=self.canvas.yview)

        # create the scrollable frame and assign it to the windows item of the canvas
        tk.Frame.__init__(self, parent, *args, **kw)
        self.windows_item = self.canvas.create_window(0, 0, window=self, anchor=tk.NW)
        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbound_to_mousewheel)

    def _bound_to_mousewheel(self, event):
        self.parent.bind_all("<MouseWheel>", self._on_mousewheel)
        self.parent.bind_all('<Button-4>', self._on_mousewheel)
        self.parent.bind_all('<Button-5>', self._on_mousewheel)
        self.update()

    def _unbound_to_mousewheel(self, event):
        self.parent.unbind_all("<MouseWheel>")
        self.parent.unbind_all('<Button-4>')
        self.parent.unbind_all('<Button-5>')
        self.update()

    def _on_mousewheel(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.update()

    def update(self):
        """
        Update changes to the canvas before the program gets
        back the mainloop, then update the scrollregion
        """
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


if __name__ == '__main__':
    root = tk.Tk()
    root.maxsize(width=500, height=500)
    frame = ScrollableFrame(root)
    for i in range(100):
        lab = tk.Label(frame, text='This is Label No. {0:d}'.format(i))
        lab.grid(row=i, column=0)
    root.mainloop()
