import mysql.connector as connector

db = connector.connect(
	host="localhost",
	username="root",
	passwd="1234"
	)

cur=db.cursor()

"""
Query Functions
"""
def create_account():
	name = input("Enter Name: ")
	age = int(input("Enter Age: "))
	mobile = int(input("Enter Mobile Number: "))
	amt = int(input("Enter Amount: "))

	cur.execute("INSERT INTO User(name, age, mobile_no,amount) VALUES(%s,%s,%s,%s)", (name,age,mobile,amt))
	db.commit()

def delete_account():
	name = input("Enter Name: ")
	cur.execute("DELETE FROM User WHERE name=(%s)", (name,))
	print("Account Deleted")

def deposit():
	name = input("Enter Name: ")
	amt = int(input("Enter Amount to deposit: "))
	cur.execute("UPDATE User SET amount = amount + %s WHERE name = %s", (amt,name,))
	db.commit()
	print("Amount Deposited")

def withdraw():
	name = input("Enter Name: ")
	amt = int(input("Enter Amount to deposit: "))
	cur.execute("UPDATE User SET amount = amount - %s WHERE name = %s", (amt,name,))
	db.commit()
	print("Amount withdrawn")

def account_info():
	name = input("Enter Name: ")

	cur.execute("SELECT * FROM User WHERE name=(%s)", (name,))
	for x in cur:
		print(x)
	# pass


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
	while True:
		print("""
		----------Bank Options----------
		1.create account
		2.close account
		3.deposit
		4.withdraw
		5.Account Info
			""")

		t = input("Enter Task Number: ")

		if t==str(1):
			create_account()
		elif t==str(2):
			delete_account()
		elif t==str(3):
			deposit()
		elif t==str(4):
			withdraw()
		elif t==str(5):
			account_info()
		elif t=="q":
			break
		else:
			print("Invalid Task")
			continue



"""
Database check/Creating Database
Conneting with database
Table check/creating Table
"""

#database check
cur.execute("SHOW DATABASES")
lst=cur.fetchall()
bank = 'bank'

if (bank,) in lst:
	print("Database Already Exists")
else:
	cur.execute("CREATE DATABASE Bank")
	print("Database Created")

# connecting with database
db = connector.connect(
	host="localhost",
	username="root",
	passwd="1234",
	database='Bank'
	)

cur=db.cursor()


# checking table
cur.execute("SHOW TABLES")
lst_ = cur.fetchall()
user = 'user'
if (user,) in lst_:
	print("Table Already Exists")
else:
	cur.execute("CREATE TABLE User (account_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age int, mobile_no int, amount int)")
	print("Table Created")



welcome_()
task_()