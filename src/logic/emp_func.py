# For employer login
from src.logic.add_emp import addemp
from src.logic.view_product import view_pro


def employer():
    while True:
        print()
        print('''Enter Your Choice:													 
					1)View Product Details
					2)Add a New Employee
					enter back to exit''')
        ccc = input('Enter _____ ')
        if ccc == '1':
            view_pro()
        if ccc == '2':
            addemp()
        if ccc.lower() == "back":
            break
