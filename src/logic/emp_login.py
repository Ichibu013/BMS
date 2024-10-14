# For Employee Login
from src.MySQLCon import mycur, mycon
from src.logic.add_product import addpro
from src.logic.booked_product import get_bkd_pro
from src.logic.delete_product import delpro
from src.logic.space import space


def emp_sign_in():
    try:
        ask = input('Enter id to sign in to the account : ')
        # To check if the employee with this ID exists or not.
        qry = 'select emp_id from employee;'
        mycur.execute(qry)
        d = mycur.fetchall()
        lis = [ ]
        for i in d:
            lis.append(i[ 0 ])
        if ask not in lis:
            print('Enter the correct id')
        else:
            while True:
                space()
                ccc = input("1. Update delivered records"
                            "\n2. Add a New Product "
                            "\n3. Delete a product "
                            "\nEnter 'Back' to logout: ")
                if ccc == '1':
                    cust_id = input('Enter customer id')
                    # Check if the customer has bookings or not
                    bkd_pro = get_bkd_pro(cust_id)
                    if bkd_pro is None or bkd_pro == ' ':
                        print('This customer has no bookings ')
                    else:
                        print('All booking(s): ', bkd_pro)
                        pro_id = input('Enter product code to\
                                        remove the delivered product ')
                        # The product IDs are stored in the form of a
                        # single value separated by '_'.
                        if pro_id in bkd_pro:
                            x = (bkd_pro[ 0:-1 ]).split('_')
                            # Returns a list of all booked products,
                            # then remove the delivered product from list
                            x.remove(pro_id)
                            # Concatenate the existing products using '_'
                            updt_pro = ''
                            for i in x:
                                updt_pro = updt_pro + i + '_'
                            qry = 'update customer set bkd_pro=%s \
                                    where cust_id=%s;'
                            val = (updt_pro, cust_id)
                            mycur.execute(qry, val)
                            mycon.commit()
                            print('Delivered product is removed\
                                    from the database. ')
                        else:
                            print('enter the correct code')
                elif ccc == '2':
                    addpro()
                elif ccc == '3':
                    delpro()
                elif ccc.lower() == 'back':
                    print("Successfully logged out ")
                    break
    except Exception:
        print('Give the correct input')
