from tkinter import *

from db import MindClockDb

from errors import McError


class insert_interval():

	def __init__(self, master, interval_no, type):

		self.master = master
		self.interval_master = Toplevel(master)

		self.messages = McError()

		self.interval_no=int(interval_no)
		self.type=type

		if(self.interval_no == 0):
			self.interval_master.destroy()
			self.master.deiconify()
		else:

			label_Interval = Label(self.interval_master, text="Interval ")

			self.entry_Interval =Entry(self.interval_master)

			label_Interval.grid(row=0,sticky=E)

			self.entry_Interval.grid(row=0,column=1)

			if(self.interval_no==1):
				next_button = Button(self.interval_master, text="Finish", command=self.call)
			else:
				next_button = Button(self.interval_master, text="Next", command=self.call)
			
			next_button.grid(columnspan=2)

			self.interval_master.mainloop()

	def call(self):
		self.insert(self.type, self.interval_no, self.entry_Interval.get() ,self.interval_master)

	def insert(self, type, interval_no, interval_time, interval_master):
		
		db = MindClockDb(self.master)

		if(type == "Production"):
			#sql="DELETE FROM production_interval"
			sql1="INSERT INTO production_interval(interval_no, interval) VALUES('{}','{}')".format(interval_no,interval_time)
		if(type == "Reproduction"):
			#sql="DELETE FROM reproduction_interval"
			sql1="INSERT INTO reproduction_interval(interval_no, interval) VALUES('{}','{}')".format(interval_no,interval_time)

		if(db.insert(sql1)):
			self.messages.success("Success", "Saved Successfully!")
		else:
			interval_master.withdraw()
			self.messages.error("Error", "Something went wrong!")
			interval_master.deiconify()
		self.interval_no=self.interval_no-1
		self.interval_master.destroy()
		self.__init__(self.master, self.interval_no, self.type)