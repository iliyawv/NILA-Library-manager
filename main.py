from tkinter import *
import tkinter.messagebox
pageStatus = 1
root = Tk()
loginBG = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/loginBG.png")
# general att
root.title("Library manager")
root.geometry("1200x800")
root.state('zoomed')


def pageDecider(value):
    if value == 1:
        loginPage()
    elif value == 2:
        firstMenu()


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

        except:
            tkinter.messagebox.showwarning(
                title="error", message="credential is wrong")

    root.config(bg="#559364")
    lblphoto = Label(root, image=loginBG,
                     width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    lblphoto.pack()
    canvas = Canvas(root, width=500, height=500,
                    bg="#AEC09A", highlightthickness=0, highlightbackground="#559364")
    canvas.place(relx=.5, rely=.5, anchor=CENTER)

    loginLabel = Label(canvas, text="Login", font=(
        "Helvetica Rounded", 30), bg="#AEC09A")
    loginLabel.place(relx=.5, rely=.15, anchor=CENTER)

    lbluser = Label(canvas, text="username", font=(
        "Helvetica Oblique", 11), bg="#AEC09A")
    lbluser.place(relx=.262, rely=.323, anchor=CENTER)

    lblpass = Label(canvas, text="password", font=(
        "Helvetica Oblique", 11), bg="#AEC09A")
    lblpass.place(relx=.262, rely=.445, anchor=CENTER)

    entryFont = ("Helvetica Rounded", 18)
    entUsername = Entry(canvas, font=entryFont, bg="#e7f0ef", fg="#559364")
    entUsername.place(relx=.5, rely=.38, anchor=CENTER)
    entPass = Entry(canvas, font=entryFont, bg="#e7f0ef", fg="#559364")
    entPass.place(relx=.5, rely=.5, anchor=CENTER)

    btnLogin = Button(canvas, bg='#559364', text="Login",
                      font=entryFont, command=login)
    btnLogin.place(relx=.5, rely=.7, anchor=CENTER)


def firstMenu():
    canvas = Canvas(root, width=1000, height=800,
                    bg="#AEC09A", highlightthickness=0, highlightbackground="#559364")
    canvas.place(relx=.5, rely=.5, anchor=CENTER)


pageDecider(pageStatus)
root.mainloop()
