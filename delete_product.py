#delete product
import dbconfig
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Delete Product Master ')
    print('=====================')
    prdct_code = input("Product code : ")
    print('=======================================')

    query = "delete from prdct_master where prdct_code='" + prdct_code + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Product Deleted Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break
print('System Close all')



