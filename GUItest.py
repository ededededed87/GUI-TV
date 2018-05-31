import tkinter

top = tkinter.Tk()

e = tkinter.Entry(top, width = 30)
e.place(x = 5, y = 50)

f = tkinter.Entry(top, width = 30)
f.place(x = 5, y = 25)


a = e.get()
b = f.get()



def add():
    a = int(e.get())
    b = int(f.get())
    print(a + b)


w = tkinter.Button(top, command = add, text = "Add")
w.place(x = 5, y = 100)




top.mainloop()
