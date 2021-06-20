import mysql
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'stockdb',
    password = ''

)

if(conn.is_connected()==True):
    print('Database Connection is Successfully')
else:
    print('Re-connect to Database')