from tkinter import *

calc_num1 = '0'
calc_num2 = ''
math_op = ''
equals_prior = False


def press_num_btn(num):
    global calc_num1
    global calc_num2
    global math_op
    if math_op == '':
        if calc_num1 == '0':
            calc_num1 = num
            num_display.config(text=calc_num1)
        else:
            calc_num1 = calc_num1 + num
            num_display.config(text=calc_num1)
    else:
        if calc_num2 == '0':
            calc_num2 = num
            num_display.config(text=calc_num2)
        else:
            calc_num2 = calc_num2 + num
            num_display.config(text=calc_num2)
    erase_button.config(text='C')

def toggle_button():
    if math_op == '/':
        divide_button.config(fg='#FF9912', bg='white', state=DISABLED)
        multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
        minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
        plus_button.config(fg='white', bg='#FF9912', state=NORMAL)
    elif math_op == '*':
        divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
        multiply_button.config(fg='#FF9912', bg='white', state=DISABLED)
        minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
        plus_button.config(fg='white', bg='#FF9912', state=NORMAL)
    elif math_op == '-':
        divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
        multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
        minus_button.config(fg='#FF9912', bg='white', state=DISABLED)
        plus_button.config(fg='white', bg='#FF9912', state=NORMAL)
    elif math_op == '+':
        divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
        multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
        minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
        plus_button.config(fg='#FF9912', bg='white', state=DISABLED)
    else:
        divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
        multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
        minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
        plus_button.config(fg='white', bg='#FF9912', state=NORMAL)


def press_divide():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if math_op != '' and calc_num2 != '' and not equals_prior:
        calc_num1 = str(eval(calc_num1 + math_op + calc_num2))
        num_display.config(text=calc_num1)
    calc_num2 = ''
    math_op = '/'
    equals_prior = False
    toggle_button()


def press_multiply():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if math_op != '' and calc_num2 != '' and not equals_prior:
        calc_num1 = str(eval(calc_num1 + math_op + calc_num2))
        num_display.config(text=calc_num1)
    calc_num2 = ''
    math_op = '*'
    equals_prior = False
    toggle_button()


def press_minus():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if math_op != '' and calc_num2 != '' and not equals_prior:
        calc_num1 = str(eval(calc_num1 + math_op + calc_num2))
        num_display.config(text=calc_num1)
    calc_num2 = ''
    math_op = '-'
    equals_prior = False
    toggle_button()


def press_comma():
    global calc_num1
    global calc_num2
    global math_op
    if num_display['text'] == calc_num1 and '.' not in calc_num1:
        calc_num1 = calc_num1 + '.'
        num_display.config(text=calc_num1)
    elif num_display['text'] == calc_num2 and '.' not in calc_num2:
        calc_num2 = calc_num2 + '.'
        num_display.config(text=calc_num2)
    erase_button.config(text='C')


def press_equals():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if calc_num1 != '' and calc_num2 != '' and math_op != '':
        calc_num1 = str(eval(calc_num1 + math_op + calc_num2))
        num_display.config(text=calc_num1)
    equals_prior = True
    divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
    multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
    minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
    plus_button.config(fg='white', bg='#FF9912', state=NORMAL)


def press_plus():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if math_op != '' and calc_num2 != '' and not equals_prior:
        calc_num1 = str(eval(calc_num1 + math_op + calc_num2))
        num_display.config(text=calc_num1)
    calc_num2 = ''
    math_op = '+'
    equals_prior = False
    toggle_button()


def press_erase():
    global calc_num1
    global calc_num2
    global math_op
    global equals_prior
    if erase_button['text'] == 'C':
        if num_display['text'] == calc_num1:
            calc_num1 = '0'
            num_display.config(text=calc_num1)
        else:
            calc_num2 = '0'
            num_display.config(text=calc_num2)
        erase_button.config(text='AC')
    else:
        calc_num1 = '0'
        calc_num2 = '0'
        math_op = ''
        equals_prior = False
        num_display.config(text=calc_num1)
        divide_button.config(fg='white', bg='#FF9912', state=NORMAL)
        multiply_button.config(fg='white', bg='#FF9912', state=NORMAL)
        minus_button.config(fg='white', bg='#FF9912', state=NORMAL)
        plus_button.config(fg='white', bg='#FF9912', state=NORMAL)


def press_neg():
    global calc_num1
    global calc_num2
    global math_op
    if num_display['text'] == calc_num1:
        if calc_num1[0] != '-':
            calc_num1 = '-' + calc_num1
        else:
            calc_num1 = calc_num1.lstrip('-')
        num_display.config(text=calc_num1)
    elif num_display['text'] == calc_num2:
        if calc_num2[0] != '-':
            calc_num2 = '-' + calc_num2
        else:
            calc_num2 = calc_num2.lstrip('-')
        num_display.config(text=calc_num2)


def press_percent():
    global calc_num1
    calc_num1 = str(eval(calc_num1) / 100)
    num_display.config(text=calc_num1)


root = Tk()
root.title('My Calculator')
root.config(bg='black')
root.minsize(215, 389)
root.maxsize(215, 389)
top_frame = Frame(root, )
top_frame.grid(row=0, columnspan=4)
num_display = Label(top_frame, bg='black', fg='white', text=calc_num1, font=10)
num_display.pack()
erase_button = Button(root, text='AC', fg='black', bg='#F5F5DC', height=4, width=6, bd='3', command=press_erase)
erase_button.grid(row=1, column=0)
Button(root, text='+/-', fg='black', bg='#F5F5DC', height=4, width=6, bd='3', command=press_neg).grid(row=1, column=1)
Button(root, text='%', fg='black', bg='#F5F5DC', height=4, width=6, bd='3', command=press_percent).grid(row=1, column=2)
divide_button = Button(root, text='/', fg='white', bg='#FF9912', height=4, width=6, bd='3', command=press_divide)
divide_button.grid(row=1, column=3)
Button(root, text='7', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(7)).grid(row=2, column=0)
Button(root, text='8', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(8)).grid(row=2, column=1)
Button(root, text='9', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(9)).grid(row=2, column=2)
multiply_button = Button(root, text='*', fg='white', bg='#FF9912', height=4, width=6, bd='3', command=press_multiply)
multiply_button.grid(row=2, column=3)
Button(root, text='4', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(4)).grid(row=3, column=0)
Button(root, text='5', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(5)).grid(row=3, column=1)
Button(root, text='6', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(6)).grid(row=3, column=2)
minus_button = Button(root, text='-', fg='white', bg='#FF9912', height=4, width=6, bd='3', command=press_minus)
minus_button.grid(row=3, column=3)
Button(root, text='1', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(1)).grid(row=4, column=0)
Button(root, text='2', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(2)).grid(row=4, column=1)
Button(root, text='3', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_num_btn(3)).grid(row=4, column=2)
plus_button = Button(root, text='+', fg='white', bg='#FF9912', height=4, width=6, bd='3', command=press_plus)
plus_button.grid(row=4, column=3)
Button(root, text='0', fg='white', bg='#4D4D4D', height=4, width=13, bd='3', command=press_num_btn(0)).grid(row=5, columnspan=2)
Button(root, text=',', fg='white', bg='#4D4D4D', height=4, width=6, bd='3', command=press_comma).grid(row=5, column=2)
Button(root, text='=', fg='white', bg='#FF9912', height=4, width=6, bd='3', command=press_equals).grid(row=5, column=3)

root.mainloop()
