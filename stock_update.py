# stock update
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')
    print('=====================')
    print('Product Master Update ')
    print('=====================')
    prdct_code = input("Product code : ")
    oldqty = input("Old Quantity : ")
    newqty = input("New Quantity : ")

    print('=======================================')
    quantity = int(oldqty) + int(newqty);
    qty = str(quantity)

    query = "update prdct_master set quantity='" + qty + "' where prdct_code='" + prdct_code + "' "
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Update Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')




