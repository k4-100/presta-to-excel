import requests

from pprint import pprint

headers = {'Content-Type': "application/json", 'Accept': "application/json"}

key='WECP867LZWGUGCVF4PJGA5W83GULG6M4'
api='http://localhost/prestashop_1_6/prestashop/api'



def get_products(main_url, section_url, headers, auth):
    def get_product(item):
        id = item['id']
        res = requests.get( url=f'{main_url}/{section_url}/{id}?output_format=JSON&io_format=JSON', headers=headers, auth=auth ).json()
        return res


    # pobiera dane i zbiera do jsona
    response = requests.get( url=f'{main_url}/{section_url}?output_format=JSON&io_format=JSON', headers=headers, auth=auth ).json()["products"]
    responses = []
    
    for item in response:
        responses.append( get_product(item) )


    return responses


if __name__ == '__main__':
    pprint( get_products( main_url=api, section_url='products', headers=headers, auth=(key,'')) )
else:
    print("Run from import")
