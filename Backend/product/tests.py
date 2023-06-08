from django.test import TestCase
from django.urls import reverse


class ProductURLsTest(TestCase):
    def test_get_products_api_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url_is_corret(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)

    def test_product_variant_api_url(self):
        url = reverse('product:variant', args=(1,))
        self.assertEqual(url, '/products/variant/1/')

    def test_unauthorized_post (self):
        response = self.client.post('/products/', data={
            "name": "teste",
            "description_short": "asdasds asdaa sdasas",
            "description_long": "lorem"*10,
            "image": "",
            "slug": "pata-de-amendoin",
            "price_marketing": 11.0,
            "price_marketing_promotional": 9.0,
            "type": "V"
        },)

        self.assertEqual(response.status_code, 403)

    





