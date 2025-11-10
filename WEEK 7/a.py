from tkinter import*
buonia = Tk()
buonia.geometry("300x300")
buonia.title("Sum")

label_a = Label(text="Input number a:")
label_a.place(x=20, y=30, width=100, height=25)
entry_a = Entry()
entry_a.place(x=150, y=30, width=100, height=25)

label_b = Label(text="Input number b:")
label_b.place(x=20, y=70, width=100, height=25)
entry_b = Entry()
entry_b.place(x=150, y=70, width=100, height=25)

label_Eq = Label(text="Eq=")
label_Eq.place(x=20, y=120, width=100, height=25)

def click_to_DO(): 
    a = int(entry_a.get())
    print(a)
    b = int(entry_b.get())
    print(b)
    print("sum", a+b)
    output= Message(text= f'{a+b}')
    output.place(x=70, y=120, width=100, height=25)

def exitt():
    exit()
click_button=Button(text="Click to do", command=click_to_DO)
click_button.place(x=150, y=200, width=100, height=25)
exit_button = Button(text="Exit", command=exitt)
exit_button.place(x=50, y=200, width=80, height=25)

buonia.mainloop()