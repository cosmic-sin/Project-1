from tkinter import *
window = Tk()
expression = StringVar()
window.geometry("350x360")
Caltitle = Label(window,text="  o.O  CALCULATOR  o_O  ",fg="purple",font=("Times New Roman",20),bg="#E7DDFF")
Caltitle.grid(row=0,column=0,columnspan=4)
CalEntry = Entry(window,font=("Arial",18),textvariable=expression,fg="#B72776")
CalEntry.grid(row=1,column=0,columnspan=4,sticky="ew",padx=10,pady=10)

def clickbtn(value):
     
    current_exp = expression.get()
    if  len(current_exp) == 0 and value == "0":
        pass
    else:
        new_expression = ""
        if current_exp == "" or current_exp[-1].isalnum():
            new_expression = current_exp + value
            
        elif not current_exp[-1].isalnum() and  not value.isalnum():
            new_expression = current_exp[:-1] + value
        else:
            new_expression = current_exp + value


        expression.set(new_expression)
    # if current_exp == "0":
        # expression.set(value)
        # CalEntry.delete(0, END)
    # elif current_exp == "+" or current_exp == "-" or current_exp == "*" or current_exp == "/" or current_exp == "%"  :
        # expression.set(value)
    # else:
        #CalEntry.insert(0,"HELLO")
        #  expression.set(current_exp + str(value))
    # if current_exp == :
    #     expression.set()
    
def clear():
    expression.set("")

def equal():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("MATH ERROR")

def undo():
    current_val=expression.get()
    if len(current_val) >= 0:
        expression.set(current_val[:-1])

# def zero():
#     current_zero = expression.get()

#     if len(current_zero)==1:
#             expression.set("0")

#     elif len(current_zero) >1:
#         expression.set(current_zero+"0")   
#     else:
#          expression.set(current_zero +"0")
    

num1 = Button(window,text="1",padx=30,pady=10,command=lambda:clickbtn("1"),bg="#5DE2E7",font=("Bold",12))
num2 = Button(window,text="2",padx=35,pady=10,command=lambda:clickbtn("2"),bg="#5DE2E7",font=("Bold",12))
num3 = Button(window,text="3",padx=30,pady=10,command=lambda:clickbtn("3"),bg="#5DE2E7",font=("bold",12))
num4 = Button(window,text="4",padx=30,pady=10,command=lambda:clickbtn("4"),bg="#5DE2E7",font=("bold",12))
num5 = Button(window,text="5",padx=35,pady=10,command=lambda:clickbtn("5"),bg="#5DE2E7",font=("bold",12))
num6 = Button(window,text="6",padx=30,pady=10,command=lambda:clickbtn("6"),bg="#5DE2E7",font=("bold",12))
num7 = Button(window,text="7",padx=30,pady=10,command=lambda:clickbtn("7"),bg="#5DE2E7",font=("bold",12))
num8 = Button(window,text="8",padx=35,pady=10,command=lambda:clickbtn("8"),bg="#5DE2E7",font=("bold",12))
num9 = Button(window,text="9",padx=30,pady=10,command=lambda:clickbtn("9"),bg="#5DE2E7",font=("bold",12))

num0 = Button(window,text="0",padx=30,pady=10,command=lambda:clickbtn("0"),bg="#5DE2E7",font=("bold",12)).grid(row=5, column=0)


dot = Button(window,text=".",padx=37,pady=10,command=lambda:clickbtn("."),bg="#5DE2E7",font=("bold",12))
percent = Button(window,text="%",padx=30,pady=10,command=lambda:clickbtn("%"),bg="#5DE2E7",font=("bold",12)) 


add_tab = Button(window,text="+",padx=30,pady=34,command=lambda:clickbtn("+"),bg="#5DE2E7",font=("bold",12))
equal_tab = Button(window,text="=",padx=30,pady=10,command=equal,bg="#5DE2E7",font=("bold",12))
clear_tab = Button(window,text="C",padx=35,pady=10,command=clear,bg="#5DE2E7",font=("bold",12))

sub_tab = Button(window,text="-",padx=30,pady=10,command=lambda:clickbtn("-"),bg="#5DE2E7",font=("bold",12))
mul_tab = Button(window,text="*",padx=30,pady=10,command=lambda:clickbtn("*"),bg="#5DE2E7",font=("bold",12))
div_tab = Button(window,text="/",padx=30,pady=10,command=lambda:clickbtn("/"),bg="#5DE2E7",font=("bold",12))

undo_tab = Button(window,text="<x",padx=28,pady=10,command=undo,bg="#5DE2E7",font=("bold",12))

num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
add_tab.grid(row=2, column=3,rowspan=2)

num4.grid(row=3, column=0)
num5.grid(row=3, column=1)
num6.grid(row=3, column=2)
sub_tab.grid(row=4, column=3)

num1.grid(row=4, column=0)
num2.grid(row=4, column=1)
num3.grid(row=4, column=2)
mul_tab.grid(row=5, column=3)

clear_tab.grid(row=5, column=1)
equal_tab.grid(row=5, column=2)
div_tab.grid(row=6, column=3)

undo_tab.grid(row=6, column=0)
dot.grid(row=6, column=1)
percent.grid(row=6,column=2)

window.mainloop()