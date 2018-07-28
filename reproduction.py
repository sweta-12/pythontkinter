from tkinter import *
import datetime
import time
class Reproduction():
	def __init__(self,master=None):
		self.master = master
		self.testcase_master = Toplevel(master)
		self.testcase_master.protocol("WM_DELETE_WINDOW", self.mainwin)
		
		self.canvas1 = Canvas(self.testcase_master, width = 350, height = 300)
		self.canvas1.pack()
		self.canvas1.create_oval(200,200,70,70,fill='#6666ff')
		self.canvas1.create_text(134,134,text="R",fill="white",font=("tahoma",30))
		self.canvas1.after(3000,self.clear)
		

		self.canvas = Canvas(self.testcase_master, width = 350, height = 300)
		self.canvas.pack()
		self.testcase_master.bind("<space>", self.show_ball)
		self.testcase_master.geometry('500x400')
		#self.now1 = datetime.datetime.now()
		
		
	def mainwin(self):
		self.master.deiconify()
		self.testcase_master.destroy()
		
	def show_ball(self,event=None):
		#self.start=float(self.now1.isoformat())
		self.start = time.time()
		self.canvas.create_oval(200,200,70,70,fill='#6666ff')
		self.canvas.create_text(134,134,text="R",fill="white",font=("tahoma",30))
		self.canvas.pack()
		
		self.testcase_master.bind("<KeyRelease>", self.hide_ball)
		#self.now2 = datetime.datetime.now()
		


	def hide_ball(self,event=None):
		self.canvas.destroy()
		#self.end=float(self.now2.isoformat())
		self.end = time.time()
		print("start time",self.start)
		print("end time",self.end)
		self.getdiff= self.end-self.start
		print("Difference",self.getdiff)

	def clear(self):
		self.canvas1.destroy()


		




