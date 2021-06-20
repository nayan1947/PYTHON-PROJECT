# sale amt report
import dbconfig
memberinput = True
while True :



    if (dbconfig.conn.is_connected() == True):
        print('Database Connection is Successfully')
    else:
        print('Re-connect to Database')

    print('=========================')
    print('sale report ')
    print('=========================')

    query = 'select sum(prdct_master.sale_cost) as sale_cost from ' \
            'prdct_master inner join sale_prdct ' \
            'on prdct_master.prdct_code=sale_prdct.prdct_code'

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

