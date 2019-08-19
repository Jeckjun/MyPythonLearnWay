from tkinter import *

win = Tk()
win.title('简易计算器')
win.geometry("220x350+500+100") # 500+100代表left 500，top 100
def hello():
    print('点击菜单')
menu = Menu(win)
for item in ['标准', '科学', '程序员']:
    menu.add_command(label = item, command = hello)
win['menu'] = menu

def calculator():
    return 
vartext = win.StringVar()
cuncu = []


btn1 = Button(win, text = '1', width = 6, height = 2, bg = 'yellow')
btn2 = Button(win, text = '2', width = 6, height = 2, bg = 'yellow')
btn3 = Button(win, text = '3', width = 6, height = 2, bg = 'yellow')
btn4 = Button(win, text = '4', width = 5, height = 2, bg = 'yellow')
btn5 = Button(win, text = '5', width = 5, height = 2, bg = 'yellow')
btn6 = Button(win, text = '6', width = 5, height = 2, bg = 'yellow')
btn7 = Button(win, text = '7', width = 5, height = 2, bg = 'yellow')
btn8 = Button(win, text = '8', width = 5, height = 2, bg = 'yellow')
btn9 = Button(win, text = '9', width = 5, height = 2, bg = 'yellow')
btn0 = Button(win, text = '0', width = 5, height = 2, bg = 'yellow')
btnP = Button(win, text = '.', width = 5, height = 2, bg = 'green')
txt = Label(win, width = 20, height = 2, anchor='se', textvariable = vartext, justify = 'right', bg = 'white')
btnCE = Button(win, text = 'CE', width = 5, height = 2, bg = 'yellow')
btnC = Button(win, text = 'C',  width = 5, height = 2, bg = 'yellow')
btnDel = Button(win, text = 'DEL', width = 5, height = 2, bg = 'yellow')
btnEq = Button(win, text = '=', width = 6, height = 2, bg = 'red')
btnAdd = Button(win, text = '+', width = 5, height = 2, bg = 'red')
btnRed = Button(win, text = '-', width = 5, height = 2, bg = 'red')
btnMul = Button(win, text = 'x', width = 5, height = 2, bg = 'red')
btnDiv = Button(win, text = '÷', width = 5, height = 2, bg = 'red')
btn1.grid(row = 4, column = 0, sticky = E + W)
btn2.grid(row = 4, column = 1, sticky = E + W)
btn3.grid(row = 4, column = 2, sticky = E + W)
btn4.grid(row = 3, column = 0, sticky = E + W)
btn5.grid(row = 3, column = 1, sticky = E + W)
btn6.grid(row = 3, column = 2, sticky = E + W)
btn7.grid(row = 2, column = 0, sticky = E + W)
btn8.grid(row = 2, column = 1, sticky = E + W)
btn9.grid(row = 2, column = 2, sticky = E + W)
btn0.grid(row = 5, column = 0, columnspan = 2, sticky = E + W)
btnP.grid(row = 5, column = 2, sticky = E + W)
btnCE.grid(row = 1, column = 0, sticky = E + W)
btnC.grid(row = 1, column = 1, sticky = E + W)
btnDel.grid(row = 1, column = 2, sticky = E + W)
txt.grid(row = 0,column = 0, columnspan = 4, sticky = E + W)
btnEq.grid(row = 5,column = 3, sticky = E + W)
btnAdd.grid(row = 4,column = 3, sticky = E + W)
btnRed.grid(row = 3,column = 3, sticky = E + W)
btnMul.grid(row = 2,column = 3, sticky = E + W)
btnDiv.grid(row = 1,column = 3, sticky = E + W)

win.mainloop()