import sqlite3

class MindClockDb:
	def __init__(self):
		self.db = sqlite3.connect("mindclock.db")
		self.cursor = self.db.cursor()
		self.cursor.row_factory = sqlite3.Row
		# create tables
		self.init_db()

	# init database structure
	def init_db(self):

		self.create_table("CREATE TABLE IF NOT EXISTS admins( id INTEGER PRIMARY KEY AUTOINCREMENT , username TEXT, password TEXT)")
		self.create_table("CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY AUTOINCREMENT , firstname TEXT , lastname TEXT, age int, weight TEXT, height TEXT, gender TEXT, userid TEXT, bmi TEXT)")
		self.create_table("CREATE TABLE IF NOT EXISTS test_types( id INTEGER  PRIMARY KEY AUTOINCREMENT , age_limit int, intervals int, replicate int)")
		self.create_table("CREATE TABLE IF NOT EXISTS operations( id INTEGER PRIMARY KEY AUTOINCREMENT , user_id int, replicate int, production_time int, reproduction_time int, early_time int, delay_time, type char)")

		# self.create_admin()

	def create_table(self, sql):
		self.cursor.execute(sql)
	# Read
	def select(self, sql):
		try:
			return self.cursor.execute(sql)
		except sqlite3.OperationalError as e:
			print(e)

	def single_record(self):
		return self.cursor.fetchone()

	# Insert into table
	def insert(self, sql):
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except sqlite3.OperationalError as e:
			print(e)

	def update(self, sql):
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except sqlite3.OperationalError as e:
			print(e)

	def delete(self, sql):
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except sqlite3.OperationalError as e:
			print(e)


	def __del__(self):
		self.cursor.close()
		self.db.close()

if __name__ == "__main__":
	dbObj = MindClockDb()

# dbObj.select("SELECT * FROM admins")
	# row = dbObj.single_record()

# print(dict(row))

# result = dbObj.insert("INSERT INTO admins(username, password) VALUES('admin123', 'admin345')")
# result = dbObj.delete("DELETE FROM admins WHERE id=5")
# result = dbObj.update("UPDATE admins SET username='admin_root' WHERE id=4")
# if(result):
# 	print("Update")
# for row in rows:
# 	print(dict(row))