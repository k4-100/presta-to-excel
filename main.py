
import tablib
import mysql.connector
from pprint import pprint


def main():
    db = 'prestashop_1_6'

    cnx = mysql.connector.connect(
            user='root', 
            password='',
            host="127.0.0.1",
            database=db
    )
    result = {}
    result = cnx._execute_query("SELECT * FROM ps_product")
    cnx.close()
        

    data = tablib.Dataset()
    # collection of names


    columns = result['columns']
    headers = []
    for item in columns:
        headers.append(item[0])
    
    for x in range(0, len(columns)):
        row = []
        for y in range(1, len(columns[0])):
            row.append( columns[x][y] )
            if y == len(columns[0]) - 1:
                data.append_col( row, header='s' )

        
    data.headers = headers
    # pprint( data.dict )
    f = open("test.xls", "wb")
    f.write( data.export('xls') )
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Run from import")
