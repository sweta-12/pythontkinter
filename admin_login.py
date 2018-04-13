from tkinter import Toplevel, Button, Frame

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
		self.center()
		self.geometry("300x200")
		self.title("Admin Login")
		button = Button(self, text="submit").grid(row=2, column=2)