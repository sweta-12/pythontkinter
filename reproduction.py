from tkinter import *

class Reproduction(Toplevel):
	def __init__(self,master=None):
		self.master = master
		self.testcase_master = Toplevel(master)
		self.testcase_master.bind("<space>", self.show_ball)


		
		self.canvas = Canvas(self.testcase_master, width = 350, height = 300)
		self.canvas.pack()

		#img = PhotoImage(file="assets/clock.gif")
		#self.canvas.create_image(60,40, anchor=NW, image=img)
	

	def show_ball(self,event=None):
		
		self.canvas.create_oval(200,200,70,70,fill='#6666ff')
		self.canvas.create_text(134,134,text="R",fill="white",font=("tahoma",30))
		self.canvas.pack()
		self.testcase_master.bind("<KeyRelease>", self.hide_ball)

	def hide_ball(self,event=None):
		self.canvas.destroy()




