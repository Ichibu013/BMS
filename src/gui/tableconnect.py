import tkinter as tk 

#For MySQL Database connection 
from src.MySQLCon import mycon,mycur

#import sqlite3

# #connect to database 
# conn = sqlite3.connect(businessproject.db)
# mycur = conn.mycur()

# Functions to interact with database
def get_customer_purchases(cust_id):
    mycur.execute('''
        SELECT p.pur_id, p.prod_id, p.total_amt, p.pay_mtd, p.amt_exg
        FROM purchase p
        WHERE p.cust_id = (%s)
    ''', (cust_id,))
    return mycur.fetchall()

def get_employee_orders(emp_id):
    mycur.execute('''
        SELECT o.ord_id, o.prod_id, o.category, o.perv_deli_date, o.nxt_deli_date, o.pay_status, o.pay_amt
        FROM orders o
        WHERE o.placed_by_emp_id = %s
    ''', (emp_id,))
    return mycur.fetchall()


def get_employee_attendance(emp_id):
    mycur.execute('''
        SELECT a.login_date, a.login_time, a.logout_time
        FROM attendance a
        WHERE a.emp_id = ?
    ''', (emp_id,))
    return mycur.fetchall()


def get_customer_order_details(cust_id):
    mycur.execute('''
        SELECT o.ord_id, o.prod_id, o.category, o.perv_deli_date, o.nxt_deli_date, o.pay_status, o.pay_amt
        FROM orders o
        JOIN purchases p ON o.prod_id = p.prod_id
        WHERE p.cust_id = ?
    ''', (cust_id))
    return mycur.fetchall()


def get_employee_customer_details(emp_id):
    mycur.execute('''
        SELECT c.cust_id, c.c_nam, c.c_lnam, c.c_phno, c.c_adrs
        FROM customers c
        JOIN orders o ON c.cust_id = o.cust_id
        WHERE o.placed_by_emp_id = ?
    ''', (emp_id,))
    return mycur.fetchall()


def get_admin_employee_details(admin_id):
    mycur.execute('''
        SELECT e.emp_id, e.e_nam, e.e_lnam, e.e_phno, e.e_adrs
        FROM employees e
        JOIN admin a ON e.dept_nam = a.dept_nam
        WHERE a.admin_id = ?
    ''', (admin_id,))
    return mycur.fetchall()

#from database import get_customer_purchases, get_employee_orders, get_employee_attendance, get_customer_order_details, get_employee_customer_details, get_admin_employee_details

# Create Tkinter GUI
root = tk.Tk()
root.title('Boutique Management System')

# Create frames for each table
customer_frame = tk.Frame(root)
purchase_frame = tk.Frame(root)
employee_frame = tk.Frame(root)
order_frame = tk.Frame(root)
attendance_frame = tk.Frame(root)
admin_frame = tk.Frame(root)

# Add widgets and functionality to each frame
cust_id = 1
purchases = get_customer_purchases(cust_id)
for purchase in purchases:
    print(purchase)

emp_id = 10001
orders = get_employee_orders(emp_id)
for order in orders:
    print(order)

attendance = get_employee_attendance(emp_id)
for attend in attendance:
    print(attend)

customer_orders = get_customer_order_details(cust_id)
for order in customer_orders:
    print(order)

employee_customers = get_employee_customer_details(emp_id)
for customer in employee_customers:
    print(customer)

admin_id = 1
admin_employees = get_admin_employee_details(admin_id)
for employee in admin_employees:
    print(employee)

root.mainloop()