from tkinter import Label, Tk, Button, Entry, Frame

from admin_login import AdminLogin
from user_login import UserLogin
class MainWindow():
	def __init__(self, master=None):
		self.master = master

		self.frame = Frame(self.master)

		self.label = Label(self.master, text="Welcome to the Mind Clock Game")
		self.label.pack()

		self.admin_button = Button(self.master, text="Admin", command=self.admin_window)
		self.admin_button.pack()

		self.user_button = Button(self.master, text="User", command=self.user_window)
		self.user_button.pack()

		self.quit = Button(self.master, text="Exit", command=master.quit)
		self.quit.pack()
		self.frame.pack()

	def admin_window(self):
		self.master.withdraw()
		self.adminwindow = AdminLogin(self.master)
		print("admin window")

	def user_window(self):
		self.master.withdraw()
		self.userwindow = UserLogin(self.master)
		print("user window")

root = Tk()
root.geometry('500x400')
root.config(bg='ivory')
root.title("Mindclock")
main_window = MainWindow(root)
root.mainloop()