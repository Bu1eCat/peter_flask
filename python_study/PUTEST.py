form os import  getenv
import pymssql

server = getenv("PYMSSQL_TEST_SERVER")
user  = getenv("PYMSSQL_TEST_USERNAME")
password = getenv("PYMSSQL_TEST_PASSWORD")

conn = pymssql.connect(server,user,password,"temdb")
cursor = conn.cursor()
cursor.execute('select * from tbluser_sys where salesrep=%s','peter')

for row in cursor:
    print('row = %r',% (row,) )

conn.close()







for row in cursor:
    print('row = {0}'.format())
