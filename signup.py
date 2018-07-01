from tkinter import *

from db import MindClockDb
from errors import McError

class signupFrame(Toplevel):
    def __init__(self, master):
        
        self.master = master
        self.signup_master = Toplevel(master)
        self.frame = Frame(self.signup_master)
        self.messages = McError()
        
        self.label_Username = Label(self.signup_master, text="ID",font="papyrus")
        self.label_Firstname = Label(self.signup_master, text="First Name",font="papyrus")
        self.label_Lastname = Label(self.signup_master, text="Last name",font="papyrus")
        self.label_Age = Label(self.signup_master, text="Age",font="papyrus")
        self.label_Gender = Label(self.signup_master, text="Gender",font=("papyrus",12))

        self.label_Height = Label(self.signup_master, text="Height(cm)",font="papyrus")
        self.label_Weight = Label(self.signup_master, text="Weight",font="papyrus")
        
 
        #self.label_BMI = Label(self, text="BMI")
        self.label_password = Label(self.signup_master, text="password",font="papyrus")
        #self.label_confirm password = Label(self, text="confirm password")

        self.entry_Username = Entry(self.signup_master)
        self.entry_Firstname = Entry(self.signup_master)
        self.entry_Lastname =Entry(self.signup_master)
        self.entry_Age = Entry(self.signup_master)
        self.gender = StringVar()
        self.entry_Gender_male=Radiobutton(self.signup_master,variable=self.gender,text="Female",value="Female")
        self.entry_Gender_female=Radiobutton(self.signup_master,variable=self.gender,text="Male",value="Male")
        self.entry_Height = Entry(self.signup_master)
        self.entry_Weight = Entry(self.signup_master)
        
        
       
        #self.entry_BMI = Entry(self)

        # self.entry_password = Entry(self, show="*")
        #self.entry_confirm password = Entry(self, show="*")

        self.label_Username.grid(row=0, sticky=E)
        self.label_Firstname.grid(row=1,sticky=E)
        self.label_Lastname.grid(row=2,sticky=E)
        self.label_Age.grid(row=3, sticky=E)
        self.label_Gender.grid(row=4, sticky=E)
        
        self.label_Height.grid(row=5, sticky=E)
        self.label_Weight.grid(row=6, sticky=E)
        #self.label_BMI.grid(row=5, sticky=E)
        # self.label_password.grid(row=5, sticky=E)
        #self.label_confirm password.grid(row=7, sticky=E)
        
        self.entry_Username.grid(row=0, column=1)
        self.entry_Firstname.grid(row=1,column=1)
        self.entry_Lastname.grid(row=2,column=1)
        self.entry_Age.grid(row=3, column=1)
        self.entry_Gender_male.grid(row=4, sticky=W+W+E, column=1)
        self.entry_Gender_female.grid(row=4, sticky=W+S, column=3)
        self.entry_Height.grid(row=5, column=1)
        self.entry_Weight.grid(row=6, column=1)
        
        #self.entry_BMI.grid(row=5, column=1)
        # self.entry_password.grid(row=6, column=1)
        #self.entry_confirm password.grid(row=7, column=1)

        #self.checkbox = Checkbutton(self, text="welcome to mindclock")
        #self.checkbox.grid(columnspan=2)
        


        self.signbtn = Button(self.signup_master, text="signup",font="papyrus", command=self._signup_btn_clicked)
        self.signbtn.grid(columnspan=2)

        #self.login_button = Button(self.master, text="login", command=self.login_window)
        #self.login_button.pack()
        
        self.signup_master.geometry('500x400')
        # self.pack()
        self.signup_master.protocol("WM_DELETE_WINDOW",self.cancel)
        


    def BMI(self, weight, height):
        bmi=(float(weight))*10000/(float(height)*float(height))

        return bmi
   


    def _signup_btn_clicked(self):
        db = MindClockDb(self.signup_master)

        username = self.entry_Username.get()
        firstname=self.entry_Firstname.get()
        lastname=self.entry_Lastname.get()
        age = self.entry_Age.get()
        gender = self.gender.get()
        height = self.entry_Height.get()
        weight = self.entry_Weight.get()

        bmi = self.BMI(weight,height)
        

        sql = "INSERT INTO users(userid,firstname,lastname, age, weight, height, gender, bmi) VALUES('{}','{}','{}',{},'{}','{}','{}','{}')".format(username,firstname,lastname, age, weight, height, gender, bmi)

        if(db.insert(sql)):
            self.messages.success("Success", "Registered Successfully!")
            self.signup_master.destroy()
            self.master.deiconify()
        else:
            self.signup_master.withdraw()
            self.messages.error("Error", "Something went wrong!")
            self.signup_master.deiconify()

    def cancel(self):
        self.signup_master.destroy()
        self.master.deiconify()


        #BMI = self.entry_BMI.get()
        # password = self.entry_password.get()
        #confirm password = self.entry_confirm password.get()

        #if username == " password == "password":
            #tm.showinfo("Login info", "Welcome John")
        #else:
            #tm.showerror("Login error", "Incorrect username")
    

# if __name__ == "__main__":
#     root = Tk()
#     lf = signupFrame(root)
#     root.mainloop()