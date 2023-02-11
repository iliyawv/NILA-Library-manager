from tkinter import *

root = Tk()

# general att
root.title("Library manager")
root.geometry("1200x800")
root.state('zoomed')


def loginPage():
    root.config(bg="#559364")
    canvas = Canvas(root, width=500, height=700,
                    bg="#AEC09A", highlightthickness=0, highlightbackground="#559364")
    canvas.place(relx=.5, rely=.5, anchor=CENTER)

    entryFont = ("Helvetica Rounded", 16)
    entUsername = Entry(canvas, font=entryFont, bg="#e7f0ef", fg="#559364")
    entUsername.place(relx=.5, rely=.3, anchor=CENTER)


loginPage()


root.mainloop()
