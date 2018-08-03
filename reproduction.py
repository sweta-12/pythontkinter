from tkinter import *
import datetime
import time
from db import MindClockDb
from errors import McError
class Reproduction():
	def __init__(self,master , userdata):
		self.master = master
		self.testcase_master = Toplevel(master)
		self.testcase_master.protocol("WM_DELETE_WINDOW", self.mainwin)
		self.userdata=userdata

		self.db = MindClockDb(self.testcase_master)

		self.messages = McError()

		self.keypress=False

		sql1 = "DELETE FROM operations WHERE type=('{}') AND user_id=('{}')".format("Reproduction",self.userdata)
		if(self.db.delete(sql1)==False):
			self.messages.error("Error", "Something went wrong!")
		
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
		if (self.keypress == False) :
			self.start = time.time()
			self.keypress=True
		else :
			self.canvas.create_oval(200,200,70,70,fill='#6666ff')
			self.canvas.create_text(134,134,text="R",fill="white",font=("tahoma",30))
			self.canvas.pack()
		
		self.testcase_master.bind("<KeyRelease>", self.hide_ball)
		#self.now2 = datetime.datetime.now()
		


	def hide_ball(self,event=None):
		self.canvas.delete(ALL)
		#self.end=float(self.now2.isoformat())
		self.keypress=False
		self.end = time.time()
		print("start time",self.start)
		print("end time",self.end)
		self.getdiff= self.end-self.start
		print("Difference",self.getdiff)
		sql="INSERT INTO operations(user_id, replicate, production_time, reproduction_time, result_time, type) VALUES('{}','{}','{}','{}','{}','{}')".format(self.userdata,1,None,3,self.getdiff,"Reproduction")

		if(self.db.insert(sql)==False):
			self.messages.error("Error", "Something went wrong!")

	def clear(self):
		self.canvas1.destroy()


		




