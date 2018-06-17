from tkinter import Label, Button, Toplevel, Entry, Frame


class UserLogin(Toplevel):
	def __init__(self, master):
		self.master = master
		self.userlogin_master = Toplevel(master)

		self.frame = Frame(self.userlogin_master)
		self.username = Entry(self.userlogin_master)
		self.username.pack()

		self.password = Entry(self.userlogin_master, show="*")
		self.password.pack()

		self.login_button = Button(self.userlogin_master, text="Login", command=self.login)
		self.login_button.pack()
		self.login_button.config(bg='navy', fg='white', bd=4) 

		self.login_button = Button(self.userlogin_master, text="Cancel", command=self.cancel)
		self.login_button.pack()
		self.login_button.config(bg='red', fg='white', bd=4) 

		self.frame.pack()

		self.userlogin_master.protocol("WM_DELETE_WINDOW",self.cancel)
		self.userlogin_master.bind('<Return>', self.login)

	def cancel(self):
		self.userlogin_master.destroy()
		self.master.deiconify()

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