import tablib
import mysql.connector
from pprint import pprint



def main():
    user = 'root'
    password = ''
    host = '127.0.0.1'
    database = 'prestashop_1_6'
    table = "ps_product"

    new_user = input(f'nazwa użytkownika[bazowo: {user}]')
    new_password = input(f'hasło[bazowo: {password}]')
    new_host = input(f'adres hosta[bazowo: {host}]')
    new_database = input(f'nazwa bazy danych[bazowo: {database}]')
    new_table = input(f'nazwa tablicy z danymi[bazowo: {table}]')
    

    if new_user:
        user = new_user
    if new_password:
        password = new_password
    if new_host:
        host = new_host
    if new_database:
        database = new_database
    if new_table:
        table = new_table

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
    cursor.execute(f"SELECT * FROM {table}")
    
    for item in cursor:
        body.append( item )
    cursor.close()


    res = cnx._execute_query(f"SELECT * FROM {table}")
    
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

    data.headers = headers
    
    print(f"zapisywanie danych w pliku {table}.xls...")
    f = open(f"{table}.xls", "wb")
    f.write( data.export('xls'));
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Run from import")
