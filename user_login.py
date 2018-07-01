from tkinter import Label, Button, Toplevel, Entry, Frame

from signup import signupFrame
from production import Production

class UserLogin(Toplevel):
	def __init__(self, master):
		self.master = master
		self.userlogin_master = Toplevel(master)

		self.frame = Frame(self.userlogin_master)

		self.userlabel = Label(self.userlogin_master, text="User ID",font="papyrus")
		self.username = Entry(self.userlogin_master)

		self.userlabel.pack()
		self.username.pack()

		self.login_button = Button(self.userlogin_master,font="papyrus", text="Start", command=self.production_open,width=7)
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
		# match username and password
		if self.username.get() == "user" and self.password.get() == "user":
			# print("Login success")
			self.userlogin_master.destroy()
			# call dashboard window
			dashboard = Dash_board(self.master)
			# self.master.deiconify()
			# print(self.username.get())
			# print(self.password.get())
	def production_open(self):
		window = Production(self.master, x1=50, y1=50, x2=150, y2=150)
