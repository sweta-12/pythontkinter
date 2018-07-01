from tkinter import *
 
from tkinter import ttk

from db import MindClockDb

from errors import McError


class Dash_board(Toplevel):

	def __init__(self,master=None):
		self.master = master
		self.dashboard_master = Toplevel(master)
		
		self.dashboard_master.title("DASHBOARD")

		self.messages = McError()
 		
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

		self.save_button = Button(self.dashboard_master, text="Save", command=self.save)
		self.save_button.grid(columnspan=2)

		self.logout_button = Button(self.dashboard_master, text="Logout", command=self.logout)
		self.logout_button.grid(columnspan=2)

		self.dashboard_master.protocol("WM_DELETE_WINDOW",self.logout)

	def logout(self):
		self.master.deiconify()
		self.dashboard_master.destroy()
	def save(self):
		db = MindClockDb(self.dashboard_master)
		
		type = self.type.get()
		Replication=self.entry_Replication.get()
		Interval=self.entry_Intervals.get()

		sql = "INSERT INTO test_types(type, replicate, intervals) VALUES('{}','{}','{}')".format(type, Replication, Interval)
		sql1 = "DELETE FROM test_types WHERE type=('{}')".format(type)

		if(db.delete(sql1) & db.insert(sql)):
			self.messages.success("Success", "Saved Successfully!")
			self.dashboard_master.destroy()
			self.master.deiconify()
		else:
			self.dashboard_master.withdraw()
			self.messages.error("Error", "Something went wrong!")
			self.dashboard_master.deiconify()