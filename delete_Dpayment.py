#delete Dealer payment
import dbconfig
memberinput = True
while True:



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Delete Dealer Payment ')
    print('=====================')
    trans_id = input("Enter Dealer transaction id: ")

    print('=======================================')

    query = "delete from d_payment where trans_id='" + trans_id + "'"
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Delete Payment Successfully..')

    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break
print('System Close all')



