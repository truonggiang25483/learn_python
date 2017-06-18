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
operator.grid(row = 1, column = 1, sticky = W)

operatorlist = [
    ' * ',' / ',
    ' + ',' - ',
    ' ( ',' ) ',
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

#Constants#
constants = Frame(window)
constants.grid(row = 3, column = 0, sticky = W)
constantslist = [
'pi',
'Speed of Light(m/s)',
'Speed of Sound(m/s)',
'Ave Distance to Sun(km)']

r = 0
c = 0

for b in constantslist:
    def cmd(x = b):
        click(x)

    Button(constants,text = b, width = 22, command = cmd).grid(row = r, column = c)
    r = r + 1

#Functions#
functions = Frame(window)
functions.grid(row = 3, column = 1, sticky = W)
functionslist = [
'Factorial(!)',
'-> Roman',
'Decimal -> Binary',
'Binary -> Decimal']

r = 0
c = 0

for b in functionslist:
    def cmd(x = b):
        click(x)

    Button(functions,text = b, width = 13, command = cmd).grid(row = r, column = c)
    r = r + 1

def click(key):
    if key == "=":
        try:
            temp = str(display.get())
            resultchars = temp.split()

            for i in range(0,len(resultchars)):
                if (not(resultchars[i] == "+" or resultchars[i] == "-" or resultchars[i] == "/" or resultchars[i] == "*" or resultchars[i] == "(" or resultchars[i] == ")")):
                    resultchars[i] = float(resultchars[i])
                    
            temp = ""
            for i in range(0,len(resultchars)):
                temp = temp + str(resultchars[i])

            result = str(eval(temp))[0:10]
            display.delete(0, END)
            display.insert(END, "=" + result)
        except:
            display.insert(END, "--> Syntax Error")
    elif key == "c":
        display.delete(0, END)
    elif key == constantslist[0]:
        display.insert(END,"3.141592654")
    elif key == constantslist[1]:
        display.insert(END,"300000000")
    elif key == constantslist[2]:
        display.insert(END,"330")
    elif key == constantslist[3]:
        display.insert(END,"149597887.5")
    elif key == functionslist[0]:
        n = display.get()
        display.delete(0,END)
        display.insert(END,calc_functions.factorial(n))
    elif key == functionslist[1]:
        n = display.get()
        display.delete(0,END)
        display.insert(END,calc_functions.to_roman(n))
    elif key == functionslist[2]:
        n = display.get()
        display.delete(0,END)
        display.insert(END,calc_functions.to_binary(n))
    elif key == functionslist[3]:
        n = display.get()
        display.delete(0,END)
        display.insert(END,calc_functions.from_binary(n))
    else:
        display.insert(END,key)

#Mainloop#
window.mainloop()
