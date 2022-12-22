from random import *
from tkinter import *

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0

while diapason < 1000:
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
    root.update()
    diapason += 1