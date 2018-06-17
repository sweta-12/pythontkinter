from tkinter import *

from database.db import MindClockDb
from errors import McError

class signupFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        self.signup_master = Toplevel(master)
        self.messages = McError()

        self.label_Username = Label(self.signup_master, text="ID")
        self.label_Age = Label(self.signup_master, text="Age")
        self.label_Gender = Label(self.signup_master, text="Gender")
        self.label_Height = Label(self.signup_master, text="Height(cm)")
        self.label_Weight = Label(self.signup_master, text="Weight")
        #self.label_BMI = Label(self, text="BMI")
        self.label_password = Label(self.signup_master, text="password")
        #self.label_confirm password = Label(self, text="confirm password")

        self.entry_Username = Entry(self.signup_master)
        self.entry_Age = Entry(self.signup_master)
        self.entry_Gender = Entry(self.signup_master)
        self.entry_Height = Entry(self.signup_master)
        self.entry_Weight = Entry(self.signup_master)
        #self.entry_BMI = Entry(self)

        # self.entry_password = Entry(self, show="*")
        #self.entry_confirm password = Entry(self, show="*")

        self.label_Username.grid(row=0, sticky=E)
        self.label_Age.grid(row=1, sticky=E)
        self.label_Gender.grid(row=2, sticky=E)
        self.label_Height.grid(row=3, sticky=E)
        self.label_Weight.grid(row=4, sticky=E)
        #self.label_BMI.grid(row=5, sticky=E)
        # self.label_password.grid(row=5, sticky=E)
        #self.label_confirm password.grid(row=7, sticky=E)
        
        self.entry_Username.grid(row=0, column=1)
        self.entry_Age.grid(row=1, column=1)
        self.entry_Gender.grid(row=2, column=1)
        self.entry_Height.grid(row=3, column=1)
        self.entry_Weight.grid(row=4, column=1)
        #self.entry_BMI.grid(row=5, column=1)
        # self.entry_password.grid(row=6, column=1)
        #self.entry_confirm password.grid(row=7, column=1)

        #self.checkbox = Checkbutton(self, text="welcome to mindclock")
        #self.checkbox.grid(columnspan=2)


        self.signbtn = Button(self.signup_master, text="signup", command=self._signup_btn_clicked)
        self.signbtn.grid(columnspan=2)

        #self.login_button = Button(self.master, text="login", command=self.login_window)
        #self.login_button.pack()


        # self.pack()
   

    def _signup_btn_clicked(self):
        # print("Clicked")
        db = MindClockDb()

        username = self.entry_Username.get()
        age = self.entry_Age.get()
        gender = self.entry_Gender.get()
        height = self.entry_Height.get()
        weight = self.entry_Weight.get()

        sql = "INSERT INTO users(userid, age, weight, height, gender) VALUES('{}',{},'{}','{}','{}')".format(username, age, weight, height, gender)

        if(db.insert(sql)):
            self.messages.success("Success", "Registered Successful!")
            self.signup_master.destroy()
        else:
            self.messages.error("Error", "Something went wrong!")

        #BMI = self.entry_BMI.get()
        # password = self.entry_password.get()
        #confirm password = self.entry_confirm password.get()

        #if username == " password == "password":
            #tm.showinfo("Login info", "Welcome John")
        #else:
            #tm.showerror("Login error", "Incorrect username")

print(__name__)

if __name__ == "__main__":
    root = Tk()
    lf = signupFrame(root)
    root.mainloop()