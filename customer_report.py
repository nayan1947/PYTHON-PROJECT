# dealer report
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=========================')
    print('customer report ')
    print('=========================')

    query = 'select * from create_customer'

    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query)
    record_object = cur_obj.fetchall()
    for rec in record_object:
        print(rec)
    #dbconfig.conn.close()
    print('=======================================')
    print('Execute All Record Successfully..')
    print('=======================================')
    break


