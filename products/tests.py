from django.test import TestCase
from django.urls import reverse


class ProductPageTests(TestCase):

    def test_products_list_view_url_by_name(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_url_by_name(self):
        response = self.client.get(reverse('product_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_products_list_page_template_used(self):
        response = self.client.get(reverse('products_list'))
        self.assertTemplateUsed(response, 'products/products_list.html')

    def test_product_detail_page_template_used(self):
        response = self.client.get(reverse('product_detail', args=[1]))
        self.assertTemplateUsed(response, 'products/product_detail.html')
