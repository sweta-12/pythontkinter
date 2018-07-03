from tkinter import *

class Reproduction(Toplevel):
	def __init__(self,master=None):
		self.testcase_master = Toplevel(master)
	

		
		self.canvas = Canvas(self.testcase_master, width = 350, height = 300)
		self.canvas.pack()

		img = PhotoImage(file="assets/clock.gif")
		self.canvas.create_image(60,40, anchor=NW, image=img)

		mainloop()


