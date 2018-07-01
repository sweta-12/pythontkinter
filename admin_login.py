from tkinter import Label, Button, Toplevel, Entry, Frame, Canvas

from admindashboard import Dash_board

from errors import McError

import sqlite3

class AdminLogin():
	def __init__(self, master):
		self.master = master
		self.adminlogin_master = Toplevel(master)

		self.db=sqlite3.connect('mindclock.db')
		self.cursor=self.db.cursor()

		self.messages = McError()

		self.frame = Frame(self.adminlogin_master)
		self.username = Label(self.adminlogin_master, text="Username")
		self.username = Entry(self.adminlogin_master)
		self.username.pack()
		self.password = Label(self.adminlogin_master, text="Password")
		self.password = Entry(self.adminlogin_master, show="*")
		self.password.pack()

		self.login_button = Button(self.adminlogin_master, text="Login", command=self.login,width=7)
		self.login_button.pack()
		self.login_button.config(fg='black', bd=4) 

		self.login_button = Button(self.adminlogin_master, text="Cancel", command=self.cancel)
		self.login_button.pack()
		self.login_button.config(fg='black', bd=4) 
		
		self.frame.pack()

		self.adminlogin_master.protocol("WM_DELETE_WINDOW",self.cancel)
		self.adminlogin_master.bind('<Return>', self.login)
		self.adminlogin_master.geometry('500x400')
		
	def cancel(self):
		self.adminlogin_master.destroy()
		self.master.deiconify()

	def login(self,event=None):
		# match username and password
		find_user = ('SELECT username,password FROM admins WHERE username = ? and password = ?')
		self.cursor.execute(find_user,[(self.username.get()),(self.password.get())])
		result = self.cursor.fetchone()
		if result:
			self.adminlogin_master.destroy()
			# call dashboard window
			dashboard = Dash_board(self.master)
		else:
			self.messages.error("Error","Invalid Username or Password")
			# self.master.deiconify()
			# print(self.username.get())
			# print(self.password.get())
	#.geometry('500x400')
	