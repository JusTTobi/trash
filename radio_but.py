import tkinter as tk

def print_choice():
       print(v.get())

root = tk.Tk()

v = tk.IntVar()
v.set(-1)

tk.Label(root,
        text="""Choose a
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root,
              text="Python",
              padx = 20,
              indicatoron = 0,
              width=20,
              variable=v,
              value=0).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="Perl",
              padx = 20,
              variable=v,
              indicatoron = 0,
              width=20,
              value=1).pack(anchor=tk.W)
tk.Button(root, text='Print', command=print_choice).pack()


root.mainloop()
