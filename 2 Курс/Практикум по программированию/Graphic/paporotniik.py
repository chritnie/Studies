from tkinter import *
import numpy as np
import random

k = [[0, 0, 0, .16, 0, 0],
                 [.85, .04, -.04, .85, 0, 1.6],
                 [.2, -.26, .23, .22, 0, 1.6],
                 [-.15, .28, .26, .24, 0, .44]]

def f(x, y, a, b, c, d, e, f):

    return np.matrix([[a, b], [c, d]]) * np.matrix([[x], [y]]) + np.matrix([[e], [f]])

width = 1000
height = 700

root = Tk()
canvas = Canvas(root, width=width, height=height, bg = 'white')
canvas.pack()

x, y = 0, 0

while True:
    P = random.randint(0, 100)

    if P == 0:
        XY = f(x, y, *k[0])
    elif P < 85:
        XY = f(x, y, *k[1])
    elif P < 93:
        XY = f(x, y, *k[2])
    else:
        XY = f(x, y, *k[3])

    x = XY[0].item()
    y = XY[1].item()

    canvas.create_oval((x * 60 + width / 2, -y * 60 + height / 1.1),
                     (x * 60 + width / 2, -y * 60 + height / 1.1), fill = 'green')
    canvas.update()

root.mainloop()