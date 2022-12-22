from tkinter import *
from math import *

root = Tk()
c = Canvas(root, width=600, height=600, bg="chartreuse")
c.pack()

c.create_oval(10, 10, 190, 190,
              fill='lightgrey',
              outline='white')
c.create_arc(10, 10, 190, 190,
             start=0, extent=45,
             fill='red')
c.create_arc(10, 10, 190, 190,
             start=180, extent=25,
             fill='orange')
c.create_arc(10, 10, 190, 190,
             start=240, extent=100,
             style=CHORD, fill='green')
c.create_arc(10, 10, 190, 190,
             start=160, extent=-70,
             style=ARC, outline='darkblue',
             width=5)

#for x in range(40, 600, 20):
#    c.create_line(x, 40, x, 600, fill='lightgray')
#   c.create_text(x, 20, text=x, font='Arial 8')

#for y in range(40, 600, 20):
#   c.create_line(40, y, 580, y, fill='lightgray')
#    c.create_text(20, y, text=y, font='Arial 8')

#c.create_line(40, 40, 580, 40, width=2, arrow='last')
#c.create_line(40, 40, 40, 580, width=2, arrow='last')


root.mainloop()