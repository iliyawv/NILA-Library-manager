from tkinter import *
import tkinter.messagebox
pageStatus = 1
root = Tk()
loginBG = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/libBG.png")
# general att
root.title("Library manager")
root.geometry("1200x800")
root.state('zoomed')
lblphoto = Label(root, image=loginBG,
                 width=root.winfo_screenwidth(), height=root.winfo_screenheight())
lblphoto.pack()


def pageDecider(value):
    if value == 1:
        loginPage()
        print(value)
    elif value == 2:
        firstMenu()
        print(value)


def loginPage():

    def login():
        username = entUsername.get()
        password = entPass.get()
        try:
            credential = open(
                f"C:/Users/GECKO/git-projects/Library management/{username}.txt", "r")
            if credential.read() != password:
                tkinter.messagebox.showwarning(
                    title="error", message="credential is wrong")
            else:
                global pageStatus
                pageStatus = 2
                canvas.destroy()
                firstMenu()

        except:
            tkinter.messagebox.showwarning(
                title="error", message="credential is wrong")

    canvas = Canvas(root, width=500, height=500,
                    bg="#b0997d", highlightthickness=2, highlightbackground="#612601")
    canvas.place(relx=.5, rely=.5, anchor=CENTER)

    loginLabel = Label(canvas, text="Login", font=(
        "Helvetica Rounded", 30), bg="#b0997d")
    loginLabel.place(relx=.5, rely=.15, anchor=CENTER)

    lbluser = Label(canvas, text="username", font=(
        "Helvetica Oblique", 11), bg="#b0997d")
    lbluser.place(relx=.262, rely=.323, anchor=CENTER)

    lblpass = Label(canvas, text="password", font=(
        "Helvetica Oblique", 11), bg="#b0997d")
    lblpass.place(relx=.262, rely=.445, anchor=CENTER)

    entryFont = ("Helvetica Rounded", 18)
    entUsername = Entry(canvas, font=entryFont, bg="#e7f0ef", fg="#695f64")
    entUsername.place(relx=.5, rely=.38, anchor=CENTER)
    entPass = Entry(canvas, font=entryFont, bg="#e7f0ef", fg="#695f64")
    entPass.place(relx=.5, rely=.5, anchor=CENTER)

    btnLogin = Button(canvas, bg='#daccbf', text="Login",
                      font=("Helvetica Rounded", 14), command=login, width=11)
    btnLogin.place(relx=.5, rely=.64, anchor=CENTER)


def firstMenu():
    canvas2 = Canvas(root, width=1000, height=800,
                     bg="#b0997d", highlightthickness=0, highlightbackground="#559364")
    canvas2.place(relx=.5, rely=.5, anchor=CENTER)

    btnUsers = Button(canvas2, bg='#daccbf', text="USERS",
                      font=("Helvetica Rounded", 34,), width=20)
    btnUsers.place(relx=.5, rely=.3, anchor=CENTER)

    btnUsers = Button(canvas2, bg='#daccbf', text="BOOKS",
                      font=("Helvetica Rounded", 34), width=20)
    btnUsers.place(relx=.5, rely=.5, anchor=CENTER)

    btnUsers = Button(canvas2, bg='#daccbf', text="BORROW/LEND",
                      font=("Helvetica Rounded", 34), width=20)
    btnUsers.place(relx=.5, rely=.7, anchor=CENTER)


pageDecider(pageStatus)
root.mainloop()
