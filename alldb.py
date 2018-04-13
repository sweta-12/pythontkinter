import sqlite3

db = sqlite3.connect("mindclock.db")
cursor = db.cursor()
cursor.execute("drop table if exists users")
cursor.execute("create table users( id int, fname text, lname text, age int, weight int, height int)")
cursor.execute("drop table if exists test_types")
cursor.execute("create table test_types( id int, age_limit int, intervals int, replicate int)")
cursor.execute("drop table if exists admins")
cursor.execute("create table admins( id int, username text, password text)")
cursor.execute("drop table if exists operations")
cursor.execute("create table operations( id int, user_id int, replicate int, production_time int, reproduction_time int, early_time int, delay_time, type char)")