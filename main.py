from tkinter import Frame, Tk, Menu, BOTH, Label, CENTER, Button, PhotoImage

from admin_login import AdminLogin

class MainWindow(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(fill=BOTH, expand=1)
		# heder text
		header = Label(self, text="Mind Clock", anchor=CENTER, justify=CENTER, fg="blue", pady=20)
		header.pack()

		# Admin and user button section
		adminBtn = Button(self, text="Admin", command=self.init_admin_login, width=7)
		adminBtn.place(x=130, y=60)

		testBtn = Button(self, text="User", command=self.init_test, width=7)
		testBtn.place(x=200, y=60)
		# End

	def init_admin_login(self):
		login = AdminLogin(self)

	def init_test(self):
		pass

root = Tk()
root.title("Mind Clock")
root.geometry("400x200")
root.resizable(width=False, height=False)
main = MainWindow(root)
root.mainloop()