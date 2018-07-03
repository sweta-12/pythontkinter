from tkinter import *
from production import Production
class Menu(Toplevel):
	def __init__(self,master=None):
		self.master = master
		self.option_menu = Toplevel(master)
		self.frame = Frame(self.option_menu)

		self.pr_button = Button(self.option_menu,text="Production",command=self.startpr)
		self.pr_button.pack()

		self.re_button = Button(self.option_menu,text="Reproduction",command=self.startre)
		self.re_button.pack()

		self.option_menu.geometry('500x400')

	def startpr(self):
		self.option_menu.withdraw()
		self.window = Production(self.master, x1=100, y1=100)
	def startre(self):
		self.option_menu.withdraw()
		self.window = Reproduction(self.master)
		self.master.deiconify()
