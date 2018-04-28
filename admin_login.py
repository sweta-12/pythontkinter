from tkinter import Toplevel, Button, Frame, E, Label, Entry

# import admin_login(AdminLogin)
# from admin_login import AdminLogin

class AdminLogin(Toplevel):
	def __init__(self, master=None):
		Toplevel.__init__(self, master)
		self.toplevel = master
		
		self.init_login_section()

	def center(self):
		x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
		y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
		self.geometry("+%d+%d" % (x, y))


	def init_login_section(self):

		self.toplevel.hideWindow()

		self.center()
		self.geometry("300x200")
		self.title("Admin Login")
		# login action
		Label(self, text="Username").grid(row=0, sticky=E)
		Label(self, text="Password").grid(row=1, sticky=E)

		self.username=Entry(self).grid(row=0, column=1)
		self.password=Entry(self, show="*").grid(row=1, column=1)

		Button(self, text="Login", command=self._login).grid(row=2, columnspan=2)
		# password.grid(row=1, sticky=E)

	def _login(self):
		self.destroy()
		self.toplevel.showWindow()