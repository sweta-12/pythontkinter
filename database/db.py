import sqlite3

class MindClockDb:
	def __init__(self):
		db = sqlite3.connect("mindclock.db")
		self.cursor = db.cursor()

	def select(self):
		pass

	def save(self):
		pass