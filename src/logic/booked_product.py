# To select all booked products of
# a given customer from the table
from src.MySQLCon import mycur


def get_bkd_pro(cust_id):
    qry = 'select bkd_pro from customer\
where cust_id=%s;'
    mycur.execute(qry, (cust_id,))
    bp = mycur.fetchone()
    bkd_pro = bp[ 0 ]
    return bkd_pro
