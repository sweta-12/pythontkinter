from tkinter import *
from time import sleep


from db import MindClockDb

from errors import McError

import sqlite3

class Production():
	def __init__(self,master):
		self.master = master
		self.testcase_master = Toplevel(master)
		


		#self.x1 = params['x1']
		#self.y1 = params['y1']
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

		# self.canvas = Canvas(self.testcase_master, width = 300, height = 200)

		#self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
		#

		#for i in range(1,self.replicate+1):
			
			#for j in range(1,self.intervals+1):
		# for i in range(1,self.replicate+1):
		# 	for j in range(1,self.intervals+1):
		# 		sql=("SELECT interval FROM production_interval WHERE interval_no='{}'").format(j)
		# 		self.cursor.execute(sql)
		# 		self.interval=self.cursor.fetchone()
		# 		self.interval=int(self.interval[0])
		# 		print("interval : ",self.interval)
		# 		self.canvas.create_oval(200,200,70,70,fill='#6666ff')
		# 		s = str(self.interval)
		# 		self.canvas.create_text(134,134,text=s,fill="white",font=("tahoma",60))
		# 		self.canvas.pack()
		# 		self.testcase_master.bind("<space>", self.hide_ball)

		self.testcase_master.protocol("WM_DELETE_WINDOW",self.cancel)


	#def flash(self):
	#	self.lbl = Label(self.testcase_master,text="Wait")
	#	self.lbl.pack()
        #bg = self.cget('background')
        #fg = self.cget('foreground')
        #self.configure(background=fg,foreground=bg)
	#	self.lbl.after(3000,self.lbldes) 
	def lbldes(self):
		self.lbl.destroy()


	def hide_ball(self,event=None):
		self.canvas.destroy()




	def cancel(self):
		self.testcase_master.destroy()
		self.master.deiconify()

# if __name__ == '__main__':
# 	main()

