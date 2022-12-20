import tablib
import mysql.connector
import pandas as pd
import json
from pprint import pprint


def main():
    db = 'prestashop_1_6'

    body = []
    headers = []

    cnx = mysql.connector.connect(
            user='root', 
            password='',
            host="127.0.0.1",
            database=db
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM ps_product")
    
    for item in cursor:
        body.append( item )
    cursor.close()


    res = cnx._execute_query("SELECT * FROM ps_product")
    
    for item in res["columns"]:
        headers.append(item[0])
    cnx.close()
            
    

    
    
    print(headers.__len__())
    data = tablib.Dataset()
    for x in range(0, len(body)):
        row = []
        for y in range(0, len(body[0])):
            row.append( body[x][y] )
            if y == len(body[0]) - 1:
                data.append( row )

    
    f = open("test.xls", "wb")
    f.write( data.export('xls'));
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Run from import")
