import tkinter.messagebox as tkmb

import customtkinter as ctk

#MySQL Connection file import 
from src.MySQLCon import mycur

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("BMS Employee login")


def login():



    uname_temp = "SELECT emp_eid FROM employee"
    mycur.execute(uname_temp)
    username = mycur.fetchall()

    pwd_temp = "SELECT emp_e_pswd FROM employee"
    mycur.execute(pwd_temp)
    password = mycur.fetchall()

    new_window = ctk.CTkToplevel(app)

    new_window.title("New Window")

    new_window.geometry("350x150")

    for i in username:
        login_success = False
        if str(user_entry.get()) in i:
            for j in password:
                if str(user_pass.get()) in j:
                    tkmb.showinfo(title = "Login Successful", message = "You have logged in Successfully")
                    login_success = True
                    ctk.CTkLabel(new_window, text = "Login page successful").pack()
                else:
                    tkmb.showwarning(title = 'Wrong password', message = 'Please check your password')
        elif str(user_entry.get()) not in i:
            for j in password:
                if str(user_pass.get()) in j:
                    tkmb.showwarning(title = 'Wrong username', message = 'Please check your username')
        else:
            tkmb.showerror(title = "Login Failed", message = "Invalid Username and password")

    print(login_success)


label = ctk.CTkLabel(app, text = "Business Management System")

label.pack(pady = 20)

frame = ctk.CTkFrame(master = app)
frame.pack(pady = 20, padx = 40, fill = 'both', expand = True)

label = ctk.CTkLabel(master = frame, text = 'System Login')
label.pack(pady = 12, padx = 10)

user_entry = ctk.CTkEntry(master = frame, placeholder_text = "Username")
user_entry.pack(pady = 12, padx = 10)

user_pass = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
user_pass.pack(pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = 'Login', command = login)
button.pack(pady = 12, padx = 10)

checkbox = ctk.CTkCheckBox(master = frame, text = 'Remember Me')
checkbox.pack(pady = 12, padx = 10)

app.mainloop()

