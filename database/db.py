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
		
		#test types
		testsql="CREATE TABLE IF NOT EXISTS test_types( id int, age_limit int, intervals int, replicate int)"
		self.cursor.execute(testsql)
		
		#operations table
		operationssql = "CREATE TABLE IF NOT EXISTS operations( id int, user_id int, replicate int, production_time int, reproduction_time int, early_time int, delay_time, type char)"
		self.cursor.execute(operationssql)

		self.db.commit()

	def select(self):
		pass

	def save(self):
		pass

dbObj = MindClockDb()