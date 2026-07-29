from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("350x500")

entry = Entry(window,width=20,font =("Arial",20), bd= 4)
entry.grid(row = 0,column = 0,columnspan = 4, padx= 10, pady = 10)

def click(value):
    entry.insert(END,value)
def clear():
    entry.delete(0,END)
def delete():
    text = entry.get()
    entry.delete(0,END)
    entry.insert(0,text[:-1])
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,result)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")
button7 = Button(window,text = "7",width = 5,height = 2,command = lambda:click("7"))
button7.grid(row = 2 ,column = 0,padx = 10, pady = 10)
button4 = Button(window,text = "4",width = 5,height = 2,command = lambda:click("4"))
button4.grid(row = 3 ,column = 0,padx = 10,pady = 10)
button1 = Button(window,text = "1",width = 5,height = 2,command = lambda:click("1"))
button1.grid(row = 4 ,column = 0,padx = 10,pady = 10)
button00 = Button(window,text = "00",width = 5,height = 2,command = lambda:click("00"))
button00.grid(row = 5 ,column = 0,padx = 10,pady = 10)


button8 = Button(window,text = "8",width = 5,height = 2,command = lambda:click("8"))
button8.grid(row = 2 ,column = 1,padx = 10,pady = 10)
button5 = Button(window,text = "5",width = 5,height = 2,command = lambda:click("5"))
button5.grid(row = 3 ,column = 1,padx = 10,pady = 10)
button2 = Button(window,text = "2",width = 5,height = 2,command = lambda:click("2"))
button2.grid(row = 4 ,column = 1,padx = 10,pady = 10)
button0 = Button(window,text = "0",width = 5,height = 2,command = lambda:click("0"))
button0.grid(row = 5 ,column = 1,padx = 10,pady = 10)


button9 = Button(window,text = "9",width = 5,height = 2,command = lambda:click("9"))
button9.grid(row = 2 ,column = 2,padx = 10, pady = 10)
button6 = Button(window,text = "6",width = 5,height = 2,command = lambda:click("6"))
button6.grid(row = 3,column = 2,padx = 10, pady = 10)
button3 = Button(window,text = "3",width = 5,height = 2,command =lambda:click("3"))
button3.grid(row = 4 ,column = 2,padx = 10, pady = 10)
button_Dot = Button(window,text = ".",width = 5,height = 2,command=lambda:click("."))
button_Dot.grid(row = 5 ,column = 2,padx = 10, pady = 10)

button_clear = Button(window,text = "C",width = 5,height = 2,command = clear)
button_clear.grid(row = 1 ,column = 0,padx = 10,pady = 10)

button_delete = Button(window,text = "x",width = 5, height = 2,command =delete)
button_delete.grid(row=5,column = 3,padx = 10,pady = 10)

button_multiply = Button(window,text = "*",width = 5, height = 2,command =lambda: click("*"))
button_multiply.grid(row=1,column = 3,padx = 10,pady = 10)

button_plus = Button(window,text = "+",width = 5, height = 2,command =lambda: click("+"))
button_plus.grid(row=2,column = 3,padx = 10,pady = 10)

button_subract = Button(window,text = "-",width = 5, height = 2,command =lambda: click("-"))
button_subract.grid(row=3,column = 3,padx = 10,pady = 10) 

button_divide = Button(window,text = "/",width = 5,height = 2,command =lambda: click("/"))
button_divide.grid(row = 1 ,column = 2,padx = 10, pady = 10)

button_remainder = Button(window,text = "%",width = 5,height = 2,command =lambda: click("%"))
button_remainder.grid(row = 1 ,column = 1,padx= 10,pady = 10)

button_equal = Button(window,text = "=",width = 5, height = 2,command =equal)
button_equal.grid(row=4,column = 3,padx = 10,pady = 10)

window.mainloop()