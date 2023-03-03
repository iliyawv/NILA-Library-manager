from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from tkinter import ttk
import pandas as pd
import random
import datetime as dt
from tkcalendar.calendar_ import Calendar
import pyglet

# install path
# os.path.realpath(os.path.dirname(__file__))
# os.getcwd()
instalPath = os.getcwd()


pyglet.font.add_file(instalPath+"/media/Helvetica-Bold.ttf")
# general attributes
pageStatus = 2
isHidden = True
dbsort = "NONE"

# color pallete
entfg = "#695f64"
entbg = "#e5e4e0"
cnvsbg = "#b0997d"
cnvshl = "#612601"
btnbg = "#daccbf"

entryFont = ("Helvetica Rounded", 18)

# database
dfIssues = pd.read_excel(
    instalPath+"/db/Issue.xlsx", na_values="Missing", dtype=str)
dfIssues = dfIssues.fillna("Missing")

dfUsers = pd.read_excel(
    instalPath+"/db/user.xlsx", na_values="Missing", dtype=str)
dfUsers = dfUsers.fillna("Missing")

dfBooks = pd.read_excel(
    instalPath+"/db/book.xlsx", na_values="Missing", dtype=str)
dfBooks = dfBooks.fillna("Missing")

# penalty price
penalty = 500


root = Tk()

# media
loginBG = PhotoImage(
    file=instalPath+"/media/libBG.png")

