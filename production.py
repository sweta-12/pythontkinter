from tkinter import *
from time import *


class Production(Toplevel):
	def __init__(self,master):
		self.testcase_master = Toplevel(master)
		self.master = master
		#self.x1 = params['x1']
		#self.y1 = params['y1']
		#self.x2 = params['x2']
		#self.y2 = params['y2']
		# self.canvas = master
		self.canvas = Canvas(self.testcase_master, width = 300, height = 200)
		def reps()
				self.canvas.create_oval(200,200,70,70,fill='red')
		#self.draw(event)
				self.canvas.create_text(134,134,text="5",fill="white",font=("tahoma",60))
				self.canvas.pack()
				self.testcase_master.bind("<space>", self.hide_ball)
				#self.lbl = Label(self.testcase_master,text="Wait")
				#self.lbl.pack()
				#self.lbl.after(3000,self.lbldes) 
				print(j)
		self.time.sleep(4)
				
				

		self.testcase_master.protocol("WM_DELETE_WINDOW",self.cancel)

	

	
	

	def flash(self):
		self.lbl = Label(self.testcase_master,text="Wait")
		self.lbl.pack()
        #bg = self.cget('background')
        #fg = self.cget('foreground')
        #self.configure(background=fg,foreground=bg)
		self.lbl.after(3000,self.lbldes) 
	def lbldes(self):
		self.lbl.destroy()
		
		
	def hide_ball(self,event=None):
		self.canvas.destroy()
		
		

	def cancel(self):
		self.testcase_master.destroy()
		self.master.deiconify()

if __name__ == '__main__':
	main()

