# Current Stock report

import dbconfig
import mysql
import mysql.connector

#dbconfig.conn
print('=========================')
print('Current stock report ')
print('=========================')

query='select * from prdct_master'

cur_obj=dbconfig.conn.cursor()
cur_obj.execute(query)
record_object=cur_obj.fetchall()
for rec in record_object:
    print ("code, product type, name, batch no, pro price, mrp,  sale price   ",rec)
dbconfig.conn.close()
print('=======================================')

print('Execute All Record Successfully..')
print('=======================================')
