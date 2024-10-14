# To delete a product from the table
from src.MySQLCon import mycur, mycon
from src.logic.view_product import view_pro


def delpro():
    view_pro()
    delt = input("Enter ID of product to be deleted")
    qry = 'delete from products where pro_id=%s;'
    mycur.execute(qry, (delt,))
    mycon.commit()
    print("Product is deleted")
