from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
# general attributes
pageStatus = 2
isHidden = True

# color pallete
entfg = "#695f64"
entbg = "#e5e4e0"
cnvsbg = "#b0997d"
cnvshl = "#612601"
btnbg = "#daccbf"


root = Tk()

# media
loginBG = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/libBG.png")

ico = Image.open(
    "C:/Users/GECKO/git-projects/Library management/media/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

viewIcon = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/view.png")
hiddenIcon = PhotoImage(
    file="C:/Users/GECKO/git-projects/Library management/media/hidden.png")

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

    def showSHIcon(e=""):

        def showChar():
            global isHidden
            if isHidden == False:
                entPass.config(show="*")
                isHidden = True
                btnShowPass.config(image=viewIcon)
            else:
                entPass.config(show="")
                isHidden = False
                btnShowPass.config(image=hiddenIcon)
        global btnShowPass

        btnShowPass = Button(canvas,
                             width=25, height=25, command=showChar)
        btnShowPass.place(relx=.77, rely=.65, anchor=CENTER)

        if isHidden == False:
            btnShowPass.config(image=hiddenIcon)
        else:
            btnShowPass.config(image=viewIcon)

    def hideSHIcon(e=""):
        btnShowPass.destroy()

    canvas = Canvas(root, width=500, height=350,
                    bg=cnvsbg, highlightthickness=2, highlightbackground=cnvshl)
    canvas.place(relx=.5, rely=.5, anchor=CENTER)

    loginLabel = Label(canvas, text="Login", font=(
        "Helvetica Rounded", 30), bg=cnvsbg)
    loginLabel.place(relx=.5, rely=.15, anchor=CENTER)

    lbluser = Label(canvas, text="username", font=(
        "Helvetica Oblique", 11), bg=cnvsbg)
    lbluser.place(relx=.262, rely=.37, anchor=CENTER)

    lblpass = Label(canvas, text="password", font=(
        "Helvetica Oblique", 11), bg=cnvsbg)
    lblpass.place(relx=.262, rely=.57, anchor=CENTER)

    entryFont = ("Helvetica Rounded", 18)
    entUsername = Entry(canvas, font=entryFont, bg=entbg, fg=entfg)
    entUsername.place(relx=.5, rely=.45, anchor=CENTER)
    entPass = Entry(canvas, show="*", font=entryFont, bg=entbg, fg=entfg)
    entPass.place(relx=.5, rely=.65, anchor=CENTER)

    btnLogin = Button(canvas, bg=btnbg, text="Login",
                      font=("Helvetica Rounded", 14), command=login, width=11)
    btnLogin.place(relx=.5, rely=.85, anchor=CENTER)

    entPass.bind("<Return>",  login)
    entPass.bind("<FocusIn>", showSHIcon)
    entPass.bind("<FocusOut>", hideSHIcon)


# main menu
def firstMenu():
    canvas2 = Canvas(root, width=700, height=500,
                     bg=cnvsbg, highlightthickness=0, highlightbackground=cnvshl)
    canvas2.place(relx=.5, rely=.5, anchor=CENTER)

    def openUsers():
        global pageStatus
        pageStatus = 3
        canvas2.destroy()
        canvas3 = Canvas(root, width=1200, height=800, bg=cnvsbg,
                         highlightthickness=2, highlightbackground=cnvshl)
        canvas3.place(relx=.5, rely=.5, anchor=CENTER)

        treeUsers = ttk.Treeview(canvas3)
        treeUsers["columns"] = ("ID", "Name", "Last Name",
                                "Phone Number", "Reg Date")

        treeUsers.column("#0", width=NO, minwidth=NO)
        treeUsers.column("ID", anchor=CENTER, width=80, minwidth=60)
        treeUsers.column("Name", anchor=W, width=160, minwidth=100)
        treeUsers.column("Last Name", anchor=W, width=160, minwidth=100)
        treeUsers.column("Phone Number", anchor=W, width=160, minwidth=100)
        treeUsers.column("Reg Date", anchor=W, width=120, minwidth=80)

        treeUsers.heading("#0", text="", anchor=W)
        treeUsers.heading("ID", anchor=CENTER, text="ID")
        treeUsers.heading("Name", anchor=W, text="Name")
        treeUsers.heading("Last Name", anchor=W, text="Last Name")
        treeUsers.heading("Phone Number", anchor=W, text="Phone Number")
        treeUsers.heading("Reg Date", anchor=W, text="Reg Date")

        treeUsers.insert(parent="", index='end', iid=0, text="",
                         values=[1, "Ilia", "Valaei", "09307637377", "14-2-2023"])

        treeUsers.place(rely=.2, relx=.5, anchor=CENTER)

    btnUsers = Button(canvas2, bg=btnbg, text="USERS",
                      font=("Helvetica Rounded", 34,), width=20, command=openUsers)
    btnUsers.place(relx=.5, rely=.2, anchor=CENTER)

    btnBooks = Button(canvas2, bg=btnbg, text="BOOKS",
                      font=("Helvetica Rounded", 34), width=20)
    btnBooks.place(relx=.5, rely=.5, anchor=CENTER)

    btnIssue = Button(canvas2, bg=btnbg, text="ISSUE A BOOK",
                      font=("Helvetica Rounded", 34), width=20)
    btnIssue.place(relx=.5, rely=.8, anchor=CENTER)

# users menu


def usersMenu():
    usersDB = sqlite3.connect("user.db")
    cursor = usersDB.cursor()

    usersDB.commit()
    usersDB.close()


usersMenu()

pageDecider(pageStatus)
root.mainloop()
