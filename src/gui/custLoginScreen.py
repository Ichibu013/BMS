import tkinter.messagebox as tkmb

import customtkinter as ctk

# MySQL Connection file import
from src.MySQLCon import mycur

# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("BM System login")


def login():
    uname_temp = "SELECT user_name FROM customer"
    mycur.execute(uname_temp)
    username = mycur.fetchall()

    pwd_temp = "SELECT pwd FROM customer"
    mycur.execute(pwd_temp)
    password = mycur.fetchall()

    new_window = ctk.CTkToplevel(app)

    new_window.title("New Window")

    new_window.geometry("350x150")

    for i in username:
        if str(user_entry.get()) in i:
            for j in password:
                if str(user_pass.get()) in j:
                    tkmb.showinfo(title = "Login Successful", message = "You have logged in Successfully")
                    app.destroy()
                    import src.gui.tableScreen

                elif str(user_pass.get()) not in j or str(user_pass.get()) == '':
                    tkmb.showwarning(title = 'Wrong password', message = 'Please check your password')
        elif str(user_entry.get()) not in i or str(user_entry.get()) == '':
            for j in password:
                if str(user_pass.get()) in j or str(user_pass.get()) == '':
                    tkmb.showwarning(title = 'Wrong username', message = 'Please check your username')
        else:
            tkmb.showerror(title = "Login Failed", message = "Invalid Username and password")



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

app.mainloop()
