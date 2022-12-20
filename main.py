
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
    result = cnx._execute_query("SELECT * FROM ps_product");
    cnx.close()

    pprint(result)

    print('text')


if __name__ == '__main__':
    main()
else:
    print("Run from import")
