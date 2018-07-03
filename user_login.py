from tkinter import Label, Button, Toplevel, Entry, Frame

from signup import signupFrame
from testwindow import TestWindow

from errors import McError

import sqlite3

class UserLogin(Toplevel):
	def __init__(self, master):
		self.master = master
		self.userlogin_master = Toplevel(master)
		self.userlogin_master.title("User")
		self.frame = Frame(self.userlogin_master)
		self.messages = McError()

		self.db=sqlite3.connect("mindclock.db")
		self.cursor=self.db.cursor()

		self.userlabel = Label(self.userlogin_master, text="User ID",font="papyrus")
		self.username = Entry(self.userlogin_master)

		self.userlabel.pack()
		self.username.pack()


		self.login_button = Button(self.userlogin_master,font="papyrus", text="Start", command=self.login,width=7)
		self.login_button.pack()

		self.login_button = Button(self.userlogin_master,font="papyrus", text="Register", command=self.signup,width=7)
		self.login_button.pack() 

		self.login_button = Button(self.userlogin_master,font="papyrus", text="Cancel", command=self.cancel,width=7)
		self.login_button.pack() 


		self.frame.pack()

		self.userlogin_master.protocol("WM_DELETE_WINDOW",self.cancel)
		self.userlogin_master.bind('<Return>', self.login)
		self.userlogin_master.geometry('500x400')

	def cancel(self):
		self.userlogin_master.destroy()
		self.master.deiconify()

	def signup(self):
		self.userlogin_master.withdraw()
		self.signup = signupFrame(self.userlogin_master)
	
	def login(self,event=None):

		find_user = ('SELECT userid FROM users WHERE userid = ?')
		self.cursor.execute(find_user,[(self.username.get())])
		value = self.username.get()
		result = self.cursor.fetchone()
		
		if result:
			self.userlogin_master.destroy()
			# call dashboard window
			#window = Production(self.master, x1=100, y1=100)
			self.userlogin_master = TestWindow(self.master)
		elif result!=value and value!="":
			self.userlogin_master.withdraw()
			self.messages.error("Error","Invalid User ID")
			self.username.delete(0,'end')
			self.userlogin_master.deiconify()
		else:
			self.userlogin_master.withdraw()
			self.messages.error("Error","Fields cannot be empty")
			self.userlogin_master.deiconify()