ico = Image.open(
    instalPath+"/media/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

viewIcon = PhotoImage(
    file=instalPath+"/media/view.png")
hiddenIcon = PhotoImage(
    file=instalPath+"/media/hidden.png")

# root attributes
root.title("NILA Library")
root.geometry("1200x800")
root.state('zoomed')
lblphoto = Label(root, image=loginBG,
                 width=root.winfo_screenwidth(), height=root.winfo_screenheight())
lblphoto.pack()


# decides which page to show
def pageDecider(value):
    if value == 1:
        loginPage()

    elif value == 2:
        firstMenu()

    elif value == 3:
        usersMenu()
    elif value == 4:
        booksMenu()
    elif value == 5:
        issueMenu()
# login page and the first page of program


def loginPage():

    def login(e=""):
        username = entUsername.get()
        password = entPass.get()
        try:
            credential = open(
                instalPath+f"/{username}.txt", "r")
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

    def openIssue():
        BtnLogout.destroy()
        global pageStatus
        pageStatus = 5
        canvas2.destroy()
        issueMenu()

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
                      font=("Helvetica Rounded", 34), width=20, command=openIssue)
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
        global dfUsers, treeUsers
        treeUsers = ttk.Treeview(frmUsers, height=15,
                                 yscrollcommand=scrlTree.set)
        treeUsers["columns"] = ("Membership ID", "First Name", "Last Name", "ID",
                                "Phone Number", "Reg Date")

        scrlTree.config(command=treeUsers.yview)

        treeUsers.column("#0", width=NO, minwidth=NO)
        treeUsers.column("Membership ID", anchor=CENTER,
                         width=120, minwidth=100)
        treeUsers.column("First Name", anchor=W, width=160, minwidth=100)
        treeUsers.column("Last Name", anchor=W, width=160, minwidth=100)
        treeUsers.column("ID", anchor=CENTER, width=80, minwidth=60)
        treeUsers.column("Phone Number", anchor=CENTER,
                         width=160, minwidth=100)
        treeUsers.column("Reg Date", anchor=CENTER, width=120, minwidth=80)

        treeUsers.heading("#0", text="", anchor=W)
        treeUsers.heading("Membership ID", anchor=CENTER, text="Membership ID")
        treeUsers.heading("First Name", anchor=W, text="First Name")
        treeUsers.heading("Last Name", anchor=W, text="Last Name")
        treeUsers.heading("ID", anchor=CENTER, text="ID")
        treeUsers.heading("Phone Number", anchor=CENTER, text="Phone Number")
        treeUsers.heading("Reg Date", anchor=CENTER, text="Reg Date")

        treeUsers.tag_configure("oddrow", background=entbg)
        treeUsers.tag_configure("evenrow", background=btnbg)

        iidCount = 0
        for record in dfUsers.values:

            if iidCount % 2 == 1:
                treeUsers.insert(parent="", index='end', iid=iidCount, text="",
                                 values=list(record), tags="oddrow")
            else:
                treeUsers.insert(parent="", index='end', iid=iidCount, text="",
                                 values=list(record), tag="evenrow")
            iidCount += 1

        treeUsers.place(rely=.5, relx=.5, anchor=CENTER)

        treeUsers.bind("<Double-1>", click)

        def userInfo(e=""):
            selected = treeUsers.focus()
            user = treeUsers.item(selected, "values")

            for record in dfUsers.values:
                if record[0] == user[0]:
                    userInfo = Toplevel(root, bg=cnvsbg, takefocus=True)
                    userInfo.title("INFO")
                    userInfo.geometry("600x400")
                    userInfo.resizable(False, False)
                    lblfrm = LabelFrame(userInfo, bd=2, text="History",
                                        bg=cnvsbg, width=575, height=375, font=("Helvetica Rounded", 10))
                    lblfrm.place(relx=.5, rely=.5, anchor=CENTER)
                    lblbalance = Label(lblfrm, text="Balance: "+record[7],
                                       font=("Helvetica Rounded", 12), bg=cnvsbg)
                    lblbalance.place(relx=.15, rely=.9, anchor=CENTER)

                    treeHitory = ttk.Treeview(lblfrm, height=12)
                    treeHitory["columns"] = (
                        "Books Issued", "issued Date", "Return Date")

                    treeHitory.column("#0", width=NO, minwidth=NO)
                    treeHitory.column("Books Issued", anchor=CENTER,
                                      width=120, minwidth=100)
                    treeHitory.column("issued Date", anchor=W,
                                      width=160, minwidth=100)
                    treeHitory.column("Return Date", anchor=W,
                                      width=160, minwidth=100)

                    treeHitory.heading("#0", text="", anchor=W)
                    treeHitory.heading(
                        "Books Issued", anchor=CENTER, text="Books Issued")
                    treeHitory.heading(
                        "issued Date", anchor=W, text="issued Date")
                    treeHitory.heading(
                        "Return Date", anchor=W, text="Return Date")

                    treeHitory.tag_configure("oddrow", background=entbg)
                    treeHitory.tag_configure("evenrow", background=btnbg)
                    infoList = list(
                        zip(record[6].split("|"), record[8].split("|"), record[9].split("|")))
                    iidCount = 0
                    for record in infoList[2:]:

                        if iidCount % 2 == 1:
                            treeHitory.insert(parent="", index='end', iid=iidCount, text="",
                                              values=list(record), tags="oddrow")
                        else:
                            treeHitory.insert(parent="", index='end', iid=iidCount, text="",
                                              values=list(record), tag="evenrow")
                        iidCount += 1

                    treeHitory.place(rely=.4, relx=.5, anchor=CENTER)

                    userInfo.grab_set()
                    break

        treeUsers.bind("<Button-3>	", userInfo)

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
        selected = treeUsers.focus()
        delValues = treeUsers.item(selected, "values")

        for index, record in enumerate(dfUsers.values):
            if list(record) == list(delValues):
                if tkinter.messagebox.askyesno("DELETE", "do you want to proceed?") == True:
                    dfUsers.drop(index=index, inplace=True)
                    sort(dbsort)
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

                for record in dfUsers.values:
                    memidList.add(record[0])
                    if record[3] == id:
                        tkinter.messagebox.showerror(
                            title="ERROR", message=f"this user with ID:{id}, already exists!")
                        break
                else:
                    while (True):
                        memID = str(random.randint(100000, 999999))
                        if memID not in memidList:
                            regDate = dt.datetime.now().strftime('%m/%d/%Y')
                            newUserdf = pd.DataFrame({"Mem ID": [memID], "NAME": [Name], "LAST NAME": [lastName], "ID": [id],
                                                      "NUMBER": [phone], "DATE": [regDate], "Book ID": ["|"], "balance": ["0"], "Iss Date": ["|"], "Ret Date": ["|"]})
                            dfUsers = pd.concat(
                                [dfUsers, newUserdf], ignore_index=True)
                            sort(dbsort)

                            from PIL import Image
                            from PIL import ImageDraw

                            from PIL import ImageFont

                            imgFront = Image.open(
                                instalPath+"/membership cards/template/1.png")

                            # ERROR(inheriting not possible)
                            I1 = ImageDraw.Draw(imgFront)
                            I2 = ImageDraw.Draw(imgFront)
                            I3 = ImageDraw.Draw(imgFront)
                            I4 = ImageDraw.Draw(imgFront)
                            myFont = ImageFont.truetype(
                                instalPath+"/media/Helvetica-Bold.ttf", 40)

                            I1.text((680, 263), Name+" "+lastName, fill=(176, 153, 125),
                                    font=myFont, align="center", anchor="mm")
                            I2.text((758, 380), memID, fill=(0, 0, 0),
                                    font=myFont, align="center", anchor="mm")
                            I3.text((758, 473), id, fill=(0, 0, 0),
                                    font=myFont, align="center", anchor="mm")
                            I4.text((758, 565), regDate, fill=(0, 0, 0),
                                    font=myFont, align="center", anchor="mm")

                            imgFront.show()
                            imgFront.save(
                                instalPath+"/membership cards/"+id+".png")
                            addWindow.destroy()
                            tkinter.messagebox.showinfo(
                                title="SUCCESSFULL!", message="You added a new user successfuly")
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

        global treeUsers, entMemID, entName, entLName, id, values
        selected = treeUsers.focus()
        values = treeUsers.item(selected, "values")
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
            instalPath+"/db/user.xlsx", index=False, header=True)

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

            def saveBook():
                global dfBooks, lblfrmBooks
                if tkinter.messagebox.askyesno(title="SAVE", message="do you wish to proceed?") == True:
                    title = entAddTitle.get()
                    author = entAddAuthor.get()
                    publisher = entAddPublisher.get()
                    publishDate = entAddPublishDate.get()

                    while True:
                        bookID = str(random.randint(1000000, 9999999))
                        for record in dfBooks.values:
                            if record[0] == bookID:
                                break
                        else:
                            break

                    newDf = pd.DataFrame({"Book ID": [bookID], "Title": [title], "Author": [author],
                                         "Publisher": [publisher], "publish Date": [publishDate], "Status": ["True"]})
                    dfBooks = pd.concat([dfBooks, newDf], ignore_index=True,)
                    dfBooks = dfBooks.sort_values(
                        by="Publisher",  ascending=True)

                    dfBooks.reset_index(drop=True, inplace=True)
                    dfBooks.to_excel(
                        instalPath+"/db/book.xlsx", index=False, header=True)
                    lblfrmBooks.destroy()
                    booksList()
                    addWindow.destroy()
                    tkinter.messagebox.showinfo(
                        title="SUCCESSFULL!", message="You added a new Book successfuly")

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
                             bg=btnbg, font=("Helvetica Rounded", 12), command=saveBook)
            btnSave.place(relx=.5, rely=.85, anchor=CENTER)

            addWindow.grab_set()

        def deleteBook():
            global dfBooks
            selected = treeBooks.focus()
            delValues = treeBooks.item(selected, "values")

            for index, record in enumerate(dfBooks.values):
                if list(record)[0] == list(delValues)[0]:
                    if tkinter.messagebox.askyesno("DELETE", "do you want to proceed?") == True:
                        dfBooks.drop(index=index, inplace=True)
                        dfBooks.to_excel(
                            instalPath+"/db/book.xlsx", index=False, header=True)

                        tkinter.messagebox.showinfo(
                            title="Successful", message=f"book {record[1]} removed!")
                        booksList()
                        break
                    else:
                        break
            else:
                tkinter.messagebox.showerror(
                    title="ERROR", message="something wrong happened!")

        BtnBackMenu = Button(root, text="BACK",
                             bg=btnbg, font=("Helvetica Rounded", 12), command=backToMenu)
        BtnBackMenu.place(relx=.05, rely=.05, anchor=CENTER)

        cnvsBooks = Canvas(root, width=1200, height=500, bg=cnvsbg,
                           highlightthickness=2, highlightbackground=cnvshl)
        cnvsBooks.place(relx=.5, rely=.5, anchor=CENTER)

        lblfrmOptions = LabelFrame(cnvsBooks, text="OPTIONS", width=300, height=400, font=("Helvetica Rounded", 10), bd=2,
                                   bg=cnvsbg)
        lblfrmOptions.place(rely=.5, relx=.82, anchor=CENTER)

        btnAddBook = Button(lblfrmOptions, text="ADD",
                            bg=btnbg, font=("Helvetica Rounded", 12), width=20, command=addBook)
        btnAddBook.place(rely=.3, relx=.5, anchor=CENTER)

        btnRemoveBook = Button(lblfrmOptions, text="REMOVE",
                               bg=btnbg, font=("Helvetica Rounded", 12), width=20, command=deleteBook)
        btnRemoveBook.place(rely=.65, relx=.5, anchor=CENTER)

        def booksList():
            global dfBooks, lblfrmBooks
            lblfrmBooks = LabelFrame(cnvsBooks, text="BOOKS", bd=2,
                                     bg=cnvsbg, width=760, height=400, font=("Helvetica Rounded", 10))
            lblfrmBooks.place(rely=.5, relx=.36, anchor=CENTER)

            scrlTree = Scrollbar(lblfrmBooks)
            scrlTree.place(relx=.96, rely=.5, anchor=CENTER, relheight=.852)
            global treeBooks
            treeBooks = ttk.Treeview(lblfrmBooks, height=15,
                                     yscrollcommand=scrlTree.set)
            treeBooks["columns"] = ("Book ID", "Title", "Author",
                                    "Publisher", "Publish Date", "Status")

            scrlTree.config(command=treeBooks.yview)

            treeBooks.column("#0", width=NO, minwidth=NO)
            treeBooks.column("Book ID", anchor=CENTER,
                             width=80, minwidth=70)
            treeBooks.column("Title", anchor=W, width=160, minwidth=100)
            treeBooks.column("Author", anchor=W, width=160, minwidth=100)
            treeBooks.column("Publisher", anchor=CENTER, width=80, minwidth=60)
            treeBooks.column("Publish Date", anchor=CENTER,
                             width=160, minwidth=100)
            treeBooks.column("Status", anchor=CENTER,
                             width=80, minwidth=60)

            treeBooks.heading("#0", text="", anchor=W)
            treeBooks.heading("Book ID", anchor=CENTER, text="Book ID")
            treeBooks.heading("Title", anchor=W, text="Title")
            treeBooks.heading("Author", anchor=W, text="Author")
            treeBooks.heading("Publisher", anchor=CENTER, text="Publisher")
            treeBooks.heading("Publish Date", anchor=CENTER,
                              text="Publish Date")
            treeBooks.heading("Status", anchor=CENTER,
                              text="Status")

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


