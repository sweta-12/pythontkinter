from tkinter import Label, Tk, Button, Entry, Frame, PhotoImage, RIGHT, LEFT,BOTH,CENTER


from admin_login import AdminLogin
from user_login import UserLogin
#class MainWindow():
	#def __init__(self, master=None):
		#self.master = master

		#self.frame = Frame(self.master)

		#self.label = Label(self.master, text="Welcome to the Mind Clock Game")
		#self.label.pack()

		#self.admin_button = Button(self.master, text="Admin", command=self.admin_window,width=7)
		#admin_button.place(x=130, y=60)

		#self.user_button = Button(self.master, text="User", command=self.user_window)
		#user_button.place(x=130, y=60)
class MainWindow(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		# 		self.pack(fill=BOTH, expand=1)
		# 		# heder text
		# 		header = Label(self, text="Mind Clock", anchor=CENTER, justify=CENTER, fg="blue", pady=20)
		# 		header.pack()

		# 		# Admin and user button section
		# 		adminBtn = Button(self, text="Admin", command=self.admin_window, width=7)
		# 		adminBtn.place(x=160, y=60)

		# 		testBtn = Button(self, text="User", command=self.user_window, width=7)
		# 		testBtn.place(x=230, y=60)

		# 		quitBtn = Button(self, text="Exit", command=self.quit,width=7)
		# 		quitBtn.place(x=190, y=120)
		# 		self.pack()
		# =======
		self.frame = Frame(self.master)

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
		#>>>>>>> 54f09538245b8685a6fc16011d3290a3926fab77

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