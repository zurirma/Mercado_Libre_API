import requests
from assertpy import assert_that
import pprint
from config import BASE_URL
from api.ml_api import MlApi
from models.producto import Producto
from models.producto import Shipping

class TestBackend:

    def setup_class(self):
        self.ml_api = MlApi(url=BASE_URL)


    def test_searching_products(self):
        response = self.ml_api.get_products('macbook+pro+m1')
        response_json = response.json()
        pprint.pprint(response_json)
        assert_that(response_json['paging']['total'], description='no corresponde').is_equal_to(408)
        assert_that(response_json["paging"]["total"]).is_greater_than_or_equal_to(response_json["paging"]["limit"])

    def test_product_detail(self):
        response = self.ml_api.get_product_detail('MLA918171240')
        response_json = response.json()
        pprint.pprint(response_json)
        producto = Producto(**response_json)
        assert_that(producto.title).is_equal_to('Macbook Air A1466 Plata 13.3 , Intel Core I5 5350u  8gb De Ram 128gb Ssd, Intel Hd Graphics 6000 1440x900px Macos')
        assert_that(producto.price).is_equal_to(154999)
        assert_that(producto.accepts_mercadopago).is_true()
        assert_that(producto.currency_id).is_equal_to('ARS')
        assert_that(producto.shipping.free_shipping).is_true()

















