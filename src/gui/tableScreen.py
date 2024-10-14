from tkinter import ttk
from tkinter.constants import VERTICAL

from customtkinter import CTkFrame, CTkComboBox, CTkEntry, CTkButton, CTk

window = CTk()
window.geometry('930x580')
window.resizable(False, False)

leftframe = CTkFrame(window)
leftframe.grid(row = 1, column = 0)

button1 = CTkButton(leftframe,
                    text = 'Place Holder')
button1.grid(row = 0, column = 0,
             pady = 20)

rightframe = CTkFrame(window)
rightframe.grid(row = 1, column = 1)

search_options = [ 'Id', 'Product Name', 'Category', 'Quantity' ]
searchbox = CTkComboBox(rightframe,
                        values = search_options,

                        state = 'readonly')
searchbox.grid(row = 0, column = 0)
searchbox.set('Search By')

searchEntry = CTkEntry(rightframe)
searchEntry.grid(row = 0, column = 1)

searchButton = CTkButton(rightframe,
                         text = 'SEARCH',
                         width = 100)
searchButton.grid(row = 0, column = 2)

showallButton = CTkButton(rightframe,
                          text = 'SHOW ALL',
                          width = 100)
showallButton.grid(row = 0, column = 3,
                   pady = 5)

tree = ttk.Treeview(rightframe,
                    height = 13,
                    )
tree.grid(row = 1, column = 0,
          columnspan = 4)

tree[ 'columns' ] = [ 'Id', 'Product Name', 'Price', 'Category', 'Quantity' ]

tree.heading('Id',
             text = 'ID')
tree.heading('Product Name',
             text = 'PRODUCT NAME')
tree.heading('Price',
             text = 'PRICE')
tree.heading('Category',
             text = 'CATEGORY')
tree.heading('Quantity',
             text = 'QUANTITY')

tree.config(show = 'headings')

tree.column('Id', width = 100)
tree.column('Product Name',width = 250)
tree.column('Price',width = 100)
tree.column('Category',width = 100)
tree.column('Quantity',width = 100)

style = ttk.Style()

style.configure('TreeView.Heading', font = ('', 18, 'bold'))

scrollbar = ttk.Scrollbar(rightframe,
                          orient = VERTICAL,
                          command = tree.yview)
scrollbar.grid(row = 1, column = 4,
               sticky = 'ns')
tree.config(yscrollcommand = scrollbar.set)

window.title("DashBoard")
window.mainloop()
