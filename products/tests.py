from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Product, Comment
from .forms import CommentForm


class ProductListPageTests(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(title='product1', description='this is a product', quantity=2,
                                               price=12000)

    def test_products_list_view_url_by_name(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)

    def test_products_list_page_template_used(self):
        response = self.client.get(reverse('products_list'))
        self.assertTemplateUsed(response, 'products/products_list.html')

    def test_product_is_in_stock(self):
        self.assertTrue(self.product1.is_in_stock)

    def test_products_list_page_content(self):
        response = self.client.get(reverse('products_list'))
        self.assertContains(response, self.product1.title)
        # self.assertContains(response, self.product1.price)


class ProductDetailPageTests(TestCase):

    def setUp(self):
        self.form = CommentForm()
        self.user = get_user_model().objects.create_user(username='mahdi', email='mahdi@gmail.com')
        self.product2 = Product.objects.create(title='product2', description='this is another product', quantity=3,
                                               short_description='hello', price=12000)
        self.comment1 = Comment.objects.create(product=self.product2, author=self.user,
                                               body='hello', stars='2')

    def test_product_detail_view_url_by_name(self):
        response = self.client.get(reverse('product_detail', args=[self.product2.id]))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_template_used(self):
        response = self.client.get(reverse('product_detail', args=[self.product2.id]))
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_is_in_stock(self):
        self.assertTrue(self.product2.is_in_stock)

    def test_product_detail_page_content(self):
        response = self.client.get(reverse('product_detail', args=[self.product2.id]))
        self.assertContains(response, self.product2.title)
        self.assertContains(response, self.product2.short_description)
        self.assertContains(response, self.product2.description)
