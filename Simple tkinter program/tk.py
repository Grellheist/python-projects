from tkinter import *


def click():
    print('You should not have done that.')

window = Tk()
window.geometry('420x420')
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
button = Button(window,
                text='Click me!',
                command=click,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black')
button.pack()


window.mainloop()
