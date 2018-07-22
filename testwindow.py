from tkinter import *
from production import Production
from reproduction import Reproduction
import sys

class TestWindow():
	def __init__(self, master=None):
		# Frame.__init__(self,master)
		self.master = Toplevel(master)
		#self.option_menu = Toplevel(master)
		#self.frame = Frame(self.option_menu)
		self.init_window()

	def init_window(self):

		self.frame = Frame(self.master)
		img=PhotoImage(file="assets/new prod.gif")
		img1=PhotoImage(file="assets/new repo.gif")

		self.production_button = Button(self.master, image=img, text= "production", command=self.production_window)
		self.production_button.image=img
		self.production_button.config(bg='#34af23')
		self.production_button.pack(padx=45, pady=60, side=LEFT)

		self.reproduction_button = Button(self.master, image=img1, text= "reproduction", command=self.reproduction_window)
		self.reproduction_button.image=img1
		self.reproduction_button.config(bg='#34af23')
		self.reproduction_button.pack(padx=45, pady=60,side=RIGHT)
	
		self.frame.pack()

		self.master.protocol("WM_DELETE_WINDOW",self.exit)

		#self.option_menu.geometry('500x400')

	def production_window(self):
		self.master.withdraw()
		self.window = Production(self.master)
		#self.testcase_master.withdraw()
		
	def reproduction_window(self):
		self.master.withdraw()
		self.window = Reproduction(self.master)
		#self.master.deiconify()
	def exit(self):
		sys.exit

	