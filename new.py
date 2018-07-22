from tkinter import *
root = Tk()
for i in range(1,101):
	f = i*i
	a = (str(f)+" ")
	l = Label(root, text=a)
	l.pack()
root.mainloop()