from tkinter import *
 
from tkinter import ttk


class Dash_board(Toplevel):

	def __init__(self,master=None):
		#Toplevel.__init__(self, master)
		#self.toplevel = master
		window = Tk()
		#tab1=Tk()
 
		window.title("DASHBOARD")
 
		tab_control = ttk.Notebook(window)
 
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

#lbl1 = Label(tab1, text= 'R replication',anchor=CENTER, justify=CENTER, fg="black", padx=5, pady=5)
#lbl1.grid(column=0, row=4)

#def init_TESTCASE(self):
		#self.pack(fill=BOTH, expand=1)
		# heder text
		#header =lbl1(self, text="AGE", anchor=CENTER, justify=CENTER, fg="blue", pady=20)
		#header.pack()
		lbl2 = Label(tab2, text= 'label2',padx=5, pady=5)
		lbl2.grid(column=0, row=0)
		tab_control.pack(expand=1, fill='both')
 
		window.mainloop()