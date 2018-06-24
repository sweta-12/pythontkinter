from tkinter import Label, Button, Toplevel, Entry, Frame

from signup import signupFrame

class UserLogin(Toplevel):
	def __init__(self, master):
		self.master = master
		self.userlogin_master = Toplevel(master)

		self.frame = Frame(self.userlogin_master)

		self.userlabel = Label(self.userlogin_master, text="User ID")
		self.username = Entry(self.userlogin_master)

		self.userlabel.pack()
		self.username.pack()

		self.login_button = Button(self.userlogin_master, text="Start", command=self.login,width=7)
		self.login_button.pack()

		self.login_button = Button(self.userlogin_master, text="Register", command=self.signup,width=7)
		self.login_button.pack() 

		self.login_button = Button(self.userlogin_master, text="Cancel", command=self.cancel,width=7)
		self.login_button.pack() 

		self.frame.pack()

		self.userlogin_master.protocol("WM_DELETE_WINDOW",self.cancel)
		self.userlogin_master.bind('<Return>', self.login)

	def cancel(self):
		self.userlogin_master.destroy()
		self.master.deiconify()

	def signup(self):
		self.userlogin_master.withdraw()
		self.signup = signupFrame(self.userlogin_master)
	
	def login(self,event=None):
		# match username and password
		if self.username.get() == "user" and self.password.get() == "user":
			# print("Login success")
			self.userlogin_master.destroy()
			# call dashboard window
			dashboard = Dash_board(self.master)
			# self.master.deiconify()
			# print(self.username.get())
			# print(self.password.get())
