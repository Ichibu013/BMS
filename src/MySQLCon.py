# MySQL connection object
from tkinter import messagebox

import mysql.connector
from pyexpat.errors import messages

try:
    mycon = mysql.connector.connect(
        host = 'localhost', user = 'root',
        password = '2004',
        database = 'businessproject')
except:
    messagebox.showerror('Error','Something went wrong,Check in MySQl')
# MySQL cursor object
mycur = mycon.cursor()
