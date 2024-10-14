from src.MySQLCon import mycur

#MySQL database DDL commands
# mycur.execute('CREATE DATABASE IF NOT EXISTS businessproject')
# mycur.execute('USE businessproject')
mycur.execute('CREATE TABLE IF NOT EXISTS customer(cust_id int PRIMARY KEY,c_nam varchar(30),c_lnam varchar(30),c_phno varchar(10),c_adrs varchar(50),last_pur_date date,last_pur_amt int)')
mycur.execute('CREATE TABLE IF NOT EXISTS purchase(pur_id int,prod_id int,total_amt int,cust_id int,pay_mtd varchar(30),amt_exg int,CONSTRAINT FK_PurCust_id FOREIGN KEY (cust_id) REFERENCES customer(cust_id))')
mycur.execute('CREATE TABLE IF NOT EXISTS products(pro_id int PRIMARY KEY,pro_nam varchar(30),pro_cata varchar(30),pro_price int,pro_stk int)')
mycur.execute('CREATE TABLE IF NOT EXISTS orders(ord_id int PRIMARY KEY,prod_id int,category varchar(30),placed_by_emp_id int,perv_deli_date date,nxt_deli_date date,pay_status varchar(10),pay_amt int,CONSTRAINT FK_prod_id FOREIGN KEY (prod_id) REFERENCES products(pro_id))')
mycur.execute('CREATE TABLE IF NOT EXISTS admin(admin_id int PRIMARY KEY,admin_nam varchar(30),admin_phno varchar(10),admin_adrs varchar(50),admin_eid varchar(30),last_entry varchar(20),dept_nam varchar(20),date_of_join date)')
mycur.execute('CREATE TABLE IF NOT EXISTS employee(emp_id int PRIMARY KEY,e_nam varchar(30),e_lnam varchar(30),e_phno varchar(10),e_adrs varchar(50),e_cno varchar(10),emp_eid varchar(30),emp_e_pswd varchar(30),last_entry varchar(20),dept_nam varchar(20),date_of_join date')
mycur.execute('CREATE TABLE IF NOT EXISTS attendence(emp_id int,login_date date,login_time timestamp,logout_time timestamp,CONSTRAINT FK_emp_id FOREIGN KEY (emp_id) REFERENCES employee(emp_id))')

