from tkinter import *
import first
from tkinter import messagebox


class RegisterClass:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Register")
        self.win.deiconify()

    def add_frame(self):
        self.frame = Frame(self.win)
        self.frame.place(x=50, y=50)

        self.labelUser = Label(self.frame, text="Name")
        self.labelUser.grid(row=0, column=0)

        self.username = Entry(self.frame)
        self.username.grid(row=0, column=1)

        self.labelEmail = Label(self.frame, text="Email")
        self.labelEmail.grid(row=1, column=0)

        self.userEmail = Entry(self.frame)
        self.userEmail.grid(row=1, column=1)

        self.labelNumber = Label(self.frame, text="Number")
        self.labelNumber.grid(row=2, column=0)

        self.usernum = Entry(self.frame)
        self.usernum.grid(row=2, column=1)

        self.labelPassword = Label(self.frame, text="Password")
        self.labelPassword.grid(row=3, column=0)

        self.userPass = Entry(self.frame, show='*')
        self.userPass.grid(row=3, column=1)

        self.buttonReg = Button(self.frame, text="Register", command=self.buttonreg)
        self.buttonReg.grid(row=4, column=1)

        self.button = Button(self.frame, text="Login", command=self.buttonclick)
        self.button.grid(row=5, column=1)

        self.win.mainloop()

    def buttonclick(self):
        self.win.destroy()
        reg = first.LoginClass()
        reg.add_frame()

    def buttonreg(self):
        self.user = self.username.get()
        self.passw = self.userPass.get()
        messagebox.showinfo("Message", self.user+ " User Added")


if __name__ == "__main__":
    r = RegisterClass()
    r.add_frame()