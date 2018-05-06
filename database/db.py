import sqlite3

class MindClockDb:
	def __init__(self):
		self.db = sqlite3.connect("mindclock.db")
		self.cursor = self.db.cursor()
		# create tables
		self.init_db()

	def init_db(self):
		# admin table create
		adminsql = "CREATE TABLE IF NOT EXISTS admins( id int, username text, password text)"
		self.cursor.execute(adminsql)
		# users table
		userssql = "CREATE TABLE IF NOT EXISTS users( id int, fname text, lname text, age int, weight int, height int)"
		self.cursor.execute(userssql)
		self.db.commit()

	def __del__(self):
		self.cursor.close()
		self.db.close()

	def select(self):
		pass

	def save(self):
		pass

dbObj = MindClockDb()