import json
import requests


headers = {'Content-Type': "application/json", 'Accept': "application/json"}

key='WECP867LZWGUGCVF4PJGA5W83GULG6M4'
# api=f'http://{key}@localhost/prestashop_1_6/prestashop/api?output_format=JSON&io_format=JSON'
api='http://localhost/prestashop_1_6/prestashop/api?output_format=JSON&io_format=JSON'


response = requests.get( url=api, headers=headers, auth=(key,''))

if __name__ == '__main__':
    print(response.json())
else:
    print("Run from import")
