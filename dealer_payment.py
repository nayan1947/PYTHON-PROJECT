#dealer payment

import dbconfig
memberinput = True
while True :


    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Dealer Payment')
    print('=====================')
    d_name = input("Enter Dealer Name : ")
    trans_id = input("Enter Transaction ID : ")
    dt_of_paym = input("Enter date of Payment : ")
    descrp = input("Description: ")
    cr = float(input("Enter Credit Amount : "))
    dr = float(input("Enter Debit Amount : "))
    print('=======================================')


    query = 'insert into d_payment(d_name	, trans_id, dt_of_paym, descrp, cr, dr) values(%s, %s, %s, %s,%s, %s)'
    val = (d_name, trans_id, dt_of_paym, descrp, cr, dr)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Dealer payment Created Successfully..')
    memberinput = input('Enter y To Continue q to stop :')

    if memberinput == 'q':

        break;
    print('System Close all')

















