# dealer report

import dbconfig
import mysql
import mysql.connector

#dbconfig.conn
print('=========================')
print('sale report ')
print('=========================')

query='select create_customer.cname as cname, ' \
      'create_customer.c_phno as c_phno,' \
      ' create_customer.address as address,' \
      ' create_customer.email as email,' \
      ' sale_prdct.prdct_code as prdct_code,' \
      ' sale_prdct.tot_quantity as tot_quantity' \
      ' from create_customer inner join sale_prdct' \
      ' on create_customer.c_phno = sale_prdct.c_phno'

cur_obj=dbconfig.conn.cursor()
cur_obj.execute(query)
record_object=cur_obj.fetchall()
for rec in record_object:
    print(rec)
dbconfig.conn.close()
print('=======================================')
print('Execute All Record Successfully..')
print('=======================================')
