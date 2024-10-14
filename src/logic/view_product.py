# To fetch values from all columns of
# product table to get product details
from src.MySQLCon import mycur


def view_pro():
    qry = 'select * from products;'
    mycur.execute(qry)
    d = mycur.fetchall()
    # contains list of all records
    dic = {}
    # Each record fetched is separated into a key value pair
    # and stored in the dictionary where product ID is the key
    for i in d:
        dic[ i[ 0 ] ] = i[ 1: ]
    print('_' * 80)
    # Printing the dictionary in the form of a table
    print("{:<17} {:<22} {:<23} {:<19}".format(
        'Product id', 'Product name', 'Price', 'Stock'))
    print('_' * 80)
    for k, v in dic.items():
        a, b, c = v
        print("{:<17} {:<22} {:<23} {:<19}".format(k, a, b, c))
    print('_' * 80)
