from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
import pandas as pd
import random
import datetime as dt
# general attributes
pageStatus = 4
isHidden = True
dbsort = "NONE"

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
    elif value == 3:
        usersMenu()
    elif value == 4:
        booksMenu()


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
                     bg=cnvsbg, highlightthickness=2, highlightbackground=cnvshl)
    canvas2.place(relx=.5, rely=.5, anchor=CENTER)
    global openUsers

    def openUsers():
        BtnLogout.destroy()
        global pageStatus
        pageStatus = 3
        canvas2.destroy()
        usersMenu()

    def openBooks():
        BtnLogout.destroy()
        global pageStatus
        pageStatus = 4
        canvas2.destroy()
        booksMenu()

    def logout():
        boolLogout = tkinter.messagebox.askyesno(
            title="Log Out", message="Do You want to logout")
        if boolLogout == True:
            BtnLogout.destroy()
            canvas2.destroy()
            loginPage()
            global pageStatus
            pageStatus = 1

    BtnLogout = Button(root, text="Log Out",
                       bg=btnbg, font=("Helvetica Rounded", 12), command=logout)
    BtnLogout.place(relx=.05, rely=.05, anchor=CENTER)

    btnUsers = Button(canvas2, bg=btnbg, text="USERS",
                      font=("Helvetica Rounded", 34,), width=20, command=openUsers)
    btnUsers.place(relx=.5, rely=.2, anchor=CENTER)

    btnBooks = Button(canvas2, bg=btnbg, text="BOOKS",
                      font=("Helvetica Rounded", 34), width=20, command=openBooks)
    btnBooks.place(relx=.5, rely=.5, anchor=CENTER)

    btnIssue = Button(canvas2, bg=btnbg, text="ISSUE A BOOK",
                      font=("Helvetica Rounded", 34), width=20)
    btnIssue.place(relx=.5, rely=.8, anchor=CENTER)

# users menu


