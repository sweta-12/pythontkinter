from tkinter import *
 
from tkinter import ttk

from db import MindClockDb

from errors import McError

from insert_interval import insert_interval

import sqlite3

import xlsxwriter

class Dash_board(Toplevel):

	def __init__(self,master=None):
		self.master = master
		self.dashboard_master = Toplevel(master)
		
		self.dashboard_master.title("DASHBOARD")

		self.messages = McError()

		self.db = sqlite3.connect("mindclock.db")
		self.cursor = self.db.cursor()

		self.menubar = Menu(self.dashboard_master)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Generate Report", command=self.generate)
		self.menubar.add_cascade(label="File", menu=self.filemenu)

 		
		self.label_Type = Label(self.dashboard_master, text="Test case type")
		self.label_Replication = Label(self.dashboard_master, text="Number of Replications")
		self.label_Intervals = Label(self.dashboard_master, text="Number of Intervals")
		
		self.type = StringVar()
		self.entry_Type_pro=Radiobutton(self.dashboard_master,variable=self.type,text="Production",value="Production")
		self.entry_Type_repro=Radiobutton(self.dashboard_master,variable=self.type,text="Reproduction",value="Reproduction")
		self.entry_Replication = Entry(self.dashboard_master)
		self.entry_Intervals =Entry(self.dashboard_master)

		self.label_Type.grid(row=0, sticky=E)
		self.label_Replication.grid(row=1,sticky=E)
		self.label_Intervals.grid(row=2,sticky=E)
        
		self.entry_Type_pro.grid(row=0, sticky=W+W+E, column=1)
		self.entry_Type_repro.grid(row=0, sticky=W+S, column=3)
		self.entry_Replication.grid(row=1, column=1)
		self.entry_Intervals.grid(row=2,column=1)

		self.save_button = Button(self.dashboard_master, text="Next", command=self.save)
		self.save_button.grid(columnspan=2)

		self.logout_button = Button(self.dashboard_master, text="Logout", command=self.logout)
		self.logout_button.grid(columnspan=2)

		self.dashboard_master.protocol("WM_DELETE_WINDOW",self.logout)
		self.dashboard_master.config(menu=self.menubar)

	def logout(self):
		self.master.deiconify()
		self.dashboard_master.destroy()
	def save(self):
		db = MindClockDb(self.dashboard_master)
		
		type = self.type.get()
		Replication=self.entry_Replication.get()
		Interval=self.entry_Intervals.get()

		sql = "INSERT INTO test_types(replicate, intervals, type) VALUES('{}','{}','{}')".format(Replication, Interval, type)
		sql1 = "DELETE FROM test_types WHERE type=('{}')".format(type)

		if(db.delete(sql1)):
			if(db.insert(sql)):
				self.messages.success("Success", "Saved Successfully!")
		else:
			dashboard_master.withdraw()
			self.messages.error("Error", "Something went wrong!")
			dashboard_master.deiconify()


	def generate(self):
		
		
		# sql="SELECT count(*) from users"
		# self.cursor.execute(sql)
		# result=self.cursor.fetchone()
		# result=result[0]

		usrftch=self.cursor.execute("SELECT DISTINCT user_id from operations")
		usr=self.cursor.fetchall()
		usr=list(sum(usr,()))
		print(len(usr))
		print(usr)
		for x in usr :
			str = "Generated Report/"+x+".xlsx"
			report = xlsxwriter.Workbook(str)
			sql="select replicate,production_time,reproduction_time,result_time,type from operations where user_id=('{}')".format(x)
			mysel=self.cursor.execute(sql)
			item=self.cursor.fetchall()
			worksheet = report.add_worksheet(x)
			worksheet.write('A1', 'REPLICATION')
			worksheet.write('B1', 'PRODUCTION TIME')
			worksheet.write('C1', 'REPRODUCTION TIME')
			worksheet.write('D1', 'RESULT TIME')
			worksheet.write('E1', 'TYPE')
			for i, row in enumerate(item):
				for j, value in enumerate(row):
					worksheet.write(i+1, j, item[i][j])
		report.close()
