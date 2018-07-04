from tkinter import *

from db import MindClockDb

from errors import McError

import sqlite3

class Production(Toplevel):
	def __init__(self,master,**params):
		self.testcase_master = Toplevel(master)
		self.master = master

		self.x1 = params['x1']
		self.y1 = params['y1']
		#self.x2 = params['x2']
		#self.y2 = params['y2']
		# self.canvas = master
		
		self.messages = McError()

		self.db = sqlite3.connect('mindclock.db')
		self.cursor=self.db.cursor()

		self.cursor.execute("SELECT replicate FROM test_types WHERE type='Production'")
		self.replicate=self.cursor.fetchone()
		self.replicate=int(self.replicate[0])
		print("No. of replications : ",self.replicate)

		self.cursor.execute("SELECT intervals FROM test_types WHERE type='Production'")
		self.intervals=self.cursor.fetchone()
		self.intervals=int(self.intervals[0])
		print("No. of intervals : ",self.intervals)

		self.canvas = Canvas(self.testcase_master, width = 300, height = 200)
		#self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
		#def run_prg(self):
		for i in range(1,self.replicate):
			for j in range(1,self.intervals+1):
				sql=("SELECT interval FROM production_interval WHERE interval_no='{}'").format(j)
				self.cursor.execute(sql)
				interval=self.cursor.fetchone()
				interval=int(interval[0])
				print("interval : ",interval)

				print(j)
				# self.reps(j)  #yaha pe na loop ka last value bas pass hora hai..baki sb to skip hora hai
			#c=c+1

				
				

		self.testcase_master.protocol("WM_DELETE_WINDOW",self.cancel)

	

	def reps(self,j):

		if(j==1):
			self.gif1 = PhotoImage(file='assets//rep4.gif')
			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
			self.canvas.after(2000, self.hide_ball)
			self.canvas.pack()
			

		elif(j==2):
			self.gif1 = PhotoImage(file='assets//admin.gif')
			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
			self.canvas.after(4000, self.hide_ball)
			self.canvas.pack()
			
		elif(j==3):
			self.gif1 = PhotoImage(file='assets//rep6.gif')
			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
			self.canvas.after(6000, self.hide_ball)
			self.canvas.pack()
			
	

	def flash(self):
		self.lbl = Label(self.testcase_master,text="Wait")
		self.lbl.pack()
        #bg = self.cget('background')
        #fg = self.cget('foreground')
        #self.configure(background=fg,foreground=bg)
		self.lbl.after(3000,self.lbldes) 
	def lbldes(self):
		self.lbl.destroy()
		
		
	def hide_ball(self):
		self.canvas.destroy()
		self.flash()

	def cancel(self):
		self.testcase_master.destroy()
		self.master.deiconify()

# if __name__ == '__main__':
# 	main()

