import tablib
import mysql.connector
from pprint import pprint



def main():
    user = 'root'
    password = ''
    host = '127.0.0.1'
    database = 'prestashop_1_6'

    new_user = input(f'user[default: {user}]')
    new_password = input(f'password[default: {password}]')
    new_host = input(f'host[default: {host}]')
    new_database = input(f'database[default: {database}]')

    if new_user == True:
        user = new_user
    if new_password == True:
        password = new_password
    if new_host == True:
        host = new_host
    if new_database == True:
        database = new_database

    body = []
    headers = []

    print("\npobieranie danych z bazy...")

    cnx = mysql.connector.connect(
            user=user, 
            password=password,
            host=host,
            database=database
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
            
    print("wkładanie danych do obiektu...")

    data = tablib.Dataset()
    for x in range(0, len(body)):
        row = []
        for y in range(0, len(body[0])):
            row.append( body[x][y] )
            if y == len(body[0]) - 1:
                data.append( row )

    
    print("zapisywanie danych w pliku .xls...")
    f = open("test.xls", "wb")
    f.write( data.export('xls'));
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Run from import")
