#customer info update
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Customer info update')
    print('=====================')
    oldc_phno = input("Customer old Phn No : ")
    newc_phno = input("Customer new Phn No : ")
    oldemail = input("Customer old email : ")
    newemail = input("Customer new email : ")

    print('=======================================')

    query = "update create_customer set c_phno = '" + newc_phno + "', email = '" + newemail + "'where c_phno='" + oldc_phno + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('customer updated Successfully..')

    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')

