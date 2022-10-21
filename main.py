import mysql.connector as connector

db = connector.connect(
	host="localhost",
	username="root",
	passwd="1234"
	)

cur=db.cursor()


def welcome_():
	print(
		"""
		----------BANKING SYSTEM PROJECT----------
		PROJECT MADE BY:- RACHIT HOODA
		CLASS:- XII A SCIENCE
		"""
		)
	print(f"using Database {bank}")


def task_():
	print("""
		1.create account
		2.close account
		3.deposit
		4.withdraw
		5.take loan
		6.Repay loan
		""")

	t = int(input("Enter Task Number: "))

	if t==1:
		pass
	elif t==2:
		pass
	elif t==3:
		pass
	elif t==4:
		pass
	elif t==5:
		pass
	elif t==6:
		pass
	else:
		print("Invalid Task")


#database check
cur.execute("SHOW DATABASES")
lst=cur.fetchall()
bank = 'bank'

if (bank,) in lst:
	print("Database Already Exists")
else:
	cur.execute("CREATE DATABASE Bank")
	print("Database Created")

db = connector.connect(
	host="localhost",
	username="root",
	passwd="1234",
	database='Bank'
	)

cur=db.cursor()



cur.execute("SHOW TABLES")
lst_ = cur.fetchall()
user = 'user'
if (user,) in lst_:
	print("Table Already Exists")
else:
	cur.execute("CREATE TABLE User (account_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age int, mobile_no int, amount int)")
	print("Table Created")

# welcome_()