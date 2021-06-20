#create customer
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')
    print('=====================')
    print('Create Customer')
    print('=====================')
    cust_code = input("Enter customer code : ")
    cname = input("Customer Name : ")
    c_phno = input("Customer Phn No : ")
    address = input("Enter Customer address : ")
    email = input("Enter Customer Email: ")
    print('=======================================')

    query = 'insert into create_customer(cust_code, cname, c_phno, address, email) values(%s, %s, %s, %s, %s)'
    val = (cust_code, cname, c_phno, address, email)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Customer Created Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')




