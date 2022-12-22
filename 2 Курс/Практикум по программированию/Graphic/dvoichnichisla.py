from tkinter import *

root = Tk()
c = Canvas(root, width=370, height=150, bg="lightgray")
c.pack()

numeric = 0
flag_1 = False
switch = False
ternary_flag_1 = -1

def click_1(event):
    global flag_1, numeric, ternary_flag_1
    if not switch:
        if not flag_1:
            flag_1 = True
            c.itemconfig(text_1, fill='white')
            c.itemconfig(btn_1, fill='black', outline='black')
        else:
            flag_1 = False
            c.itemconfig(text_1, fill='black')
            c.itemconfig(btn_1, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_1, text=128)
    else:
        if ternary_flag_1 == -1:
            ternary_flag_1 = 0
            c.itemconfig(btn_1, fill='grey', outline='grey')
            c.itemconfig(text_1, text=0)
        elif ternary_flag_1 == 0:
            ternary_flag_1 = 1
            c.itemconfig(text_1, fill='white', text=3 ** 7)
            c.itemconfig(btn_1, fill='black', outline='black')
        else:
            ternary_flag_1 = -1
            c.itemconfig(text_1, fill='black', text=-3 ** 7)
            c.itemconfig(btn_1, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()



flag_2 = False
ternary_flag_2 = -1


def click_2(event):
    global flag_2, numeric, ternary_flag_2
    if not switch:
        if not flag_2:
            flag_2 = True
            c.itemconfig(text_2, fill='white')
            c.itemconfig(btn_2, fill='black', outline='black')
        else:
            flag_2 = False
            c.itemconfig(text_2, fill='black')
            c.itemconfig(btn_2, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_2, text=64)
    else:
        if ternary_flag_2 == -1:
            ternary_flag_2 = 0
            c.itemconfig(btn_2, fill='grey', outline='grey')
            c.itemconfig(text_2, text=0)
        elif ternary_flag_2 == 0:
            ternary_flag_2 = 1
            c.itemconfig(text_2, fill='white', text=3 ** 6)
            c.itemconfig(btn_2, fill='black', outline='black')
        else:
            ternary_flag_2 = -1
            c.itemconfig(text_2, fill='black', text=-3 ** 6)
            c.itemconfig(btn_2, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_3 = False
ternary_flag_3 = -1


def click_3(event):
    global flag_3, numeric, ternary_flag_3
    if not switch:
        if not flag_3:
            flag_3 = True
            c.itemconfig(text_3, fill='white')
            c.itemconfig(btn_3, fill='black', outline='black')
        else:
            flag_3 = False
            c.itemconfig(text_3, fill='black')
            c.itemconfig(btn_3, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_3, text=32)
    else:
        if ternary_flag_3 == -1:
            ternary_flag_3 = 0
            c.itemconfig(btn_3, fill='grey', outline='grey')
            c.itemconfig(text_3, text=0)
        elif ternary_flag_3 == 0:
            ternary_flag_3 = 1
            c.itemconfig(text_3, fill='white', text=3 ** 5)
            c.itemconfig(btn_3, fill='black', outline='black')
        else:
            ternary_flag_3 = -1
            c.itemconfig(text_3, fill='black', text=-3 ** 5)
            c.itemconfig(btn_3, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_4 = False
ternary_flag_4 = -1

def click_4(event):
    global flag_4, numeric, ternary_flag_4
    if not switch:
        if not flag_4:
            flag_4 = True
            c.itemconfig(text_4, fill='white')
            c.itemconfig(btn_4, fill='black', outline='black')
        else:
            flag_4 = False
            c.itemconfig(text_4, fill='black')
            c.itemconfig(btn_4, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_4, text=16)
    else:
        if ternary_flag_4 == -1:
            ternary_flag_4 = 0
            c.itemconfig(btn_4, fill='grey', outline='grey')
            c.itemconfig(text_4, text=0)
        elif ternary_flag_4 == 0:
            ternary_flag_4 = 1
            c.itemconfig(text_4, fill='white', text=3 ** 4)
            c.itemconfig(btn_4, fill='black', outline='black')
        else:
            ternary_flag_4 = -1
            c.itemconfig(text_4, fill='black', text=-3 ** 4)
            c.itemconfig(btn_4, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_5 = False
ternary_flag_5 = -1

def click_5(event):
    global flag_5, numeric, ternary_flag_5
    if not switch:
        if not flag_5:
            flag_5 = True
            c.itemconfig(text_5, fill='white')
            c.itemconfig(btn_5, fill='black', outline='black')
        else:
            flag_5 = False
            c.itemconfig(text_5, fill='black')
            c.itemconfig(btn_5, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_5, text=8)
    else:
        if ternary_flag_5 == -1:
            ternary_flag_5 = 0
            c.itemconfig(btn_5, fill='grey', outline='grey')
            c.itemconfig(text_5, text=0)
        elif ternary_flag_5 == 0:
            ternary_flag_5 = 1
            c.itemconfig(text_5, fill='white', text=3 ** 3)
            c.itemconfig(btn_5, fill='black', outline='black')
        else:
            ternary_flag_5 = -1
            c.itemconfig(text_5, fill='black', text=-3 ** 3)
            c.itemconfig(btn_5, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_6 = False
ternary_flag_6 = -1

def click_6(event):
    global flag_6, numeric, ternary_flag_6
    if not switch:
        if not flag_6:
            flag_6 = True
            c.itemconfig(text_6, fill='white')
            c.itemconfig(btn_6, fill='black', outline='black')
        else:
            flag_6 = False
            c.itemconfig(text_6, fill='black')
            c.itemconfig(btn_6, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_6, text=4)
    else:
        if ternary_flag_6 == -1:
            ternary_flag_6 = 0
            c.itemconfig(btn_6, fill='grey', outline='grey')
            c.itemconfig(text_6, text=0)
        elif ternary_flag_6 == 0:
            ternary_flag_6 = 1
            c.itemconfig(text_6, fill='white', text=3 ** 2)
            c.itemconfig(btn_6, fill='black', outline='black')
        else:
            ternary_flag_6 = -1
            c.itemconfig(text_6, fill='black', text=-3 ** 2)
            c.itemconfig(btn_6, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_7 = False
ternary_flag_7 = -1

def click_7(event):
    global flag_7, numeric, ternary_flag_7
    if not switch:
        if not flag_7:
            flag_7 = True
            c.itemconfig(text_7, fill='white')
            c.itemconfig(btn_7, fill='black', outline='black')
        else:
            flag_7 = False
            c.itemconfig(text_7, fill='black')
            c.itemconfig(btn_7, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_7, text=2)
    else:
        if ternary_flag_7 == -1:
            ternary_flag_7 = 0
            c.itemconfig(btn_7, fill='grey', outline='grey')
            c.itemconfig(text_7, text=0)
        elif ternary_flag_7 == 0:
            ternary_flag_7 = 1
            c.itemconfig(text_7, fill='white', text=3 ** 1)
            c.itemconfig(btn_7, fill='black', outline='black')
        else:
            ternary_flag_7 = -1
            c.itemconfig(text_7, fill='black', text=-3 ** 1)
            c.itemconfig(btn_7, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()


flag_8 = False
ternary_flag_8 = -1

def click_8(event):
    global flag_8, numeric, ternary_flag_8
    if not switch:
        if not flag_8:
            flag_8 = True
            c.itemconfig(text_8, fill='white')
            c.itemconfig(btn_8, fill='black', outline='black')
        else:
            flag_8 = False
            c.itemconfig(text_8, fill='black')
            c.itemconfig(btn_8, fill='white', outline='white')
        numeric = int(flag_1) * 2 ** 7 + int(flag_2) * 2 ** 6 + int(flag_3) * 2 ** 5 + int(flag_4) * 2 ** 4 + int(
            flag_5) * 2 ** 3 + int(flag_6) * 2 ** 2 + int(flag_7) * 2 ** 1 + int(flag_8) * 2 ** 0
        text_var.set(numeric)
        c.itemconfig(text_8, text=1)
    else:
        if ternary_flag_8 == -1:
            ternary_flag_8 = 0
            c.itemconfig(btn_8, fill='grey', outline='grey')
            c.itemconfig(text_8, text=0)
        elif ternary_flag_8 == 0:
            ternary_flag_8 = 1
            c.itemconfig(text_8, fill='white', text=3 ** 0)
            c.itemconfig(btn_8, fill='black', outline='black')
        else:
            ternary_flag_8 = -1
            c.itemconfig(text_8, fill='black', text=-3 ** 0)
            c.itemconfig(btn_8, fill='white', outline='white')
        numeric = ternary_flag_1 * 3 ** 7 + ternary_flag_2 * 3 ** 6 + ternary_flag_3 * 3 ** 5 + ternary_flag_4 * 3 ** 4 + \
                  ternary_flag_5 * 3 ** 3 + ternary_flag_6 * 3 ** 2 + ternary_flag_7 * 3 ** 1 + ternary_flag_8 * 3 ** 0
        text_var.set(numeric)
    root.title()

def turn_ternary():
    global numeric, ternary_flag_1, ternary_flag_2, ternary_flag_3, ternary_flag_4, ternary_flag_5, ternary_flag_6, ternary_flag_7, ternary_flag_8,\
        flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8, switch
    if btn_turn['text'] == 2:
        switch = True
        btn_turn['text'] = "-3+"
        ternary_flag_1, ternary_flag_2, ternary_flag_3, ternary_flag_4, ternary_flag_5, ternary_flag_6, ternary_flag_7, ternary_flag_8 = -1, -1, -1, -1, -1, -1, -1, -1
        c.itemconfig(btn_1, fill='white', outline='white'), c.itemconfig(btn_2, fill='white', outline='white'), c.itemconfig(btn_3, fill='white', outline='white'),
        c.itemconfig(btn_4, fill='white', outline='white'), c.itemconfig(btn_5, fill='white', outline='white'), c.itemconfig(btn_6, fill='white', outline='white'),
        c.itemconfig(btn_7, fill='white', outline='white'), c.itemconfig(btn_8, fill='white', outline='white')
        c.itemconfig(text_1, fill='black', text=-3 ** 7)
        c.itemconfig(text_2, fill='black', text=-3 ** 6)
        c.itemconfig(text_3, fill='black', text=-3 ** 5)
        c.itemconfig(text_4, fill='black', text=-3 ** 4)
        c.itemconfig(text_5, fill='black', text=-3 ** 3)
        c.itemconfig(text_6, fill='black', text=-3 ** 2)
        c.itemconfig(text_7, fill='black', text=-3 ** 1)
        c.itemconfig(text_8, fill='black', text=-3 ** 0)
        numeric = -3280
        text_var.set(numeric)
    else:
        switch = False
        btn_turn['text'] = 2
        flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8 = False, False, False, False, False, False, False, False
        c.itemconfig(btn_1, fill='white', outline='white')
        c.itemconfig(btn_2, fill='white', outline='white')
        c.itemconfig(btn_3, fill='white', outline='white')
        c.itemconfig(btn_4, fill='white', outline='white')
        c.itemconfig(btn_5, fill='white', outline='white')
        c.itemconfig(btn_6, fill='white', outline='white')
        c.itemconfig(btn_7, fill='white', outline='white')
        c.itemconfig(btn_8, fill='white', outline='white')
        c.itemconfig(text_1, text=128, fill='black')
        c.itemconfig(text_2, text=64, fill='black')
        c.itemconfig(text_3, text=32, fill='black')
        c.itemconfig(text_4, text=16, fill='black')
        c.itemconfig(text_5, text=8, fill='black')
        c.itemconfig(text_6, text=4, fill='black')
        c.itemconfig(text_7, text=2, fill='black')
        c.itemconfig(text_8, text=1, fill='black')
        numeric = '0'
        text_var.set(numeric)


text_var = StringVar()
timelabel = Label(root, textvariable=text_var, font=('Cambria', 30, 'bold', 'normal'), bg='lightgrey')
timelabel.place(x=0, y=60, width=110, height=70)

btn_1 = c.create_oval(10, 10, 50, 50, fill = 'white', outline='white')
text_1 = c.create_text(30, 30, text=128, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_1, '<Button-1>', click_1)
c.tag_bind(text_1, '<Button-1>', click_1)

btn_2 = c.create_oval(55, 10, 95, 50, fill='white', outline='white')
text_2 = c.create_text(75, 30, text=64, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_2, '<Button-1>', click_2)
c.tag_bind(text_2, '<Button-1>', click_2)

btn_3 = c.create_oval(100, 10, 140, 50, fill = 'white', outline='white')
text_3 = c.create_text(120, 30, text=32, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_3, '<Button-1>', click_3)
c.tag_bind(text_3, '<Button-1>', click_3)

btn_4 = c.create_oval(145, 10, 185, 50, fill = 'white', outline='white')
text_4 = c.create_text(165, 30, text=16, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_4, '<Button-1>', click_4)
c.tag_bind(text_4, '<Button-1>', click_4)

btn_5 = c.create_oval(190, 10, 230, 50, fill = 'white', outline='white')
text_5 = c.create_text(210, 30, text=8, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_5, '<Button-1>', click_5)
c.tag_bind(text_5, '<Button-1>', click_5)

btn_6 = c.create_oval(235, 10, 275, 50, fill = 'white', outline='white')
text_6 = c.create_text(255, 30, text=4, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_6, '<Button-1>', click_6)
c.tag_bind(text_6, '<Button-1>', click_6)

btn_7 = c.create_oval(280, 10, 320, 50, fill = 'white', outline='white')
text_7 = c.create_text(300, 30, text=2, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_7, '<Button-1>', click_7)
c.tag_bind(text_7, '<Button-1>', click_7)

btn_8 = c.create_oval(325, 10, 365, 50, fill = 'white', outline='white')
text_8 = c.create_text(345, 30, text=1, font=('Cambria', 10, 'bold', 'normal'))
c.tag_bind(btn_8, '<Button-1>', click_8)
c.tag_bind(text_8, '<Button-1>', click_8)

btn_turn = Button(relief='ridge',
                  text=2, font=('Cambria', 10, 'bold', 'normal'),
                  fg='black',
                  bd='0',
                  bg='white',
                  command=turn_ternary)
btn_turn.place(x=325, y=105, width=40, height=40)

root.mainloop()
