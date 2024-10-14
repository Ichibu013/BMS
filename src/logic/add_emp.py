# To add employee details
from src.MySQLCon import mycur, mycon
from src.logic.space import space


def addemp():
	qry = "select * from employee;"
	mycur.execute(qry)
	emp_list = mycur.fetchall()
	print("List of Employees ")
	for emp in emp_list:
		print("Emp Id : ", emp[0], " Name : ", emp[1],
			" Last Name : ", emp[2], " Phone No : ", emp[3])
	ne = []
	n = int(input('enter the no. of employees to add '))
	for i in range(1, n+1):
		t = ()
		print('enter employee id ')
		idd = int(input(str(i)+') '))
		print('Name ')
		nam = input(str(i)+') ')
		print('Last name ')
		lnam = input(str(i)+') ')
		print('Contact no. ')
		conno = int(input(str(i)+') '))
		print('Address ')
		adrs = input(str(i)+') ')
		# A tuple containing details of an employee
		t = (idd, nam, lnam, conno, adrs)
		# List containing details of n number
		# of employees to be added
		ne = ne+[t, ]
	qry = 'insert into employee values(%s,%s,%s,%s,%s);'
	# A list containing details of each employee
	# in the form of a tuple is to be passed along with the query
	for i in range(len(ne)):
		val = ne[i]
		mycur.execute(qry, val)
		mycon.commit()
	print('All Employee details added. ')
	space()
