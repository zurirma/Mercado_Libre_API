import requests

class MlApi:

    def __init__(self, url):
        self.base_url = url

    def get_products(self, nombre_producto):
        path = f'{self.base_url}/sites/MLA/search?q=/{nombre_producto}'
        response = requests.get(url=path)
        return response

    def get_product_detail(self, id_producto):
        path = f'{self.base_url}/items/{id_producto}'
        response = requests.get(url=path)
        return response




