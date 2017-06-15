#Imports#
from tkinter import *
from decimal import *
import calc_functions

#Window#
window = Tk()
window.title("Python Calculator")
window.resizable(0,0)

#TopRow Frame#
top_row = Frame(window)
top_row.grid(row = 0, column = 0, columnspan = 3, stick = "N")

#Use and Entry for Editable Display#
display = Entry(window, width = 40, bg = "gray64")
display.grid(row = 0, columnspan = 3)

#Num Pad Frame#
num_pad = Frame(window)
num_pad.grid(row = 1, column = 0, stick = "W")

#Numpad keys#
numpadlist = [
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '.','0','='
    ]

r = 0
c = 0

for btntext in numpadlist:
    def cmd(x = btntext):
        click(x)

    Button(num_pad,text = btntext, width = 5, command = cmd).grid(row = r, column = c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

#Operator#
operator = Frame(window)
operator.grid(row = 3, column = 1, sticky = W)

operatorlist = [
    '*','/',
    '+','-',
    '(',')',
    'c'
    ]

r = 0
c = 0

for b in operatorlist:
    def cmd(x = b):
        click(x)

    Button(operator,text = b, width = 5, command = cmd).grid(row = r, column = c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

#Mainloop#
window.mainloop()
