# dealer Master

import dbconfig

#dbconfig.conn
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Delete Dealer Master ')
    print('=====================')
    dcode = input("Enter Dealer code : ")
    print('=======================================')

    query = "delete from d_master where dcode='" + dcode + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    # dbconfig.conn.close()
    print('Delete Successfully..')

    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break
print('System Close all')




