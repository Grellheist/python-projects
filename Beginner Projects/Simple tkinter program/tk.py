from tkinter import *


def click():
    info = entry.get()
    if len(info) != 0:
        print(f'You just typed "{info}".')
        print('You should not say stuff like that.')
    else:
        print('You should not have done that.')


def delete():
    entry.delete(0,END)


def backspace():
    entry.delete(len(entry.get())-1,END)


def display():
    if(x.get()==1):
        print('Thank you :)')
    else:
        print('But why tho')


window = Tk()
window.geometry('800x800')
window.title('Kapimba')
window.config(background='black')
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
label = Label(window,
              text='Hello World!',
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='#000000',
              bd=10,
              padx=20,
              pady=20,
              image=icon,
              compound='top')
label.pack()
entry = Entry(window,
              font=('Arial', 30))
entry.pack(side=TOP)
submit_button = Button(window,
                text='Submit',
                command=click,
                font=('Arial', 15),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black')
delete_button = Button(window,
                text='Delete',
                command=delete,
                font=('Arial', 15),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black')
backspace = Button(window,
                text='Backspace',
                command=backspace,
                font=('Arial', 15),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black')
submit_button.pack()
delete_button.pack()
backspace.pack()

x = IntVar()
check_button = Checkbutton(window,
                           text='Click here to sell your soul',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='#000000',
                           activeforeground='#00FF00',
                           activebackground='#000000')

check_button.pack()

window.mainloop()
