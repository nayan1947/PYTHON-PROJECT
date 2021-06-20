#dealer info update

import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')
    print('=====================')
    print('dealer info update')
    print('=====================')
    oldphno = input("dealer old Phn No : ")
    newphno = input("dealer new Phn No : ")
    newdmail = input("dealer new mail id : ")
    newdaddress = input("dealer new address :")
    print('=======================================')

    query = "update d_master set phno = '" + newphno + "', " \
    "daddress = '" + newdaddress + "'," \
     " dmail = '" + newdmail + "' where phno='" + oldphno + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('dealer information updated Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')


