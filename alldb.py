import sqlite3

#connecting with the database
db = sqlite3.connect("mindclock.db")
cursor = db.cursor()

#creating table users
cursor.execute("drop table if exists users")
cursor.execute("create table users( id int, fname text, lname text, age int, weight int, height int)")

#creating table for test
cursor.execute("drop table if exists test_types")
cursor.execute("create table test_types( id int, age_limit int, intervals int, replicate int)")

#creating table for admin data
cursor.execute("drop table if exists admins")
cursor.execute("create table admins( id int, username text, password text)")

#creating table for operations
cursor.execute("drop table if exists operations")
cursor.execute("create table operations( id int, user_id int, replicate int, production_time int, reproduction_time int, early_time int, delay_time, type char)")

