# import tablib
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import mysql.connector
from pprint import pprint

# QUERIES = [
# '''
# SELECT * FROM ps_product
# ''',
# '''
# SELECT * FROM ps_stock_available
# ''',
# '''
# SELECT id_product, reference FROM ps_product
# ''',
# ]

FIRST_QUERY = '''
SELECT * FROM ps_product
'''

DB = 'prestashop_1_6'

FILENAME = "kilka_queries"



def main():
    user = 'root'
    password = ''
    host = '127.0.0.1'
    database = DB
    # table = "ps_product"
    # limit = 0
    

    # new_user = input(f'nazwa użytkownika[bazowo: {user}]')
    # new_password = input(f'hasło[bazowo: {password}]')
    # new_host = input(f'adres hosta[bazowo: {host}]')
    # new_database = input(f'nazwa bazy danych[bazowo: {database}]')
    # new_table = input(f'nazwa tablicy z danymi[bazowo: {table}]')
    # new_limit = input(f'limit wartości[bazowo: {limit}]')
    # 

    # if new_user:
    #     user = new_user
    # if new_password:
    #     password = new_password
    # if new_host:
    #     host = new_host
    # if new_database:
    #     database = new_database
    # if new_table:
    #     table = new_table

    wb = Workbook()
    index = 1
    query = FIRST_QUERY
    while True:
        print('###################################')
        body = []
        headers = []
        
        tabname = query.split("FROM")[1]
        if index > 1:
            ws = wb.create_sheet(f'{index} {tabname}')
        else:
            ws = wb.active
            ws.title = f'{index} {tabname}'

        print(f'wykonanywanie zapytania:\n{query} ')
        print("pobieranie danych z bazy...")

        cnx = mysql.connector.connect(
                user=user, 
                password=password,
                host=host,
                database=database
        )
        cursor = cnx.cursor()
        cursor.execute(query)
        
        for item in cursor:
            body.append( item )
        cursor.close()
        
        res = cnx._execute_query(query)
        for item in res["columns"]:
            headers.append(item[0])
        cnx.close()

        for x, item in enumerate(body):
            for y in range(0,len(item)):
                ws.cell( row = 1 + 1 + x, column = 1 + y, value = item[y])
        for x in range(0, len(headers)):
            ws.cell( row = 1, column = 1 + x, value = headers[x])
            ws.column_dimensions[get_column_letter(x+1)].width = 30

        index += 1 
        print("wkładanie danych do obiektu...\n")
        
        query = input("następne zapytanie[naciśnij ENTER aby zakończyć]: ")
        
        # loop break
        if bool(query) == False:
            break

    wb.save(f'{FILENAME}.xlsx');
        

if __name__ == '__main__':
    main()
else:
    print("Run from import")
