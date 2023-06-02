from django.test import TestCase
from django.urls import reverse


class ProductURLsTest(TestCase):
    def test_get_products_api_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url_is_corret(self):
        url = reverse('product:detail', args=(1,))
        self.assertEqual(url, '/products/1/')

    def test_product_variant_api_url(self):
        url = reverse('product:variant', args=(1,))
        self.assertEqual(url, '/products/variant/1/')
