from tkinter import *
 
from tkinter import ttk


class Dash_board(Toplevel):

	def __init__(self,master=None):
		self.master = master
		self.dashboard_master = Toplevel(master)

		
 
		self.dashboard_master.title("DASHBOARD")
 
		tab_control = ttk.Notebook(self.dashboard_master)
 
		tab1 = ttk.Frame(tab_control)
 
		tab2 = ttk.Frame(tab_control)
 
		tab_control.add(tab1, text='TESTCASE')
		tab_control.add(tab2, text='RECORD')

		lbl1=Label(tab1, text= 'AGE',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
		lbl1.grid(column=0, row=0)

		lbl1=Label(tab1, text= 'production interval',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
		lbl1.grid(column=0, row=1)
		lbl1=Label(tab1, text= ' P replication',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
		lbl1.grid(column=0, row=2)
		lbl1=Label(tab1, text= 'reproduction interval',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
		lbl1.grid(column=0, row=3)
		lbl1=Label(tab1, text= 'R replication',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
		lbl1.grid(column=0, row=4)

		e1 = Entry(tab1)
		e2 = Entry(tab1)
		e3 = Entry(tab1)
		e4 = Entry(tab1)

		e1.grid(row=1, column=1)
		e2.grid(row=2, column=1)
		e3.grid(row=3, column=1)
		e4.grid(row=4, column=1)


		lbl2 = Label(tab2, text= 'label2',padx=5, pady=5)
		lbl2.grid(column=0, row=0)
		tab_control.pack(expand=1, fill='both')

		logout_button = Button(self.dashboard_master, text="Logout", command=self.logout)
		logout_button.pack()

		self.dashboard_master.protocol("WM_DELETE_WINDOW",self.logout)

	def logout(self):
		self.master.deiconify()
		self.dashboard_master.destroy()