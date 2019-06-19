from tkinter import *
from tkinter import messagebox
import second


class LoginClass:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Login")
        self.win.deiconify()

    def add_frame(self):
        self.frame = Frame(self.win)
        self.frame.place(x=50, y=50)

        self.labelUser = Label(self.frame, text="Username")
        self.labelUser.grid(row=0, column=0)

        self.username = Entry(self.frame)
        self.username.grid(row=0, column=1)

        self.labelPassword = Label(self.frame, text="Password")
        self.labelPassword.grid(row=1, column=0)

        self.userPass = Entry(self.frame, show='*')
        self.userPass.grid(row=1, column=1)

        self.button = Button(self.frame, text="Login", command=self.buttonclick)
        self.button.grid(row=2, column=1)

        self.buttonReg = Button(self.frame, text="Register", command=self.buttonreg)
        self.buttonReg.grid(row=3, column=1)

        self.win.mainloop()

    def buttonclick(self):
        messagebox.showinfo("Message", "Login Successfully")

    def buttonreg(self):
        self.win.destroy()
        reg = second.RegisterClass()


if __name__ == "__main__":
    x = LoginClass()
    x.add_frame()
