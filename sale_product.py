#sale product
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Sale Product')
    print('=====================')
    c_phno = input("Customer Phn No : ")

    prdct_code = input("Product code : ")
    tot_quantity = input("Enter Total Quantity: ")

    print('=======================================')

    query = 'insert into sale_prdct(c_phno, prdct_code, tot_quantity) values(%s, %s, %s)'
    val = (c_phno, prdct_code, tot_quantity)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('sale Created Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')


