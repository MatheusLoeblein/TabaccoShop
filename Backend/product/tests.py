from django.test import TestCase
from django.urls import reverse

from .models import Product, Variation


class ProductTest(TestCase):

    def create_product_and_variant(self):
        product_mock = Product.objects.create(
            name="teste", 
            description_short="asdasds asdaa sdasas",
            price_marketing=11.0,
            type="V")
        Variation.objects.create(
            product=product_mock,
            name='teste',
            price=19,
            price_promotional=19,
            stock=290
            )
        return product_mock
    
    def test_get_products_api_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url_is_corret(self):
        product = self.create_product_and_variant()
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_post(self):
        response = self.client.post('/products/', data={
            "name": "teste",
            "description_short": "asdasds asdaa sdasas",
            "description_long": "lorem",
            "image": "",
            "slug": "pata-de-amendoin",
            "price_marketing": 11.0,
            "price_marketing_promotional": 9.0,
            "type": "V"
        },)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, {"detail": "Authentication credentials were not provided."})


class ProductVariantTest(ProductTest, TestCase):

    def test_product_variant_api_url(self):
        url = reverse('product:variant', args=(1,))
        self.assertEqual(url, '/products/variant/1/')

    def teste_get_variant_url_return_not_fould(self):
        response = self.client.get('/products/variant/1/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"detail": "Not found."})

    def teste_get_variant_url_return_products_variants(self):
        product = self.create_product_and_variant()
        response = self.client.get(f'/products/variant/{product.id}/')
        self.assertEqual(response.status_code, 200)


