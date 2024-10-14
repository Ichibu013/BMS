import customtkinter as ctk

# MySQL Connection file import
from src.MySQLCon import mycur, mycon

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")

# Dimensions of the window
appWidth, appHeight = 300, 480


# App Class
class App(ctk.CTk):

    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("BMS Sign UP")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                      text = "Fist Name")
        self.nameLabel.grid(row = 0, column = 0,
                            padx = 20, pady = 20,
                            sticky = "ew")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                                      placeholder_text = "First Name")
        self.nameEntry.grid(row = 0, column = 1,
                            columnspan = 3, padx = 20,
                            pady = 20, sticky = "ew")

        # Name Label
        self.lnameLabel = ctk.CTkLabel(self,
                                       text = "Last Name")
        self.lnameLabel.grid(row = 1, column = 0,
                             padx = 20, pady = 20,
                             sticky = "ew")

        self.lnameEntry = ctk.CTkEntry(self,
                                       placeholder_text = "Last Name")
        self.lnameEntry.grid(row = 1, column = 1,
                             columnspan = 3, padx = 20,
                             pady = 20, sticky = "ew")

        # Age Label
        self.adrsLabel = ctk.CTkLabel(self, text = "Address")
        self.adrsLabel.grid(row = 2, column = 0,
                            padx = 20, pady = 20,
                            sticky = "ew")

        # Age Entry Field
        self.adrsEntry = ctk.CTkEntry(self,
                                      placeholder_text = "Location")
        self.adrsEntry.grid(row = 2, column = 1,
                            columnspan = 3, padx = 20,
                            pady = 20, sticky = "ew")

        # Phone Label
        self.phoneLabel = ctk.CTkLabel(self, text = "Number")
        self.phoneLabel.grid(row = 3, column = 0,
                             padx = 20, pady = 20,
                             sticky = "ew")

        # phone Entry Field
        self.phoneEntry = ctk.CTkEntry(self,
                                       placeholder_text = "Contact Number")
        self.phoneEntry.grid(row = 3, column = 1,
                             columnspan = 3, padx = 20,
                             pady = 20, sticky = "ew")
        # UserName Label
        self.unameLabel = ctk.CTkLabel(self, text = "UserName")
        self.unameLabel.grid(row = 4, column = 0,
                             padx = 20, pady = 20,
                             sticky = "ew")

        # UserName Entry Field
        self.unameEntry = ctk.CTkEntry(self,
                                       placeholder_text = "UserName")
        self.unameEntry.grid(row = 4, column = 1,
                             columnspan = 3, padx = 20,
                             pady = 20, sticky = "ew")

        # Password Label
        self.pwdLabel = ctk.CTkLabel(self, text = "Password")
        self.pwdLabel.grid(row = 5, column = 0,
                           padx = 20, pady = 20,
                           sticky = "ew")

        # Password Entry Field
        self.pwdEntry = ctk.CTkEntry(self,
                                     placeholder_text = "Password")
        self.pwdEntry.grid(row = 5, column = 1,
                           columnspan = 3, padx = 20,
                           pady = 20, sticky = "ew")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text = "SIGN UP ",
                                                   command = self.generateResults)
        self.generateResultsButton.grid(row = 6, column = 1,
                                        columnspan = 2, padx = 20,
                                        pady = 20, sticky = "ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
                                         width = 200,
                                         height = 100)
        self.displayBox.grid(row = 7, column = 0,
                             columnspan = 4, padx = 20,
                             pady = 20, sticky = "nsew")

    # This function is used to insert the
    # details entered by users into the textbox
    def generateResults(self):
        # self.displayBox.delete("0.0", "200.0")
        # text = self.createText()
        # self.displayBox.insert("0.0", text)

        c_det = ()

        cid_qry = "SELECT cust_id FROM customer ORDER BY cust_id desc"
        mycur.execute(cid_qry)
        cid_ary = mycur.fetchall()
        cid = cid_ary(0)

        custid = cid + 1
        cnam = str(self.nameEntry.get())
        clnam = str(self.lnameEntry.get())
        cphno = str(self.phoneEntry.get())
        cadrs = str(self.adrsEntry.get())
        cuid = str(self.unameEntry.get())
        cpwd = str(self.pwdEntry.get())
        c_det = (custid, cnam, clnam, cphno, cadrs, cuid, cpwd)

        qry = 'insert into customer values(%s,%s,%s,%s,%s,NULL,NULL,%s,%s);'

        # value of the fields to be entered with the query
        val = c_det

        mycur.execute(qry, val)
        mycon.commit()

if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()


