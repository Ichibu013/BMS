
#TO CHANGE


import customtkinter as ctk

#MySQL Connection file import 
from src.MySQLCon import mycur,mycon

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")


# Dimensions of the window
appWidth, appHeight = 580, 700


# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Order Form")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")

        # Prodcut ID Label
        self.idLabel = ctk.CTkLabel(self,
                                      text = "Product ID")
        self.idLabel.grid(row = 0, column = 0,
                            padx = 20, pady = 20,
                            sticky = "ew")

        # ID Entry Field
        self.idEntry = ctk.CTkEntry(self,
                                      placeholder_text = "ID")
        self.idEntry.grid(row = 1, column = 0,
                            columnspan = 1, padx = 20,
                            pady = 20, sticky = "ew")

        # Product Name Label
        self.pnamLabel = ctk.CTkLabel(self,
                                       text = "Product Name")
        self.pnamLabel.grid(row = 0, column = 1,
                             padx = 20, pady = 20,
                             sticky = "ew")

        #Product Name Entry
        self.pnamEntry = ctk.CTkEntry(self,
                                       placeholder_text = "Name")
        self.pnamEntry.grid(row = 1, column = 1,
                             columnspan = 1, padx = 20,
                             pady = 20, sticky = "ew")

        # Quantity Label
        self.qtyLabel = ctk.CTkLabel(self, text = "Quantity")
        self.qtyLabel.grid(row = 0, column = 2,
                            padx = 20, pady = 20,
                            sticky = "ew")

        #Quantity Entry Field
        self.qtyEntry = ctk.CTkEntry(self,
                                      placeholder_text = "Quantity")
        self.qtyEntry.grid(row = 1, column = 2,
                            columnspan = 1, padx = 20,
                            pady = 20, sticky = "ew")

        #Add new item button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text = "+",
                                                   height = 5,width = 25,
                                                   command = self.generateResults
                                                   )
        self.generateResultsButton.grid(row = 1, column = 5)


        # Place order Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text = "Place Order ",
                                                   command = self.placeOrder)
        self.generateResultsButton.grid(row = 3, column = 2,
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
    def placeOrder(self):
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
        c_det = (custid, cnam, clnam, cphno, cadrs,cuid,cpwd)


        qry = 'insert into customer values(%s,%s,%s,%s,%s,NULL,NULL,%s,%s);'

        # value of the fields to be entered with the query
        val = c_det

        mycur.execute(qry, val)
        mycon.commit()

   


if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()

