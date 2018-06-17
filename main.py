from tkinter import Label, Tk, Button, Entry, Frame, PhotoImage, RIGHT, LEFT

from admin_login import AdminLogin
from user_login import UserLogin
class MainWindow():
	def __init__(self, master=None):
		self.master = master

		self.frame = Frame(self.master)

		self.label = Label(self.master, text="Mind Clock")

		img=PhotoImage(file="assets/admin.gif")
		img1=PhotoImage(file="assets/user.gif")

		self.label = Label(self.master, text="Welcome to the Mind Clock Game",font="papyrus")
		self.label.config(bg='#34af23')
		self.label.pack()

		self.admin_button = Button(self.master, image=img, text= "admin", command=self.admin_window)
		self.admin_button.image=img
		self.admin_button.config(bg='#34af23')
		self.admin_button.pack(side=LEFT)

		self.user_button = Button(self.master, image=img1, text= "user", command=self.user_window)
		self.user_button.image=img1
		self.user_button.config(bg='#34af23')
		self.user_button.pack(side=RIGHT)

		#self.quit = Button(self.master, text="Exit", command=master.quit)
		#self.quit.pack()
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
root.config(bg='#34af23')
root.title("Mindclock")
main_window = MainWindow(root)
root.mainloop()