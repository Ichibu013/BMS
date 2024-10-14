import customtkinter
from Tools.demo.spreadsheet import CENTER
from customtkinter import CTkLabel


# Dimensions of the window
appWidth, appHeight = 400, 400


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Customer")
        self.add("Employee")
        self.add("Admin")

        def custlogin():
            app.destroy()
            import src.gui.custLoginScreen


        # Customer Sign in widget
        self.label = customtkinter.CTkButton(master = self.tab("Customer"),
                                             text = "SIGN IN",
                                             anchor = CENTER,
                                             command = custlogin)
        self.label.pack(padx = 20, pady = 20)

        # Customer Sign Up widget
        self.label = customtkinter.CTkButton(master = self.tab("Customer"),
                                             text = "SIGN UP",
                                             anchor = CENTER, )
        self.label.pack(padx = 20, pady = 20)

        # Employee Sign in widget
        self.label = customtkinter.CTkButton(master = self.tab("Employee"),
                                             text = "SIGN IN",
                                             anchor = CENTER, )
        self.label.pack(padx = 20, pady = 20)

        # Admin Sign in widget
        self.label = customtkinter.CTkButton(master = self.tab("Admin"),
                                             text = "SIGN IN",
                                             anchor = CENTER, )
        self.label.pack(padx = 10, pady = 20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Sets the title of the window to "App"
        self.title("BMS")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")

        # Heading
        self.label = CTkLabel(self,
                              text = 'Business Management System',
                              font = ('',18,'bold'))
        # self.label.grid(row = 0,column = 0)
        self.label.pack(padx = 20, pady = 20)
        self.tab_view = MyTabView(master = self)
        # self.tab_view.grid(row = 1, column = 0,
        #                    padx = 20, pady = 20)
        self.tab_view.pack(padx = 20, pady = 20)


app = App()
app.mainloop()
