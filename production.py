from tkinter import *

class Production(Toplevel):
	def __init__(self,master,**params):
		self.testcase_master = Toplevel(master)
		self.master = master
		self.x1 = params['x1']
		self.y1 = params['y1']
		#self.x2 = params['x2']
		#self.y2 = params['y2']
		# self.canvas = master
		self.canvas = Canvas(self.testcase_master, width = 300, height = 200)
		#self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
		#def run_prg(self):
		for i in range(1,3):
			#c=2
			j=i
			#print(i)
			for j in range(0,4):
				print(j)
				self.reps(j)  #yaha pe na loop ka last value bas pass hora hai..baki sb to skip hora hai
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

if __name__ == '__main__':
	main()

