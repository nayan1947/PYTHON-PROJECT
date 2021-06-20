# product master

import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')
    print('=====================')
    print('Product Master ')
    print('=====================')
    prdct_code = input("Product code : ")
    prdct_name = input("Product name : ")
    prdct_comp = input("Product Company : ")
    batch_nos = input("Batch no : ")
    prdct_price = input("Product price: ")
    mrp = input("Product MRP : ")
    sale_cost = input("Sale cost of the product : ")
    quantity = input("Quantity : ")
    print('=======================================')

    query = 'insert into prdct_master(prdct_code, prdct_name, prdct_comp,' \
            ' batch_nos, prdct_price, mrp, sale_cost, quantity) ' \
            'values(%s, %s, %s, %s, %s, %s, %s, %s)'
    val = (prdct_code, prdct_name, prdct_comp, batch_nos, prdct_price,
           mrp, sale_cost, quantity)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')




