# dealer Master
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=====================')
    print('Dealer Master ')
    print('=====================')
    dcode = input("Enter Dealer code : ")
    dname = input("Enter Dealer Name : ")
    daddress = input("Enter Dealer Address : ")
    phno = input("Enter phn no : ")
    gstno = input("Enter gst no : ")
    dmail = input("enter mail id : ")
    print('=======================================')

    query = 'insert into d_master(dcode, dname, daddress, phno, gstno, dmail ) values(%s, %s, %s, %s, %s, %s)'
    val = (dcode, dname, daddress, phno, gstno, dmail)
    cur_obj = dbconfig.conn.cursor()
    cur_obj.execute(query, val)
    dbconfig.conn.commit()
    #dbconfig.conn.close()
    #cur_obj.close()
    print('Dealer Create Successfully..')

    memberinput = input('Enter y To Continue q to stop :')
    if memberinput == 'q':
        break
print('System Close all')