def usersMenu():
    canvas3 = Canvas(root, width=1200, height=800, bg=cnvsbg,
                     highlightthickness=2, highlightbackground=cnvshl)
    canvas3.place(relx=.5, rely=.5, anchor=CENTER)

    def backToMenu():
        BtnBackMenu.destroy()
        canvas3.destroy()
        firstMenu()
        global pageStatus
        pageStatus = 2

    BtnBackMenu = Button(root, text="BACK",
                         bg=btnbg, font=("Helvetica Rounded", 12), command=backToMenu)
    BtnBackMenu.place(relx=.05, rely=.05, anchor=CENTER)

    def userList():
        global frmUsers
        frmUsers = LabelFrame(canvas3, text="USERS", bd=2,
                              bg=cnvsbg, width=1000, height=400, font=("Helvetica Rounded", 10))
        frmUsers.place(rely=.28, relx=.5, anchor=CENTER)
        scrlTree = Scrollbar(frmUsers)
        scrlTree.place(relx=.911, rely=.5, anchor=CENTER, relheight=.854)
        global treeBooks
        treeBooks = ttk.Treeview(frmUsers, height=15,
                                 yscrollcommand=scrlTree.set)
        treeBooks["columns"] = ("Membership ID", "First Name", "Last Name", "ID",
                                "Phone Number", "Reg Date")

        scrlTree.config(command=treeBooks.yview)

        treeBooks.column("#0", width=NO, minwidth=NO)
        treeBooks.column("Membership ID", anchor=CENTER,
                         width=120, minwidth=100)
        treeBooks.column("First Name", anchor=W, width=160, minwidth=100)
        treeBooks.column("Last Name", anchor=W, width=160, minwidth=100)
        treeBooks.column("ID", anchor=CENTER, width=80, minwidth=60)
        treeBooks.column("Phone Number", anchor=CENTER,
                         width=160, minwidth=100)
        treeBooks.column("Reg Date", anchor=CENTER, width=120, minwidth=80)

        treeBooks.heading("#0", text="", anchor=W)
        treeBooks.heading("Membership ID", anchor=CENTER, text="Membership ID")
        treeBooks.heading("First Name", anchor=W, text="First Name")
        treeBooks.heading("Last Name", anchor=W, text="Last Name")
        treeBooks.heading("ID", anchor=CENTER, text="ID")
        treeBooks.heading("Phone Number", anchor=CENTER, text="Phone Number")
        treeBooks.heading("Reg Date", anchor=CENTER, text="Reg Date")

        treeBooks.tag_configure("oddrow", background=entbg)
        treeBooks.tag_configure("evenrow", background=btnbg)

        iidCount = 0
        for record in dfUsers.values:

            if iidCount % 2 == 1:
                treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                 values=list(record), tags="oddrow")
            else:
                treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                 values=list(record), tag="evenrow")
            iidCount += 1

        treeBooks.place(rely=.5, relx=.5, anchor=CENTER)

        treeBooks.bind("<Double-1>", click)

    def userEdit():
        global frmEdit, entMemID, entName, entLName
        frmEdit = LabelFrame(canvas3, text="EDIT", bd=2,
                             bg=cnvsbg, width=1000, height=160, font=("Helvetica Rounded", 10))
        frmEdit.place(relx=.5, rely=.65, anchor=CENTER)
        lblMemID = Label(frmEdit, text="Name",
                         font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblMemID.place(relx=.2, rely=.21, anchor=CENTER)
        entMemID = Entry(frmEdit,
                         font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entMemID.place(relx=.2, rely=.4, anchor=CENTER)
        lblName = Label(frmEdit, text="Last Name",
                        font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblName.place(relx=.5, rely=.21, anchor=CENTER)

        entName = Entry(frmEdit,
                        font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entName.place(relx=.5, rely=.4, anchor=CENTER)
        lblLname = Label(frmEdit, text="Phone number",
                         font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblLname.place(relx=.8, rely=.21, anchor=CENTER)

        entLName = Entry(frmEdit,
                         font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entLName.place(relx=.8, rely=.4, anchor=CENTER)
        btnApply = Button(frmEdit, text="Apply",
                          bg=btnbg, font=("Helvetica Rounded", 12), command=applyChanges)
        btnApply.place(relx=.5, rely=.7, anchor=CENTER)

    def applyChanges():
        global entMemID, entName, entLName, id, dfUsers
        temp1 = entMemID.get()
        temp2 = entName.get()
        temp3 = entLName.get()
        if not (temp1 == "" or temp2 == "" or temp3 == ""):
            for record in dfUsers.values:
                if record[0] == id:
                    if tkinter.messagebox.askyesno(title="Apply", message="do you wish to proceed?") == True:
                        temp = record
                        temp[1] = temp1
                        temp[2] = temp2
                        temp[4] = temp3
                        dfUsers = dfUsers.replace(record, temp)
                        sort(dbsort)
                        break
            else:
                tkinter.messagebox.showerror(
                    title="ERROR", message="choose a user to edit!")
        else:
            tkinter.messagebox.showerror(
                title="ERROR", message="fields cant be empty")

        entLName.delete(0,  END)
        entName.delete(0,  END)
        entMemID.delete(0,  END)

    def deleteUser():
        global delValues, dfUsers
        selected = treeBooks.focus()
        delValues = treeBooks.item(selected, "values")

        for index, record in enumerate(dfUsers.values):
            if list(record) == list(delValues):
                if tkinter.messagebox.askyesno("DELETE", "do you want to proceed?") == True:
                    dfUsers.drop(index=index, inplace=True)
                    sort(dbsort)
                    dfUsers = pd.read_excel(
                        'C:/Users/GECKO/git-projects/Library management/db/user.xlsx', na_values="Missing", dtype=str)
                    dfUsers = dfUsers.fillna("Missing")
                    tkinter.messagebox.showinfo(
                        title="Successful", message=f"user {record[1]} {record[2]} removed!")
                    break
                else:
                    break
        else:
            tkinter.messagebox.showerror(
                title="ERROR", message="something wrong happened!")

    def UserAdd():
        global dfUsers

        addWindow = Toplevel(root, bg=cnvsbg, takefocus=True)
        addWindow.title("Add User")
        addWindow.geometry("800x280")
        addWindow.resizable(False, False)
        addWindow.wm_iconphoto(False, photo)

        def saveUser():
            global dfUsers
            if tkinter.messagebox.askyesno(title="SAVE", message="do you wish to proceed?") == True:
                id = entAddID.get()
                lastName = entAddLastName.get()
                Name = entAddName.get()
                phone = entAddPhone.get()
                memidList = set()

                memID = str(random.randint(100000, 999999))
                for record in dfUsers.values:
                    memidList.add(record[0])
                    if record[3] == id:
                        tkinter.messagebox.showerror(
                            title="ERROR", message=f"this user with ID:{id}, already exists!")
                        break
                else:
                    while (True):
                        memid = str(random.randint(100000, 999999))
                        if memid not in memidList:
                            newUserdf = pd.DataFrame({"Mem ID": [memID], "NAME": [Name], "LAST NAME": [lastName], "ID": [id],
                                                      "NUMBER": [phone], "DATE": [dt.datetime.now().strftime('%m/%d/%Y')]})
                            dfUsers = pd.concat(
                                [dfUsers, newUserdf], ignore_index=True)
                            sort(dbsort)
                            print(dfUsers)
                            break

        lblfrmAddUser = LabelFrame(
            addWindow, text="Add", width=700, height=200, font=("Helvetica Rounded", 10), bg=cnvsbg, bd=2)
        lblfrmAddUser.place(relx=.5, rely=.4, anchor=CENTER)

        entAddName = Entry(lblfrmAddUser,
                           font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entAddName.place(relx=.3, rely=.2, anchor=CENTER)

        lblAddName = Label(lblfrmAddUser, text="Name",
                           font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblAddName.place(relx=.07, rely=.2, anchor=CENTER)

        entAddLastName = Entry(lblfrmAddUser,
                               font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entAddLastName.place(relx=.3, rely=.45, anchor=CENTER)

        lblAddLastName = Label(lblfrmAddUser, text="Last Name",
                               font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblAddLastName.place(relx=.07, rely=.45, anchor=CENTER)

        entAddID = Entry(lblfrmAddUser,
                         font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entAddID.place(relx=.8, rely=.2, anchor=CENTER)

        lblAddID = Label(lblfrmAddUser, text="ID",
                         font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblAddID.place(relx=.55, rely=.2, anchor=CENTER)

        entAddPhone = Entry(lblfrmAddUser,
                            font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
        entAddPhone.place(relx=.8, rely=.45, anchor=CENTER)

        lblAddPhone = Label(lblfrmAddUser, text="Phone Number",
                            font=("Helvetica Rounded", 12), bg=cnvsbg)
        lblAddPhone.place(relx=.55, rely=.45, anchor=CENTER)

        btnSave = Button(lblfrmAddUser, text="Save",
                         bg=btnbg, font=("Helvetica Rounded", 12), command=saveUser)
        btnSave.place(relx=.5, rely=.85, anchor=CENTER)

        addWindow.grab_set()

    def click(e=""):

        global treeBooks, entMemID, entName, entLName, id, values
        selected = treeBooks.focus()
        values = treeBooks.item(selected, "values")
        entLName.delete(0,  END)
        entName.delete(0,  END)
        entMemID.delete(0,  END)
        entLName.insert(0,  values[4])
        entName.insert(0,  values[2])
        entMemID.insert(0,  values[1])
        id = values[0]

    global id
    id = 0
    frmUsersOption = LabelFrame(canvas3, text="OPTIONS", bd=2,
                                bg=cnvsbg, width=475, height=150, font=("Helvetica Rounded", 10))
    frmUsersOption.place(relx=.281, rely=.86, anchor=CENTER)
    # options
    btnAddUser = Button(frmUsersOption, text="Add",
                        bg=btnbg, font=("Helvetica Rounded", 12), command=UserAdd)
    btnAddUser.place(relx=.3, rely=.5, anchor=CENTER)

    btnDelUser = Button(frmUsersOption, text="Remove",
                        bg=btnbg, font=("Helvetica Rounded", 12), command=deleteUser)
    btnDelUser.place(relx=.7, rely=.5, anchor=CENTER)
    # options end

    frmSortUsers = LabelFrame(canvas3, text="SORT OPTIONS", bd=2,
                              bg=cnvsbg, width=475, height=150, font=("Helvetica Rounded", 10))
    frmSortUsers.place(relx=.719, rely=.86, anchor=CENTER)
    # sort options
    global dfUsers
    dfUsers = pd.read_excel(
        'C:/Users/GECKO/git-projects/Library management/db/user.xlsx', na_values="Missing", dtype=str)
    dfUsers = dfUsers.fillna("Missing")

    def sort(type):
        global dfUsers, id
        global dbsort
        dbsort = type
        if type == "Name":
            dfUsers = dfUsers.sort_values(by="NAME", ascending=True)
        elif type == "Last Name":
            dfUsers = dfUsers.sort_values(by="LAST NAME", ascending=True)
        elif type == "Membership ID":
            dfUsers = dfUsers.sort_values(by="Mem ID", ascending=True)
        elif type == "RegDate":
            dfUsers = dfUsers.sort_values(by="DATE", ascending=True)
        id = 0

        dfUsers.to_excel(
            excel_writer='C:/Users/GECKO/git-projects/Library management/db/user.xlsx', index=False, header=True)

        frmUsers.destroy()
        userList()

    userList()
    userEdit()

    global dbsort
    clicked = StringVar()
    clicked.set(dbsort)
    optmnSort = OptionMenu(frmSortUsers, clicked, "Name",
                           "Last Name",
                           "Membership ID",
                           "RegDate",)
    optmnSort.configure(bg=btnbg, highlightbackground=cnvsbg)
    optmnSort.place(relx=.55, rely=.3, anchor=CENTER)

    lblSort = Label(frmSortUsers, text="sort by:", bg=cnvsbg,
                    font=("Helvetica Rounded", 12))
    lblSort.place(relx=.35, rely=.3, anchor=CENTER)

    def doSort():
        sort(clicked.get())

    btnSort = Button(frmSortUsers, text="sort",
                     bg=btnbg, font=("Helvetica Rounded", 12), command=doSort, width=15)
    btnSort.place(relx=.46, rely=.7, anchor=CENTER)

    # sort options end


def booksMenu():
    def booksMenu_ui():
        def backToMenu():
            BtnBackMenu.destroy()
            cnvsBooks.destroy()
            firstMenu()
            global pageStatus
            pageStatus = 2

        def addBook():
            addWindow = Toplevel(root, bg=cnvsbg, takefocus=True)
            addWindow.title("Add Book")
            addWindow.geometry("800x280")
            addWindow.resizable(False, False)
            addWindow.wm_iconphoto(False, photo)

            def saveUser():
                if tkinter.messagebox.askyesno(title="SAVE", message="do you wish to proceed?") == True:
                    id = entAddID.get()
                    lastName = entAddLastName.get()
                    Name = entAddName.get()
                    phone = entAddPhone.get()
                    memidList = set()

                    memID = str(random.randint(100000, 999999))
                    for record in dfUsers.values:
                        memidList.add(record[0])
                        if record[3] == id:
                            tkinter.messagebox.showerror(
                                title="ERROR", message=f"this user with ID:{id}, already exists!")
                            break
                    else:
                        while (True):
                            memid = str(random.randint(100000, 999999))
                            if memid not in memidList:
                                newUserdf = pd.DataFrame({"Mem ID": [memID], "NAME": [Name], "LAST NAME": [lastName], "ID": [id],
                                                          "NUMBER": [phone], "DATE": [dt.datetime.now().strftime('%m/%d/%Y')]})
                                dfUsers = pd.concat(
                                    [dfUsers, newUserdf], ignore_index=True)
                                sort(dbsort)
                                print(dfUsers)
                                break

            lblfrmAddBook = LabelFrame(
                addWindow, text="Add", width=700, height=200, font=("Helvetica Rounded", 10), bg=cnvsbg, bd=2)
            lblfrmAddBook.place(relx=.5, rely=.4, anchor=CENTER)

            entAddTitle = Entry(lblfrmAddBook,
                                font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
            entAddTitle.place(relx=.3, rely=.2, anchor=CENTER)

            lblAddTitle = Label(lblfrmAddBook, text="Title",
                                font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblAddTitle.place(relx=.07, rely=.2, anchor=CENTER)

            entAddAuthor = Entry(lblfrmAddBook,
                                 font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
            entAddAuthor.place(relx=.3, rely=.45, anchor=CENTER)

            lblAddAuthor = Label(lblfrmAddBook, text="Author",
                                 font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblAddAuthor.place(relx=.07, rely=.45, anchor=CENTER)

            entAddPublisher = Entry(lblfrmAddBook,
                                    font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
            entAddPublisher.place(relx=.8, rely=.2, anchor=CENTER)

            lblAddPublisher = Label(lblfrmAddBook, text="Publisher",
                                    font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblAddPublisher.place(relx=.55, rely=.2, anchor=CENTER)

            entAddPublishDate = Entry(lblfrmAddBook,
                                      font=("Helvetica Rounded", 12), bg=entbg, fg=entfg)
            entAddPublishDate.place(relx=.8, rely=.45, anchor=CENTER)

            lblAddPublishDate = Label(lblfrmAddBook, text="publish date",
                                      font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblAddPublishDate.place(relx=.55, rely=.45, anchor=CENTER)

            btnSave = Button(lblfrmAddBook, text="Save",
                             bg=btnbg, font=("Helvetica Rounded", 12), command=saveUser)
            btnSave.place(relx=.5, rely=.85, anchor=CENTER)

            addWindow.grab_set()

        BtnBackMenu = Button(root, text="BACK",
                             bg=btnbg, font=("Helvetica Rounded", 12), command=backToMenu)
        BtnBackMenu.place(relx=.05, rely=.05, anchor=CENTER)

        cnvsBooks = Canvas(root, width=1200, height=500, bg=cnvsbg,
                           highlightthickness=2, highlightbackground=cnvshl)
        cnvsBooks.place(relx=.5, rely=.5, anchor=CENTER)

        lblfrmBooks = LabelFrame(cnvsBooks, text="USERS", bd=2,
                                 bg=cnvsbg, width=760, height=400, font=("Helvetica Rounded", 10))
        lblfrmBooks.place(rely=.5, relx=.36, anchor=CENTER)

        lblfrmOptions = LabelFrame(cnvsBooks, text="OPTIONS", width=300, height=400, font=("Helvetica Rounded", 10), bd=2,
                                   bg=cnvsbg)
        lblfrmOptions.place(rely=.5, relx=.82, anchor=CENTER)

        btnAddBook = Button(lblfrmOptions, text="ADD",
                            bg=btnbg, font=("Helvetica Rounded", 12), width=20, command=addBook)
        btnAddBook.place(rely=.3, relx=.5, anchor=CENTER)

        btnRemoveBook = Button(lblfrmOptions, text="REMOVE",
                               bg=btnbg, font=("Helvetica Rounded", 12), width=20)
        btnRemoveBook.place(rely=.65, relx=.5, anchor=CENTER)

        def booksList():
            global dfBooks
            dfBooks = pd.read_excel(
                'C:/Users/GECKO/git-projects/Library management/db/book.xlsx', na_values="Missing", dtype=str)
            dfBooks = dfBooks.fillna("Missing")

            scrlTree = Scrollbar(lblfrmBooks)
            scrlTree.place(relx=.96, rely=.5, anchor=CENTER, relheight=.852)
            global treeBooks
            treeBooks = ttk.Treeview(lblfrmBooks, height=15,
                                     yscrollcommand=scrlTree.set)
            treeBooks["columns"] = ("Book ID", "Title", "Author",
                                    "publisher", "publish Date")

            scrlTree.config(command=treeBooks.yview)

            treeBooks.column("#0", width=NO, minwidth=NO)
            treeBooks.column("Book ID", anchor=CENTER,
                             width=120, minwidth=100)
            treeBooks.column("Title", anchor=W, width=160, minwidth=100)
            treeBooks.column("Author", anchor=W, width=160, minwidth=100)
            treeBooks.column("publisher", anchor=CENTER, width=80, minwidth=60)
            treeBooks.column("publish Date", anchor=CENTER,
                             width=160, minwidth=100)

            treeBooks.heading("#0", text="", anchor=W)
            treeBooks.heading("Book ID", anchor=CENTER, text="Book ID")
            treeBooks.heading("Title", anchor=W, text="Title")
            treeBooks.heading("Author", anchor=W, text="Author")
            treeBooks.heading("publisher", anchor=CENTER, text="publisher")
            treeBooks.heading("publish Date", anchor=CENTER,
                              text="publish Date")

            treeBooks.tag_configure("oddrow", background=entbg)
            treeBooks.tag_configure("evenrow", background=btnbg)

            iidCount = 0
            for record in dfBooks.values:

                if iidCount % 2 == 1:
                    treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                     values=list(record), tags="oddrow")
                else:
                    treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                     values=list(record), tag="evenrow")
                iidCount += 1

            treeBooks.place(rely=.5, relx=.5, anchor=CENTER)
        booksList()
    booksMenu_ui()


pageDecider(pageStatus)
root.mainloop()
