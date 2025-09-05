from tkinter import *
import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
root = Tk()
root.title("Calculator")
e = Entry(root, width=35, borderwidth=9)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def add_button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def add_dot():
    dotcurrent = e.get()
    e.delete(0, END)
    if "." not in dotcurrent:
        e.insert(0, str(dotcurrent + "."))
def clear_number():
    e.delete(0, END)
def operation(op):
    global f_num, math
    f_num = float(e.get())
    math = op
    e.delete(0, END)
def button_equal():
    global f_num, math
    try:
        second_number = float(e.get())
        e.delete(0, END)
        if math in ops:
            if math == "/" and second_number == 0:
                e.insert(0, "Error: Div by 0")
            else:
                result = ops[math](f_num, second_number)
                
                if result == int(result):
                    e.insert(0, int(result))
                else:
                    e.insert(0, round(result, 8)) 
       
   
        math = None  
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input")
    except NameError: # يحدث إذا لم يتم تعيين 'math' بعد (مثل الضغط على = أولاً)
        e.delete(0, END)
        e.insert(0, "Error")

b1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_button(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_button(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_button(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_button(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_button(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_button(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_button(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_button(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_button(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_button(0))
bplus = Button(root, text="+", padx=40, pady=20, command=lambda: operation("+"))
bminus = Button(root, text="-", padx=40, pady=20, command=lambda: operation("-"))
bmul = Button(root, text="*", padx=40, pady=20, command=lambda: operation("*"))
bdiv = Button(root, text="/", padx=40, pady=20, command=lambda: operation("/"))
bequal = Button(root, text="=", padx=40, pady=20, command=lambda: button_equal())
beclear = Button(root, text="clear", padx=40, pady=20, command=lambda: clear_number())
bdot = Button(root, text=".", padx=40, pady=20, command=lambda: add_dot())
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b0.grid(row=4, column=0)
bplus.grid(row=4, column=1)
bminus.grid(row=4, column=2)
bmul.grid(row=5, column=0)
bdiv.grid(row=5, column=1)
bequal.grid(row=5, column=2)
beclear.grid(row=7, column=1)
bdot.grid(row=7, column=2)



root.mainloop()