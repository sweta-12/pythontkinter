from tkinter import messagebox

class McError:
	def __init__(self, master=None):
		pass

	def error(self,head, msg):
		messagebox.showerror(head, msg)

	def success(self, head, msg):
		messagebox.showinfo(head,msg)