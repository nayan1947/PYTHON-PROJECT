#bill master

import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')
    print('=====================')
    print('Bill Master')
    print('=====================')
    dname = input("Enter Dealer Name : ")
    deal_nos = input("Enter Dealer Phn no : ")
    tot_item = input("Enter total no item : ")
    bill_amt = input("Bill Amount : ")
    bill_dt = input("Bill Date : ")
    print('=======================================')

    query = 'insert into bill_master(dname, deal_nos, tot_item, bill_amt, bill_dt) values(%s, %s, %s, %s, %s)'
    val = (dname, deal_nos, tot_item, bill_amt, bill_dt)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    print('Bill Created Successfully..')
    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break;
print('System Close all')


