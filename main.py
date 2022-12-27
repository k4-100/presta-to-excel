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
    pprint(res["columns"])
    for x, item in enumerate(res["columns"] ):
        column_letter = get_column_letter(x+1)
        for y in range(0,len(item)):
            ws1.cell( row = 1 + y, column = 1 + x, value = item[y])
            ws1.column_dimensions[column_letter].width = 30
    # for index, item in enumerate(res["columns"]):
    #     # headers.append(item[0])
    #     pprint(item)
    #     pprint(index)
    #         ws1.cell( row=1, column = 1 + index, value=item[0] )
    cnx.close()

    
        # pprint( openpyxl.utils.cell.get_column_letter() )
        # openpyxl.uti
        # ws1.column_dimensions[column_cells[0].column].width = 30

    # for row in ws1.rows:
    #     for cell in row:
    #         if cell.value:
    #             dims[cell.column] = max((dims.get(cell.column, 0), len(str(cell.value))))    
    # for col, value in dims.items():
    #     pprint(col, value)
        # ws1.column_dimensions[col].width = 100


            
    print("wkładanie danych do obiektu...")
    
    
    wb.save('pyxltext.xlsx');


    # for x in range(0, len(body)):
    #     row = []
    #     for y in range(0, len(body[0])):
    #         row.append( body[x][y] )
    #         if y == len(body[0]) - 1:
    #             data.append( row )



    # data.headers = headers
    
    # print(f"zapisywanie danych w pliku {table}.xls...")
    # f = open(f"{table}.xls", "wb")
    # f.write( data.export('xls'));
    # f.close()

if __name__ == '__main__':
    main()
else:
    print("Run from import")