def issueMenu():
    def issueMenu_ui():
        def backToMenu():
            BtnBackMenu.destroy()
            cnvsIssue.destroy()
            firstMenu()
            global pageStatus
            pageStatus = 2

        def addIssue():
            addWindow = Toplevel(root, bg=cnvsbg, takefocus=True)
            addWindow.title("ADD ISSUE")
            addWindow.geometry("900x350")
            addWindow.resizable(False, False)
            addWindow.wm_iconphoto(False, photo)

            searchIcon = PhotoImage(
                file=instalPath+"/media/search.png")

            lblframeAddIssue = LabelFrame(addWindow, text="ADD", bd=2,
                                          bg=cnvsbg, width=850, height=320, font=("Helvetica Rounded", 10))
            lblframeAddIssue.place(rely=.5, relx=.5, anchor=CENTER)

            lblUserID = Label(lblframeAddIssue, text="User ID:",
                              font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblUserID.place(rely=.3, relx=.07, anchor=CENTER)

            entUserID = Entry(lblframeAddIssue,
                              font=("Helvetica Rounded", 14), bg=entbg, fg=entfg)
            entUserID.place(rely=.3, relx=.3, anchor=CENTER)

            lblBookID = Label(lblframeAddIssue, text="Book ID:",
                              font=("Helvetica Rounded", 12), bg=cnvsbg)
            lblBookID.place(rely=.6, relx=.07, anchor=CENTER)

            entBookID = Entry(lblframeAddIssue,
                              font=("Helvetica Rounded", 14), bg=entbg, fg=entfg)
            entBookID.place(rely=.6, relx=.3, anchor=CENTER)

            def searchWindow():
                searchwindow = Toplevel(addWindow, bg=cnvsbg, takefocus=True)
                searchwindow.title("search Book")
                searchwindow.geometry("800x400")
                searchwindow.resizable(False, False)
                searchwindow.wm_iconphoto(False, photo)
                lblframettk = LabelFrame(searchwindow, text="books", bd=2,
                                         bg=cnvsbg, width=750, height=375, font=("Helvetica Rounded", 10))
                lblframettk.place(rely=.5, relx=.5, anchor=CENTER)

                treeBooks = ttk.Treeview(lblframettk, height=12)
                treeBooks["columns"] = ("Book ID", "Title", "Author",
                                        "Publisher", "Publish Date", "Status")

                treeBooks.column("#0", width=NO, minwidth=NO)
                treeBooks.column("Book ID", anchor=CENTER,
                                 width=80, minwidth=70)
                treeBooks.column("Title", anchor=W, width=160, minwidth=100)
                treeBooks.column("Author", anchor=W, width=160, minwidth=100)
                treeBooks.column("Publisher", anchor=CENTER,
                                 width=80, minwidth=60)
                treeBooks.column("Publish Date", anchor=CENTER,
                                 width=160, minwidth=100)
                treeBooks.column("Status", anchor=CENTER,
                                 width=80, minwidth=60)

                treeBooks.heading("#0", text="", anchor=W)
                treeBooks.heading("Book ID", anchor=CENTER, text="Book ID")
                treeBooks.heading("Title", anchor=W, text="Title")
                treeBooks.heading("Author", anchor=W, text="Author")
                treeBooks.heading("Publisher", anchor=CENTER, text="Publisher")
                treeBooks.heading("Publish Date", anchor=CENTER,
                                  text="Publish Date")
                treeBooks.heading("Status", anchor=CENTER,
                                  text="Status")

                treeBooks.tag_configure("oddrow", background=entbg)
                treeBooks.tag_configure("evenrow", background=btnbg)

                treeBooks.place(rely=.6, relx=.5, anchor=CENTER)

                entsearch = Entry(lblframettk, font=("Helvetica Rounded", 12),
                                  bg=entbg, fg=entfg)

                treeBooks.tag_configure("oddrow", background=entbg)
                treeBooks.tag_configure("evenrow", background=btnbg)

                entsearch.place(rely=.1, relx=.22, anchor=CENTER)

                def doSearch():
                    book = entsearch.get()
                    if book == "":
                        iidCount = 0
                        treeBooks.delete(*treeBooks.get_children())
                        for record in dfBooks.values:

                            if iidCount % 2 == 1:
                                treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                                 values=list(record), tags="oddrow")
                            else:
                                treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                                 values=list(record), tag="evenrow")
                            iidCount += 1
                    else:
                        iidCount = 0
                        treeBooks.delete(*treeBooks.get_children())
                        for bookname in dfBooks.values:
                            if book in bookname[1]:
                                if iidCount % 2 == 1:
                                    treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                                     values=list(bookname), tags="oddrow")
                                else:
                                    treeBooks.insert(parent="", index='end', iid=iidCount, text="",
                                                     values=list(bookname), tag="evenrow")
                                iidCount += 1
                doSearch()

                def bookNameByID(e=""):
                    selected = treeBooks.focus()
                    item = treeBooks.item(selected, "values")[0]
                    searchwindow.destroy()

                    entBookID.insert(0, item)

                treeBooks.bind("<Double-1>", bookNameByID)
                btnDoSearch = Button(
                    lblframettk, text="Search", bg=btnbg, font=("Helvetica Rounded", 12), command=doSearch)
                btnDoSearch.place(rely=.1, relx=.49, anchor=CENTER)

                searchwindow.grab_set()

            btnSearch = Button(lblframeAddIssue, height=20,
                               width=20, image=searchIcon, command=searchWindow)
            btnSearch.image = searchIcon

            btnSearch.place(rely=.6, relx=.43, anchor=CENTER)

            def apply():
                global lblfrmIssues
                global dfUsers, dfBooks, dfIssues
                if tkinter.messagebox.askokcancel(title="Save Issue", message="do you wish to proceed?"):
                    userID = entUserID.get()
                    bookID = entBookID.get()
                    doBreak = False
                    for i, record in enumerate(dfUsers.values):
                        if record[0] == userID:
                            for j, book in enumerate(dfBooks.values):
                                if book[0] == bookID:
                                    if book[5] == "True":
                                        while True:
                                            issueID = str(
                                                random.randint(1000000, 9999999))
                                            for id in dfIssues.values:
                                                if record[0] == issueID:
                                                    break
                                            else:
                                                break

                                        IssDate = dt.datetime.now().strftime('%m/%d/%Y')
                                        RetDate = cal.get_date()
                                        newdf = pd.DataFrame(
                                            {"Issue Number": [issueID], "User": [record[1]+" "+record[2]], "User ID": [userID], "Title": [book[1]], "book ID": [bookID], "Issue Date": [IssDate], "EXP Date": [RetDate]})
                                        dfIssues = pd.concat(
                                            [dfIssues, newdf], ignore_index=True)
                                        dfIssues.to_excel(
                                            instalPath+"/db/Issue.xlsx", index=False, header=True)

                                        dfUsers.at[i, "Book ID"] = record[6] + \
                                            "|" + book[0]
                                        dfUsers.at[i, "Iss Date"] = record[8] + \
                                            "|" + IssDate
                                        dfUsers.at[i, "Ret Date"] = record[9] + \
                                            "|" + RetDate

                                        dfBooks.at[j, "Status"] = "False"

                                        dfUsers.to_excel(
                                            instalPath+"/db/user.xlsx", index=False, header=True)
                                        dfBooks.to_excel(
                                            instalPath+"/db/book.xlsx", index=False, header=True)

                                        lblfrmIssues.destroy()
                                        issueList()
                                        tkinter.messagebox.showinfo(
                                            title="SUCCESSFULL!", message="You added a new Issue successfuly")
                                        addWindow.destroy()

                                        doBreak = True
                                        break
                                    else:
                                        tkinter.messagebox.showerror(
                                            title="ERROR", message="Someone else has the book!")
                                        doBreak = True
                                        break

                            else:
                                tkinter.messagebox.showerror(
                                    title="ERROR", message="Book not found!")
                        if doBreak:
                            break

                    else:
                        tkinter.messagebox.showerror(
                            title="ERROR", message="User not found!")

            btnApply = Button(lblframeAddIssue, text="Apply",
                              bg=btnbg, font=("Helvetica Rounded", 12), command=apply)
            btnApply.place(rely=.85, relx=.5, anchor=CENTER)

            lblReturnDate = Label(lblframeAddIssue, text="pick a date to return", font=(
                "Helvetica Rounded", 12), bg=cnvsbg)
            lblReturnDate.place(rely=.1, relx=.8, anchor=CENTER)

            cal = Calendar(lblframeAddIssue, selectmode="day",
                           mindate=dt.date.today(), maxdate=dt.date.today()+dt.timedelta(days=180), background=cnvshl, bordercolor=cnvsbg, headersbackground=btnbg, date_pattern="mm/dd/y")
            cal.place(rely=.5, relx=.8, anchor=CENTER)

            addWindow.grab_set()

        BtnBackMenu = Button(root, text="BACK",
                             bg=btnbg, font=("Helvetica Rounded", 12), command=backToMenu)
        BtnBackMenu.place(relx=.05, rely=.05, anchor=CENTER)

        cnvsIssue = Canvas(root, width=1200, height=800, bg=cnvsbg,
                           highlightthickness=2, highlightbackground=cnvshl)
        cnvsIssue.place(relx=.5, rely=.5, anchor=CENTER)

        lblframeOptions = LabelFrame(cnvsIssue, text="OPTIONS", bd=2,
                                     bg=cnvsbg, width=400, height=100, font=("Helvetica Rounded", 10))
        lblframeOptions.place(rely=.85, relx=.5, anchor=CENTER)

        btnAddIssue = Button(lblframeOptions, text="issue a book",
                             bg=btnbg, font=("Helvetica Rounded", 12), command=addIssue)
        btnAddIssue.place(rely=.5, relx=.3, anchor=CENTER)

        def returnBook():
            global dfIssues, treeIssues, penalty, dfBooks
            selected = treeIssues.focus()
            delValues = treeIssues.item(selected, "values")

            for i, record in enumerate(dfIssues.values):
                if list(delValues) == list(record):
                    dfIssues.drop(index=i, inplace=True)
                    dfIssues.to_excel(
                        instalPath+"/db/Issue.xlsx", index=False, header=True)
                    lblfrmIssues.destroy()
                    issueList()

                    dayscount = (dt.datetime.strptime(
                        record[6], "%m/%d/%Y") - dt.datetime.now()).days + 1

                    for j, book in enumerate(dfBooks.values):
                        if delValues[4] == book[0]:
                            dfBooks.at[j, "Status"] = "True"
                            dfBooks.to_excel(
                                instalPath+"/db/book.xlsx", index=False, header=True)

                            break
                    tkinter.messagebox.showinfo(
                        title="SUCCESSFULL!", message="You deleted the Issue successfuly")

                    if dayscount < 0:
                        for index, user in enumerate(dfUsers.values):
                            if user[0] == record[2]:
                                dfUsers.at[index, "balance"] = str(
                                    int(user[7]) + (dayscount * penalty))
                                dfUsers.to_excel(
                                    instalPath+"/db/user.xlsx", index=False, header=True)
                                break

        btnReturn = Button(lblframeOptions, text="Return",
                           bg=btnbg, font=("Helvetica Rounded", 12), command=returnBook)
        btnReturn.place(rely=.5, relx=.7, anchor=CENTER)

        def issueList():
            global lblfrmIssues, dfIssues
            lblfrmIssues = LabelFrame(cnvsIssue, text="ISSUES", bd=2,
                                      bg=cnvsbg, width=1000, height=600, font=("Helvetica Rounded", 10))
            lblfrmIssues.place(rely=.4, relx=.5, anchor=CENTER)

            scrlTree = Scrollbar(lblfrmIssues)
            scrlTree.place(relx=.92, rely=.5, anchor=CENTER, relheight=.87)
            global treeIssues
            treeIssues = ttk.Treeview(lblfrmIssues, height=24,
                                      yscrollcommand=scrlTree.set)
            treeIssues["columns"] = ("Issue Number", "User", "User ID",
                                     "Title", "book ID", "Issue Date", "EXP Date")

            scrlTree.config(command=treeIssues.yview)

            treeIssues.column("#0", width=NO, minwidth=NO)
            treeIssues.column("Issue Number", anchor=CENTER,
                              width=90, minwidth=80)
            treeIssues.column("User", anchor=W, width=160, minwidth=100)
            treeIssues.column("User ID", anchor=W, width=100, minwidth=80)
            treeIssues.column("Title", anchor=CENTER, width=160, minwidth=100)
            treeIssues.column("book ID", anchor=CENTER,
                              width=90, minwidth=80)
            treeIssues.column("Issue Date", anchor=CENTER,
                              width=110, minwidth=100)
            treeIssues.column("EXP Date", anchor=CENTER,
                              width=110, minwidth=100)

            treeIssues.heading("#0", text="", anchor=W)
            treeIssues.heading("Issue Number", anchor=CENTER,
                               text="Issue Number")
            treeIssues.heading("User", anchor=W, text="User")
            treeIssues.heading("User ID", anchor=W, text="User ID")
            treeIssues.heading("Title", anchor=CENTER, text="Title")
            treeIssues.heading("book ID", anchor=CENTER,
                               text="book ID")
            treeIssues.heading("Issue Date", anchor=CENTER,
                               text="Issue Date")
            treeIssues.heading("EXP Date", anchor=CENTER,
                               text="EXP Date")

            treeIssues.tag_configure("oddrow", background=entbg)
            treeIssues.tag_configure("evenrow", background=btnbg)
            treeIssues.tag_configure("expired", foreground="red")

            iidCount = 0
            cTime = dt.datetime.now().strftime('%m/%d/%Y')
            for record in dfIssues.values:

                if iidCount % 2 == 1:
                    if record[-1] < cTime:
                        treeIssues.insert(parent="", index='end', iid=iidCount, text="",
                                          values=list(record), tags=("expired", "oddrow"))
                    else:
                        treeIssues.insert(parent="", index='end', iid=iidCount, text="",
                                          values=list(record), tags="oddrow")
                else:
                    if record[-1] < cTime:
                        treeIssues.insert(parent="", index='end', iid=iidCount, text="",
                                          values=list(record), tags=("expired", "evenrow"))
                    else:
                        treeIssues.insert(parent="", index='end', iid=iidCount, text="",
                                          values=list(record), tags="evenrow")

                iidCount += 1

            treeIssues.place(rely=.5, relx=.5, anchor=CENTER)
        issueList()
    issueMenu_ui()


pageDecider(pageStatus)
root.mainloop()
