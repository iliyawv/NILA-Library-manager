from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# general attributes
pageStatus = 1


# color pallete
entfg = "#695f64"
entbg = "#e5e4e0"
cnvsbg = "#b0997d"
cnvshl = "#612601"
btnbg = "#daccbf"


root = Tk()

loginBG = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/libBG.png")

ico = Image.open(
    "C:/Users/GECKO/git-projects/Library management/media/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# root attributes
root.title("Library manager")
root.geometry("1200x800")
root.state('zoomed')
lblphoto = Label(root, image=loginBG,
                 width=root.winfo_screenwidth(), height=root.winfo_screenheight())
lblphoto.pack()


# decides which page to show
def pageDecider(value):
    if value == 1:
        loginPage()
        print(value)
    elif value == 2:
        firstMenu()
        print(value)


# login page and the first page of program
def loginPage():

    def login(e=""):
        username = entUsername.get()
        password = entPass.get()
        try:
            credential = open(
                f"C:/Users/GECKO/git-projects/Library management/{username}.txt", "r")
            if credential.read() != password:
                tkinter.messagebox.showwarning(
                    title="ERROR", message="credential is unmatched")
            else:
                global pageStatus
                pageStatus = 2
                canvas.destroy()
                firstMenu()

        except:
            tkinter.messagebox.showwarning(
                title="error", message="credential is wrong")

    canvas = Canvas(root, width=500, height=500,
                    bg=cnvsbg, highlightthickness=2, highlightbackground=cnvshl)
    canvas.place(relx=.5, rely=.5, anchor=CENTER)

    loginLabel = Label(canvas, text="Login", font=(
        "Helvetica Rounded", 30), bg=cnvsbg)
    loginLabel.place(relx=.5, rely=.15, anchor=CENTER)

    lbluser = Label(canvas, text="username", font=(
        "Helvetica Oblique", 11), bg=cnvsbg)
    lbluser.place(relx=.262, rely=.323, anchor=CENTER)

    lblpass = Label(canvas, text="password", font=(
        "Helvetica Oblique", 11), bg=cnvsbg)
    lblpass.place(relx=.262, rely=.445, anchor=CENTER)

    entryFont = ("Helvetica Rounded", 18)
    entUsername = Entry(canvas, font=entryFont, bg=entbg, fg=entfg)
    entUsername.place(relx=.5, rely=.38, anchor=CENTER)
    entPass = Entry(canvas, font=entryFont, bg=entbg, fg=entfg)
    entPass.place(relx=.5, rely=.5, anchor=CENTER)

    btnLogin = Button(canvas, bg=btnbg, text="Login",
                      font=("Helvetica Rounded", 14), command=login, width=11)
    btnLogin.place(relx=.5, rely=.64, anchor=CENTER)

    entPass.bind("<Return>",  login)


# main menu
def firstMenu():
    canvas2 = Canvas(root, width=1000, height=800,
                     bg=cnvsbg, highlightthickness=0, highlightbackground=cnvshl)
    canvas2.place(relx=.5, rely=.5, anchor=CENTER)

    btnUsers = Button(canvas2, bg=btnbg, text="USERS",
                      font=("Helvetica Rounded", 34,), width=20)
    btnUsers.place(relx=.5, rely=.3, anchor=CENTER)

    btnBooks = Button(canvas2, bg=btnbg, text="BOOKS",
                      font=("Helvetica Rounded", 34), width=20)
    btnBooks.place(relx=.5, rely=.5, anchor=CENTER)

    btnIssue = Button(canvas2, bg=btnbg, text="ISSUE A BOOK",
                      font=("Helvetica Rounded", 34), width=20)
    btnIssue.place(relx=.5, rely=.7, anchor=CENTER)


pageDecider(pageStatus)
root.mainloop()
