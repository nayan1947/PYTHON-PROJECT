#delete customer
import dbconfig
memberinput = True
while True :

    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Delete Customer')
    print('=====================')
    cust_code = input("Enter customer code : ")
    print('=======================================')

    query = "delete from create_customer where cust_code='" + cust_code + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
        #dbconfig.conn.close()
    print('Deleted Customer Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')







