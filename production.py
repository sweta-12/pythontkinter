from tkinter import Toplevel, Label

import sys
import time
from datetime import datetime
from db import MindClockDb

class Production:
	def __init__(self, master, userdata):

		# logged in userdata
		self.userdata = userdata
		self.productioncounter = 0
		self.replicationcounter = 1

		self.production_master = Toplevel(master)
		self.production_master.protocol("WM_DELETE_WINDOW", sys.exit)
		self.production_master.title("Production")
		self.production_master.focus_set()

		self.db = MindClockDb()
		# self.production_master.attributes('-fullscreen', True)
		self.init_production()

	def init_production(self):
		set = {'font': 'Times 70 bold'}
		self.get_production_intervals()

		self.production_timer = Label(self.production_master, text=self.time[self.productioncounter], **set)
		self.production_timer.pack(padx=200, pady=320)
		self.production_master.bind('<space>', self.get_production_event)


	def get_production_intervals(self):
		# self.time = []
		# self.event = []
		# self.data = self.db.select("SELECT ")
		data = self.db.select("SELECT id, intervals, replicate, type FROM test_types WHERE type='P'")
		data = data.fetchone()
		intervals = dict(data)
		self.time = intervals['intervals'].split('-')
		self.replicate = intervals['replicate']

	def get_production_event(self, event):
		time.sleep(2)

		self.productioncounter += 1
		print(self.replicationcounter)
		# check replication is
		if self.replicationcounter > self.replicate:
			sys.exit()

		# change text on key press
		try:
			self.production_timer.config(text=self.time[self.productioncounter])
		except IndexError as e:
			self.replicationcounter += 1
			self.productioncounter = 0

# from tkinter import *

# class Production(Toplevel):
# 	def __init__(self,master,**params):
# 		self.testcase_master = Toplevel(master)
# 		self.master = master
# 		self.x1 = params['x1']
# 		self.y1 = params['y1']
# 		#self.x2 = params['x2']
# 		#self.y2 = params['y2']
# 		# self.canvas = master
# 		self.canvas = Canvas(self.testcase_master, width = 300, height = 200)
# 		#self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
# 		#def run_prg(self):
# 		for i in range(1,3):
# 			#c=2
# 			j=i
# 			#print(i)
# 			for j in range(0,4):
# 				print(j)
# 				self.reps(j)  #yaha pe na loop ka last value bas pass hora hai..baki sb to skip hora hai
# 			#c=c+1

				
				

# 		self.testcase_master.protocol("WM_DELETE_WINDOW",self.cancel)

	

# 	def reps(self,j):

# 		if(j==1):
# 			self.gif1 = PhotoImage(file='assets//rep4.gif')
# 			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
# 			self.canvas.after(2000, self.hide_ball)
# 			self.canvas.pack()
			

# 		elif(j==2):
# 			self.gif1 = PhotoImage(file='assets//admin.gif')
# 			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
# 			self.canvas.after(4000, self.hide_ball)
# 			self.canvas.pack()
			
# 		elif(j==3):
# 			self.gif1 = PhotoImage(file='assets//rep6.gif')
# 			self.canvas.create_image(self.x1, self.y1, image=self.gif1, anchor=CENTER)
# 			self.canvas.after(6000, self.hide_ball)
# 			self.canvas.pack()
			
	

# 	def flash(self):
# 		self.lbl = Label(self.testcase_master,text="Wait")
# 		self.lbl.pack()
#         #bg = self.cget('background')
#         #fg = self.cget('foreground')
#         #self.configure(background=fg,foreground=bg)
# 		self.lbl.after(3000,self.lbldes) 
		
# 	def lbldes(self):
# 		self.lbl.destroy()
		
		
# 	def hide_ball(self):
# 		self.canvas.destroy()
# 		self.flash()

# 	def cancel(self):
# 		self.testcase_master.destroy()
# 		self.master.deiconify()

# if __name__ == '__main__':
# 	main()




# from tkinter import *
# from time import sleep


# from db import MindClockDb

# from errors import McError

# import sqlite3

# class Production():
# 	def __init__(self,master):
# 		self.master = master
# 		self.testcase_master = Toplevel(master)
		


# 		#self.x1 = params['x1']
# 		#self.y1 = params['y1']
# 		#self.x2 = params['x2']
# 		#self.y2 = params['y2']
# 		# self.canvas = master
		
# 		self.messages = McError()

# 		self.db = sqlite3.connect('mindclock.db')
# 		self.cursor=self.db.cursor()

# 		self.cursor.execute("SELECT replicate FROM test_types WHERE type='Production'")
# 		self.replicate=self.cursor.fetchone()
# 		self.replicate=int(self.replicate[0])
# 		print("No. of replications : ",self.replicate)

# 		self.cursor.execute("SELECT intervals FROM test_types WHERE type='Production'")
# 		self.intervals=self.cursor.fetchone()
# 		self.intervals=int(self.intervals[0])
# 		print("No. of intervals : ",self.intervals)

# 		# self.canvas = Canvas(self.testcase_master, width = 300, height = 200)

# 		#self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
# 		#

# 		#for i in range(1,self.replicate+1):
			
# 			#for j in range(1,self.intervals+1):
# 		# for i in range(1,self.replicate+1):
# 		# 	for j in range(1,self.intervals+1):
# 		# 		sql=("SELECT interval FROM production_interval WHERE interval_no='{}'").format(j)
# 		# 		self.cursor.execute(sql)
# 		# 		self.interval=self.cursor.fetchone()
# 		# 		self.interval=int(self.interval[0])
# 		# 		print("interval : ",self.interval)
# 		# 		self.canvas.create_oval(200,200,70,70,fill='#6666ff')
# 		# 		s = str(self.interval)
# 		# 		self.canvas.create_text(134,134,text=s,fill="white",font=("tahoma",60))
# 		# 		self.canvas.pack()
# 		# 		self.testcase_master.bind("<space>", self.hide_ball)

# 		self.testcase_master.protocol("WM_DELETE_WINDOW",self.cancel)


# 	#def flash(self):
# 	#	self.lbl = Label(self.testcase_master,text="Wait")
# 	#	self.lbl.pack()
#         #bg = self.cget('background')
#         #fg = self.cget('foreground')
#         #self.configure(background=fg,foreground=bg)
# 	#	self.lbl.after(3000,self.lbldes) 
# 	def lbldes(self):
# 		self.lbl.destroy()


# 	def hide_ball(self,event=None):
# 		self.canvas.destroy()




# 	def cancel(self):
# 		self.testcase_master.destroy()
# 		self.master.deiconify()

# # if __name__ == '__main__':
# # 	main()

