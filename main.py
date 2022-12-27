# import tablib
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import mysql.connector
from pprint import pprint



def main():
    user = 'root'
    password = ''
    host = '127.0.0.1'
    database = 'prestashop_1_6'
    table = "ps_product"
    limit = 0

    new_user = input(f'nazwa użytkownika[bazowo: {user}]')
    new_password = input(f'hasło[bazowo: {password}]')
    new_host = input(f'adres hosta[bazowo: {host}]')
    new_database = input(f'nazwa bazy danych[bazowo: {database}]')
    new_table = input(f'nazwa tablicy z danymi[bazowo: {table}]')
    new_limit = input(f'limit wartości[bazowo: {limit}]')
    

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

    wb = Workbook()
    ws1 = wb.active
    ws1.title = f'{table}'

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

    for x, item in enumerate(body):
        for y in range(0,len(item)):
            ws1.cell( row = 1 + 1 + x, column = 1 + y, value = item[y])
    for x in range(0, len(headers)):
        ws1.cell( row = 1, column = 1 + x, value = headers[x])
        ws1.column_dimensions[get_column_letter(x+1)].width = 30

            
    print("wkładanie danych do obiektu...")
    
    wb.save(f'{table}.xlsx');

if __name__ == '__main__':
    main()
else:
    print("Run from import")
