# To check if a customer of a given ID exists or not
from src.MySQLCon import mycur


def check():
    # Query to select all customer IDs
    # from the table
    qry = 'select cust_id from customer;'

    mycur.execute(qry)
    ''' Return a list where each element
    in the list is a tuple
    fetched from each record in table
    Each tuple contains a single element
    as only customer IDs are fetched
    from cust_id column of each record'''

    d = mycur.fetchall()
    # To create a list of all customer IDs in the table
    list_of_ids = [ ]
    for ids in d:
        # A list of all customer IDs in table
        list_of_ids.append(ids[ 0 ])

    return list_of_ids

