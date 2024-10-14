from src.MySQLCon import mycur, mycon
from src.logic.booked_product import get_bkd_pro
from src.logic.check import check
from src.logic.space import space


def sign_in():
    try:
        ask = int(input('Enter customer ID to sign in : '))
        # Using check function to check whether this account exists or not
        list_of_ids = check()
        if ask in list_of_ids:
            while True:
                print(''' Do you want to :																 
						1) View Bookings
						2) Book a product
						3) Update Self Details
						4) Cancel booked products 
							enter 'back' to exit ''')
                # Take choice of the customer
                ccc = input('enter choice - ')
                if ccc == '1':
                    # Get booked product function is used where cutomer ID
                    # is passed as an argument

                    s = get_bkd_pro(ask)
                    # To check if the column has any value
                    if s is None or s == ' ':
                        print('you have not booked products yet')
                    else:
                        ''' If more than one products are booked,
                        their IDs are stored as a single value
                        separated by '_' so we have to split the
                        string to print each product ID.'''

                        # d is a list containing product IDs
                        d = s.split('_')

                        print('Booked products')
                        for bkditems in d:
                            print(bkditems)

                if ccc == '2':

                    # check if the product to be booked exists or not
                    qry = 'select pro_id from products;'
                    mycur.execute(qry)
                    pro_list = mycur.fetchall()
                    ''' contains a list where each element is a tuple fetched
                    from each record, the tuple contains values in the
                    column named pro_nam from products table.'''

                    # empty list to store product IDs
                    list_of_products = [ ]
                    for i in pro_list:
                        list_of_products.append(i[ 0 ])

                    # Take ID and quantity of product to be booked
                    pro_id = input('Enter the product id to book products : ')
                    # To add booked product in the column,we first
                    # need to check if it already contains a value in it
                    if pro_id in list_of_products:
                        # Customer ID is given as value along with
                        # query to fetch booked product for the given ID
                        qry = 'select bkd_pro from customer where cust_id=%s;'
                        mycur.execute(qry, (ask,))
                        pr = mycur.fetchone()
                        # prl is value fetched from table
                        prl = pr[ 0 ]
                        # When the column is empty the new product is to stored
                        if prl is None or prl == ' ':
                            qry = 'update customer set bkd_pro=%s where cust_id=%s;'
                            val = (pro_id + '_', ask)
                            mycur.execute(qry, val)
                            mycon.commit()
                            print('Your Product is booked !!')

                            ''' If there already exists a value in bkd_pro column,
                                new value must be concatenated with the existing
                                one and again stored in the table'''
                        else:
                            prl1 = prl + pro_id
                            qry2 = 'update customer set bkd_pro=%s where cust_id=%s;'
                            # val2 is the new value containing all booked products
                            # to be stored in the column
                            val2 = (prl1 + '_', ask)
                            mycur.execute(qry2, val2)
                            mycon.commit()
                            print('Your Product is booked !!')

                    else:
                        print('This product does not exists.\
        Please write the correct product id!')

                if ccc == '3':

                    qry = 'select cust_id,c_nam,c_lnam,c_phno,c_adrs\
                                from customer where cust_id =%s'
                    mycur.execute(qry, (ask,))
                    # clist contains list of all values fetched
                    # in the form of a tuple for this customer ID
                    clist = mycur.fetchone()
                    # list of fields to be updated
                    flds = [ 'Name', 'Last Name', 'Ph.No', 'Address' ]
                    dic = {}
                    print("Your existing record is :")
                    # The fetched details are stored in the form of key
                    # value pair in a dictionary
                    for i in range(4):
                        dic[ flds[ i ] ] = clist[ i + 1 ]
                        print(i + 1, ' ', flds[ i ], ' : ', clist[ i + 1 ])

                    for i in range(len(clist)):
                        updtc = int(input('enter choice to update '))
                        upval = input('enter' + flds[ updtc - 1 ] + ' ')
                        # Change the value corresponding to the required field
                        dic[ flds[ updtc - 1 ] ] = upval
                        yn = input(
                            'Do you want to update other details? y or n ')
                        if yn in 'Nn':
                            break
                    qry = 'update customer set c_nam=%s,c_lnam=%s,c_phno=%s,\
                            c_adrs=%s where cust_id=%s;'

                    updtl = tuple(dic.values()) + (ask,)
                    # The value to be passed along with the query is a tuple
                    # containing updated details of the given customer ID
                    val = (updtl)
                    mycur.execute(qry, val)
                    mycon.commit()
                    print('Your details are updated ')

                if ccc == '4':

                    try:
                        # To get the existing bookings
                        # Booked products in the table
                        bkd_pro = get_bkd_pro(ask)
                        print('Your Booking(s) : \n ', bkd_pro)
                        if bkd_pro is None or bkd_pro == ' ':
                            print('you have no bookings to cancel')
                        else:
                            cw = input("To cancel all products; enter A \nOR \
        enter the product code to cancel : ")
                            if cw in 'Aa':
                                qry = 'update customer set bkd_pro=NULL\
                                        where cust_id=%s'

                                mycur.execute(qry, (ask,))
                                mycon.commit()
                                print('All bookings deleted')
                            elif cw in bkd_pro:
                                # If more than one products entered,
                                # split them on the basis of '_'
                                # x is a list containing all booked products
                                x = (bkd_pro[ 0:-1 ]).split('_')

                                # Delete the required product ID
                                x.remove(cw)
                                updt_pro = ''
                                # Again concatenate each product ID
                                # in the list to store in the table
                                for item in x:
                                    updt_pro = updt_pro + item + '_'
                                qry = 'update customer set bkd_pro=%s where cust_id=%s'
                                val = (updt_pro, ask)
                                mycur.execute(qry, val)
                                mycon.commit()
                                print('Booking Cancelled !')
                    except Exception:
                        print('Some problem in updating details.Try again')
                if ccc.lower() == 'back':
                    print("Successfully logged out")
                    space()
                    break

        else:
            print('This Account does not exist. ')
    except Exception:
        print('Some error occurred. Try Again')
