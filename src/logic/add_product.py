# To add a new product in Products table
from src.MySQLCon import mycon, mycur
from src.logic.view_product import view_pro


def addpro():
    # Display list of products
    view_pro()
    n = int(input('Enter no of items to insert '))
    for j in range(n):
        # Initialize tuple to store
        # product details.
        t = ()
        pronum = input("Product No. ")
        proid = input('Product ID : ')
        pprice = int(input('Price : '))
        cata = input("Category : ")
        pstk = int(input('Stock : '))
        t = (proid, pronum, cata, pprice, pstk)
        # Using MySql query
        qry = 'insert into products values(%s,%s,%s,%s,%s);'
        val = t
        mycur.execute(qry, val)
        mycon.commit()
        print("Product Added")
