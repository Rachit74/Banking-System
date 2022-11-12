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
	pass_ = input("Passoword: ")

	cur.execute("INSERT INTO User(name, age, mobile_no,amount, acc_pass) VALUES(%s,%s,%s,%s,%s)", (name,age,mobile,amt,pass_))
	db.commit()
	cur.execute("SELECT account_id FROM User WHERE name=%s", (name,))
	for x in cur:
		id_=x
	print(f"ACCOUNT CREATED YOUR ACCOUNT ID IS {id_} AND PASSWORD IS {pass_}")

def delete_account():
	id_1 = input("Enter id: ")
	passw_ = input("Enter Password: ")
	cur.execute("SELECT acc_pass FROM User WHERE account_id = %s", (id_1,))
	for x in cur:
		pass_=str(x)
	pass_2 = pass_[2:-3]
	if passw_ == pass_2:
		cur.execute("DELETE FROM User WHERE account_id=(%s)", (id_1,))
		db.commit()
		print("Account Deleted")
	else:
		print("Invalid Password")

def deposit():
	id_1 = input("Enter id: ")
	passw_ = input("Enter Passoword: ")
	cur.execute("SELECT acc_pass FROM User WHERE account_id = %s", (id_1,))
	for x in cur:
		pass_=str(x)
	pass_2 = pass_[2:-3]
	if passw_ == pass_2:
		amt = int(input("Enter Amount to deposit: "))
		cur.execute("UPDATE User SET amount = amount + %s WHERE account_id = %s", (amt,id_1,))
		db.commit()
		print("Amount Deposited")
	else:
		print("Invalid Password!")

def withdraw():
	id_1 = input("Enter id: ")
	passw_ = input("Enter Password: ")
	cur.execute("SELECT acc_pass FROM User WHERE account_id = %s", (id_1,))
	for x in cur:
		pass_=str(x)
	pass_2 = pass_[2:-3]
	if passw_ == pass_2:
		amt = int(input("Enter Amount to deposit: "))
		cur.execute("UPDATE User SET amount = amount - %s WHERE account_id = %s", (amt,id_1,))
		db.commit()
		print("Amount withdrawn")
	else:
		print("Invalid Password")

def account_info():
	id_1 = input("Enter id: ")
	passw_ = input("Enter Password: ")
	cur.execute("SELECT acc_pass FROM User WHERE account_id = %s", (id_1,))
	for x in cur:
		pass_=str(x)
	pass_2 = pass_[2:-3]
	if passw_ == pass_2:
		cur.execute("SELECT * FROM User WHERE account_id=(%s)", (id_1,))
		for x in cur:
			print(x)
	else:
		print("Invalid Password")


def welcome_():
	print(
		"""
		----------BANKING SYSTEM PROJECT----------
		PROJECT MADE BY:- Rachit Hooda, Pranay Tiwari, Anuj Gurjar, Sahil Yadav
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
	cur.execute("CREATE TABLE User (account_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age int, mobile_no int, amount int, acc_pass VARCHAR(50))")
	print("Table Created")



welcome_()
task_()
