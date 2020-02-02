from tkinter import *


class View:

    def __init__(self):
        self.window = Tk()
        self.nameFlag = False

        self.frame = Frame(self.window)
        self.frame.grid(row=0)

        self.messages = Text(self.frame)
        self.messages.grid(row="0", column=0, columnspan=22, sticky=EW)
        self.input_user = StringVar()
        self.input_field = Entry(self.frame, text=self.input_user)
        self.input_field.grid(row=20, column=10, sticky=EW)

        self.myLabel1 = Label(self.window, text="")
        self.myLabel2 = Label(self.window, text="")
        self.myLabel3 = Label(self.window, text="")
        self.myLabel1.grid(row=1, column=0)
        self.myLabel2.grid(row=1, column=15)
        self.myLabel3.grid(row=1, column=30)

        self.myLabel4 = Label(self.window, text="")
        self.myLabel5 = Label(self.window, text="")
        self.myLabel6 = Label(self.window, text="")
        self.myLabel4.grid(row=10, column=0)
        self.myLabel5.grid(row=10, column=15)
        self.myLabel6.grid(row=10, column=30)

        self.myLabel7 = Label(self.window, text="")
        self.myLabel8 = Label(self.window, text="")
        self.myLabel9 = Label(self.window, text="")
        self.myLabel7.grid(row=20, column=0)
        self.myLabel8.grid(row=20, column=15)
        self.myLabel9.grid(row=20, column=30)

    def assign(self, fnc):
        self.input_field.bind("<Return>", fnc)

    def Enter_pressed(self, event):
        self.input_get = input_field.get()
        self.messages.insert(INSERT, '%s\n' % input_get)
        self.input_user.set('')
        return "break"

    def changeLabel1(self, newStr):
        self.myLabel1['text'] = newStr

    def changeLabel2(self, newStr):
        self.myLabel2['text'] = newStr

    def changeLabel3(self, newStr):
        self.myLabel3['text'] = newStr

    def changeLabel4(self, newStr):
        self.myLabel4['text'] = newStr

    def changeLabel5(self, newStr):
        self.myLabel5['text'] = newStr

    def changeLabel6(self, newStr):
        self.myLabel6['text'] = newStr

    def changeLabel7(self, newStr):
        self.myLabel7['text'] = newStr

    def changeLabel8(self, newStr):
        self.myLabel8['text'] = newStr

    def changeLabel9(self, newStr):
        self.myLabel9['text'] = newStr

    def pushChat(self, msg):
        self.messages.insert(INSERT, msg)

    def mainLoop(self):
        self.window.mainloop()
